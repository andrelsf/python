#
imposto = int(input("Imposto: "))

if imposto < 10:
    print("Medio")
elif imposto < 27.5:
    print("Alto")
else:
    print("Muito Alto")
