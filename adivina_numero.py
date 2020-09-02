import random


def run():
    numero_random = random.randint(1, 100)
    numero_elegido = int(input("Elige un número del 1 al 100: "))
    while numero_elegido != numero_random:
        if numero_elegido < numero_random:
            print ("El número es más grande :P")
        else:
            print("El número es más pequeño :P")
        numero_elegido = int(input("\nElige otro número: "))
    print("\nGanaste papu!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \nEres heavy!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


if __name__ == "__main__":
    run()