n = int(input("ingrese una edad: "))
edades = (12,13,11,10,12,11,13,11)
x = 0
i = 0
while i < 8:
    if n == edades[i]:
        x += 1
    i += 1
print(x)
