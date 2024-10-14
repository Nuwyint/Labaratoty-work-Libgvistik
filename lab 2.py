# This is a sample Python script.
import math
import sys
import numpy as np
import matplotlib.pyplot as plt


def func(x1, x2):
    # func_value = ((((x1 - a) * math.cos(alph) + (x2 - b) * math.sin(alph)) ** 2) / (c ** 2)) + (
    #         (((x2 - b) * math.cos(alph) - (x1 - a) * math.sin(alph)) ** 2) / (d ** 2))
    # return func_value
    rosenbrock = (100 * ((x2 - x1 ** 2) ** 2) + (1 - x1) ** 2)
    return rosenbrock


x1 =40
x2 = 60
a = 0
b = 1
c = 2
d = 4
alph = 40
m = 0
n = 2
f = []
h = 0.01
x = []
optimal_points = []
e = 0.1
optimal_pointsPowell = []
k = 0
optimal_pointsPowell.append((x1, x2))


def draw(optimal_points=[], last_points=[], optimal_pointsPowell=[]):
    x1_range = np.linspace(-30, 60, 1000)
    x2_range = np.linspace(-30, 60, 1000)

    X1, X2 = np.meshgrid(x1_range, x2_range)
    Z = func(X1, X2)

    plt.contour(X1, X2, Z, levels=30, cmap='viridis')

    if optimal_points:
        x1_optimal, x2_optimal = zip(*optimal_points)
        plt.scatter(x1_optimal, x2_optimal, c='blue', marker='x', label='Оптимальные точки')
        plt.plot(x1_optimal, x2_optimal, '-o', color='blue', linewidth=1, markersize=4)
        #for i, (x1, x2) in enumerate(optimal_points):
           # plt.annotate(f'{i + 1}', (x1, x2), textcoords="offset points", xytext=(-10, -10), ha='center')

    if optimal_pointsPowell:
        x1_optimalPowell, x2_optimalPowell = zip(*optimal_pointsPowell)
        plt.scatter(x1_optimalPowell, x2_optimalPowell, c='green', marker='x', label='Оптимальные точки Powell')
        plt.plot(x1_optimalPowell, x2_optimalPowell, '-o', color='green', linewidth=1, markersize=4)
        #for i, (x1, x2) in enumerate(optimal_pointsPowell):
            #plt.annotate(f'{i + 1}', (x1, x2), textcoords="offset points", xytext=(-10, -10), ha='center')

    if last_points:
        x1_last, x2_last = zip(*last_points)
        plt.scatter(x1_last, x2_last, c='red', marker='x', label='Итоговая точка')

    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Линии уровня функции')

    plt.show()


print(func(x1, x2 + h))
print(func(x1, x2 - h))
f.append(func(x1, x2))
f0 = f[0]
f1 = f0
while (f1 < f0 or f1 == f0 or m == 0):
    k += 1
    print(k)
    f0 = f1
    x01 = x1
    x02 = x2
    if (func(x1, x2 + h) > func(x1, x2 - h)):
        h = h * (-1)
    x2 += h
    print(func(x1, x2))
    f.append(func(x1, x2))
    m += 1
    optimal_points.append((x1, x2))
    while ((f[m] < f[m - 1])):
        x2 += h
        f.append(func(x1, x2))
        m += 1
        optimal_points.append((x1, x2))
        print(func(x1, x2))
    x2 -= h
    print(func(x1, x2))
    if (func(x1 + h, x2) > func(x1 - h, x2)):
        h = h * (-1)
        print(func(x1, x2))
    x1 += h
    f.append(func(x1, x2))
    m += 1
    optimal_points.append((x1, x2))
    while ((f[m] < f[m - 1])):
        x1 += h
        f.append(func(x1, x2))
        optimal_points.append((x1, x2))
        m += 1
    f1 = f[m]
    print("Начальные точки")
    print(x01, x02)
    print("Конечные точки")
    print(x1, x2)

    optimal_pointsPowell.append((x1, x2))
    h2 = x2 - x02
    h1 = x1 - x01
    print(x1, x2)

    optimal_pointsPowell.append((x1, x2))

    while (func(x1, x2) < func(x1 - h1, x2 - h2)):
        print("Делаем шаг")
        x1 += h1
        x2 += h2
        print(x1, x2)
        optimal_pointsPowell.append((x1, x2))
        print("значение предыдущего шага")
        print(func(x1 - h1, x2 - h2))
        print("значение конечного шага")
        print(func(x1, x2))

    print("Делаем шаг обратно")
    x1 -= h1
    x2 -= h2
    f.append(func(x1, x2))
    f.append(func(x1, x2))
    optimal_pointsPowell.append((x1, x2))
    f.append(func(x1, x2))
    print(x1, x2)
    print("----------------------------------------")
    if(k == 100000):
        break

