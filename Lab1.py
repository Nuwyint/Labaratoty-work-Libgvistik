# Таблица шифровки ключевых слов и символов
token_table = {
    "read": 1,
    "if": 2,
    "or": 3,
    "then": 4,
    "writeln": 5,
    "DO": 14,
    "end": 15,
    "PUT": 16,
    "DATA": 17,
    "/": 18,
    "(": 6,
    ")": 7,
    ";": 8,
    ",": 9,
    ">": 11,
    "<": 10,
    "=": 19,
    "+": 20,
    "ид": 12,
    "const": 13
}

# Таблица переменных (идентификаторов)
variable_table = {}
variable_counter = 1

# Исходный код
code = """
Z = Z + 1;
if Z > N then DO;
Z = Z / N;
PUT DATA (Z);
end;
"""

lines = code.strip().split('\n')
print(lines)

def translate_line(line):
    tokens = line.replace("(", " ( ").replace(")", " ) ").replace(";", " ; ").replace(",", " , ").split()
    translated_tokens = []

    for token in tokens:
        if token in token_table:
            translated_tokens.append(str(token_table[token]))
        elif token.isdigit():
            translated_tokens.append(str(token_table["const"]))
            translated_tokens.append(token)
        else:
            if token not in variable_table:
                global variable_counter
                variable_table[token] = variable_counter
                variable_counter += 1
            translated_tokens.append(str(token_table["ид"]))
            translated_tokens.append(str(variable_table[token]))

    return " ".join(translated_tokens)

translated_code = [translate_line(line) for line in lines]

print("Таблица шифровки:")
for key, value in sorted(token_table.items()):
    print(f"{key}\t{value}")

print("\nТаблица переменных:")
for key, value in sorted(variable_table.items(), key=lambda item: item[1]):
    print(f"{value}\t{key}")

print("\nПереведенный код:")
for line in translated_code:
    print(line)
