sueldos = (3000,2500,4000,4200,3800)
i = 0
menor = sueldos[0]
mayor = sueldos[0]
while i < 5:
    if menor > sueldos[i]:
        menor = sueldos[i]
    if mayor < sueldos[i]:
        mayor = sueldos[i]
    i+=1
print("el sueldo menor es: ",menor)
print("el suledo mayor es: ",mayor)