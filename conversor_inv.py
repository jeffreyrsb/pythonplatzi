dolares = input ("¿Cuántos dólares tienes?: ")
dolares = float(dolares)
valor_soles = 1/3.56
soles = dolares / valor_soles
soles = round(soles, 2)
soles = str(soles)
print("Tienes S/." + soles + " soles")