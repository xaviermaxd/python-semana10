months = ("Enero","Febrero","Marzo","Abril","Mayo","Junio",
    "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
while True:
    numero = int(input("Numero del mes: "))
    if numero <= 0:
        # El prigrama debe terminar
        # Break => Frenar
        print("El numero debe ser mayor a 0")
        break
    print(months[numero - 1])