print("Минимальное значение функции при x1: " + str(x1) + " x2: " + str(x2))  # Print x1 and x2
print("Принимает значение:")
print(func(x1, x2))
draw(optimal_points, [(x1, x2)], optimal_pointsPowell)


# ----------------------------------------------------------------------------------------------------------------------
# import itertools
# import math
# import sys
# import numpy as np
# import matplotlib.pyplot as plt
#
# x1 = 7
# x2 = -3
# a = 0
# b = 1
# c = 2
# d = 4
# alph = 40
# m = 0
# n = 2
# x = []
# f = [0,0,0]
# optimal_points1 = []
# optimal_points2 = []
# optimal_points3 = []
# proverka_points = []
# optimal_points4 = []
# x1 = 4.85
# y1 = -4.03
# x2 = 4.85
# y2 = -3.0
# x3 = 5.85
# y3 = -4.03
# x4 =0.0
# y4 = 0.0
# opt_point = []
#
# def func(x1, x2):
#     alph_rad = math.radians(alph)
#     func_value = ((((x1 - a) * math.cos(alph_rad) + (x2 - b) * math.sin(alph_rad)) ** 2) / (c ** 2)) + (
#     (((x2 - b) * math.cos(alph_rad) - (x1 - a) * math.sin(alph_rad)) ** 2) / (d ** 2))
#     return func_value
#
#
# # def func(x1, x2):
# #     return 100 * (x2 - x1**2)**2 + (1 - x1)**2
#
# def draw(optimal_points1=[], optimal_points2=[], optimal_points3=[], last_points=[]):
#     x1_range = np.linspace(-5, 10, 1000)
#     x2_range = np.linspace(-6, 5, 1000)
#
#     X1, X2 = np.meshgrid(x1_range, x2_range)
#     Z = func(X1, X2)
#
#     levels = np.linspace(np.min(Z), np.max(Z), 50)
#
#     plt.contour(X1, X2, Z, levels=levels, cmap='viridis')
#
#     if last_points:
#         x1_last, x2_last = zip(*last_points)
#         plt.scatter(x1_last, x2_last, c='red', marker='x', label='Итоговая точка')
#         for i, (x, y) in enumerate(last_points, 1):
#             plt.annotate(f'Финал\n{i}', (x, y), fontsize=12, color='red')
#
#     if optimal_points1:
#         x1_optimal, x2_optimal = zip(*optimal_points1)
#         plt.scatter(x1_optimal, x2_optimal, c='blue', marker='x', label='Оптимальные точки')
#         for i, (x, y) in enumerate(optimal_points1, 1):
#             plt.annotate(1, (x, y), fontsize=12, color='blue')
#
#         plt.plot(x1_optimal, x2_optimal, c='blue')
#
#     if optimal_points2:
#         x1_optimal, x2_optimal = zip(*optimal_points2)
#         plt.scatter(x1_optimal, x2_optimal, c='blue', marker='x', label='Оптимальные точки')
#         for i, (x, y) in enumerate(optimal_points2, 1):
#             plt.annotate(2, (x, y), fontsize=12, color='blue')
#
#         plt.plot(x1_optimal, x2_optimal, c='blue')
#     if optimal_points3:
#         x1_optimal, x2_optimal = zip(*optimal_points3)
#         plt.scatter(x1_optimal, x2_optimal, c='blue', marker='x', label='Оптимальные точки')
#         for i, (x, y) in enumerate(optimal_points3, 1):
#             plt.annotate(3, (x, y), fontsize=12, color='blue')
#         plt.plot(x1_optimal, x2_optimal, c='blue')
#     if optimal_points1 and optimal_points2 and optimal_points3:
#         for i in range(min(len(optimal_points1), len(optimal_points2), len(optimal_points3))):
#             x1_optimal1, x2_optimal1 = optimal_points1[i]
#             x1_optimal2, x2_optimal2 = optimal_points2[i]
#             x1_optimal3, x2_optimal3 = optimal_points3[i]
#
#             plt.scatter(x1_optimal1, x2_optimal1, c='blue', marker='x', label='Оптимальные точки 1')
#             plt.scatter(x1_optimal2, x2_optimal2, c='red', marker='x', label='Оптимальные точки 2')
#             plt.scatter(x1_optimal3, x2_optimal3, c='green', marker='x', label='Оптимальные точки 3')
#
#             # Соединяем точки линиями
#             plt.plot([x1_optimal1, x1_optimal2, x1_optimal3, x1_optimal1],
#                      [x2_optimal1, x2_optimal2, x2_optimal3, x2_optimal1], c='purple')
#
#
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.title('Линии уровня функции')
#
#     plt.show()
#
# def methodSimplex(f,  x1, y1, x2, y2, x3, y3):
#     x1arr = []
#     y1arr = []
#     for i in range(100):
#         f = [func(x1, y1), func(x2, y2), func(x3, y3)]
#         optimal_points1.append((x1, y1))
#         optimal_points2.append((x2, y2))
#         optimal_points3.append((x3, y3))
#         proverka_points.append(func(x1, y1))
#         proverka_points.append(func(x2, y2))
#         proverka_points.append(func(x3, y3))
#
#         if f.index(max(f)) == 0 :
#             x1 = x3 + x2 - x1
#             y1 = y3 + y2 - y1
#             x1arr.append(x1)
#             y1arr.append(y1)
#             if(i > 6 and ((proverka_points[m - 1] == proverka_points[m - 7]) and
#                           (proverka_points[m - 2] == proverka_points[m - 8]) and
#                           (proverka_points[m - 3] == proverka_points[m - 9]))):
#                 x1 = (((x3 + x2)/2) + x1) / 2
#                 y1 = (((y3 + y2)/2) + y1) / 2
#                 optimal_points1.append((x1, y1))
#
#         elif f.index(max(f)) == 1:
#             x2 = x3 + x1 - x2
#             y2 = y3 + y1 - y2
#             if (i > 6 and ((proverka_points[m - 1] == proverka_points[m - 7]) and
#                            (proverka_points[m - 2] == proverka_points[m - 8]) and
#                            (proverka_points[m - 3] == proverka_points[m - 9]))):
#                 x2 = ((x1 + x3)*0.5 + x2) / 2
#                 y2 = ((y1 + y3)*0.5 + y2) / 2
#         elif f.index(max(f)) == 2:
#             x3 = x2 + x1 - x3
#             y3 = y2 + y1 - y3
#             if (i > 6 and ((proverka_points[m - 1] == proverka_points[m - 7]) and
#                            (proverka_points[m - 2] == proverka_points[m - 8]) and
#                            (proverka_points[m - 3] == proverka_points[m - 9]))):
#                 x3 = ((x1 + x2)*0.5 + x3) / 2
#                 y3 = ((y1 + y2)*0.5 + y3) / 2
#         if (math.sqrt(((sum(f))**2/(i+1))) < 0.001):
#             f = [func(x1, y1), func(x2, y2), func(x3, y3)]
#             if f.index(min(f)) == 0:
#                 last_points = [x1, y1]
#                 print("Минимальное значение функции при x1:")
#                 print(x1)
#                 print("Минимальное значение функции при x2:")
#                 print(y1)
#                 print("Значение функции в этой точке:")
#                 print(min(f))
#                 draw(optimal_points1, optimal_points2, optimal_points3, [(x1, y1)])
#             elif f.index(min(f)) == 1:
#                 last_points = [x2, y2]
#                 print("Минимальное значение функции при x1:")
#                 print(x2)
#                 print("Минимальное значение функции при x2:")
#                 print(y2)
#                 print("Значение функции в этой точке:")
#                 print(min(f))
#                 draw(optimal_points1, optimal_points2, optimal_points3, [(x2, y2)])
#             elif f.index(min(f)) == 2:
#                 last_points = [x3, y3]
#                 print("Минимальное значение функции при x1:")
#                 print(x3)
#                 print("Минимальное значение функции при x2:")
#                 print(y3)
#                 print("Значение функции в этой точке:")
#                 print(min(f))
#                 draw(optimal_points1,optimal_points2,optimal_points3, [(x3, y3)])
#
#
#
#
# methodSimplex(f, x1, y1, x2, y2, x3, y3)

