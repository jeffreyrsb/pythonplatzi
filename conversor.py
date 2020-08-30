def conversor(tipo_moneda, valor_dolar):
    soles = input("¿Cuántos " + tipo_moneda + " tienes?: ")
    soles = float(soles)
    dolares = soles / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu="""
Bienvenido al conversor de monedas 💲

1. Soles
2. Pesos colombianos
3. Pesos argentinos
4. Pesos mexicanos

Elige una opción: """

opcion=int(input(menu))

if opcion==1:
    conversor("soles", 3.56)
elif opcion==2:
    conversor("pesos colombianos", 3875)
elif opcion == 3:
    conversor("pesos argentinos", 65)
elif opcion == 4:
    conversor("pesos mexicanos", 24)
else:
    print("Ingresa una opción correcta 🤡")
