pesos = input ("¿Cuántos soles tienes?: ")
pesos = float(pesos)
valor_dolar = 3.56
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")
