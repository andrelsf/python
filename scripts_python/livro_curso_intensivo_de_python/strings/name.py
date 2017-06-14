#
name = "andre l s ferreira"

# Muda a primeira letra para maiuscula
print(name.title(), "\n")

# Muda todos caracteres para letras maiusculas
print(name.upper(), "\n")

# Muda todos caracteres para letras minusculas
print(name.lower(), "\n")

# Concatenação de STRINGS
print("CONCATENACAO de Strings\n".upper())

first_name = "Andre"
last_name = "Ferreira"
full_name = first_name + " " + last_name

message = "Hello my friend " + full_name.title() + "!"

print(message)

# Acrescentando espaços em branco em strings com tabulações ou quebra de linha
# Adiciona quebra de linha
print("\n" + message + "\n")

# Adiciona tabulação
print("\t" + message)

print("Languages:\n\tPython\n\tJava\n\tC\n\tC++\n\tJavaScript")

# Removendo os espaços em branco
#>>> favorite_language = ' python '
#>>> favorite_language.rstrip()
#' python'
#>>> favorite_language.lstrip()
#'python '
#>>> favorite_language.strip()
#'python'
#
print("\n"+ "Removendo espaços em branco" + "\n")

favorite_language = 'Python '
print("Favorite Language: " + favorite_language)

print("Favorite Language: " + favorite_language.rstrip())

print("Favorite Language: " + favorite_language.strip())

print(message)

print("RSTrip: " + message.rstrip())

print("STrip.: " + message.strip())

