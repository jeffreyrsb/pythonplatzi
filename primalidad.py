def es_primo(numero):
    contador = 0

    for i in range (1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0 and numero != 1:
        return True
    else:
        return False


def run():
    numero = int(input("Escribe un número: "))
    if es_primo(numero):
        print("Es tu prima!")
    else:
        print("No es tu prima.")


if __name__ == "__main__":
    run()