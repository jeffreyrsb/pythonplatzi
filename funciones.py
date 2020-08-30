# def imprimir_mensaje():
#     print("Mensaje especial: ")
#     print("¡Estoy aprendiendo a usar funciones!")

# print("""
# """)
# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def conversacion(mensaje):
    print("")
    print("Hola =)")
    print("Elegiste la opción " + str(mensaje))
    print("Adiós")
    print("")

opcion = int(input("""
Elige una opciónc(1, 2, 3):
"""))
if opcion == 1:
    conversacion(opcion)
elif opcion ==2:
    conversacion(opcion)
elif opcion == 3:
    conversacion(opcion)
else:
    print("Escribe la opción correcta 🤡🤡🤡🤡🤡🤡🤡")