numeros = []
while True:
    num = int(input("ingrese un numero: "))
    if num <= 0:
        break
    numeros.append(num)
numeros.sort()
numeros.reverse()
print(numeros)