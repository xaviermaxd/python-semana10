alumnos = ("jose","alex","jorge","luis")
i = 0
while True:
    n = int(input("ingrese un numero: "))
    if n > 4:
        print("numero incorrecto")
        break
    print(alumnos[n-1])