def solicitar_numero():
    """Solicita al usuario un número entero positivo y lo valida."""
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            if numero > 0:
                return numero
            else:
                print("Por favor, ingrese un número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero positivo.")

def reducir_a_un_digito(n):
    """Reduce un número a un solo dígito sumando sus dígitos recursivamente."""
    while n >= 10:
        n = sum(int(digito) for digito in str(n))
    return n

def procesar_pares(numero):
    """Simula la carrera entre los pares de dígitos de un número."""
    numero_str = str(numero)
    resultados = []

    while len(numero_str) > 1:
        print("\nNueva ronda:")
        nuevo_numero = ""

        for i in range(0, len(numero_str) - 1, 2):
            carro_x = reducir_a_un_digito(int(numero_str[i]) + int(numero_str[i + 1]))
            carro_y = reducir_a_un_digito(int(numero_str[i + 1]) + int(numero_str[i + 2])) if i + 2 < len(numero_str) else None

            if carro_y is not None:
                if carro_x > carro_y:
                    ganador = "Carro_X"
                elif carro_x < carro_y:
                    ganador = "Carro_Y"
                else:
                    ganador = "Empate"
                print(f"{numero_str[i]}+{numero_str[i + 1]} = {carro_x}\t{numero_str[i + 1]}+{numero_str[i + 2]} = {carro_y}\tGanador: {ganador}")
            else:
                print(f"{numero_str[i]}+{numero_str[i + 1]} = {carro_x}\tGanador: Carro_X")

            nuevo_numero += str(carro_x if carro_y is None else max(carro_x, carro_y))

        numero_str = nuevo_numero
        resultados.append(numero_str)

    print("\nResultado final de la carrera:", numero_str)
    return resultados

# Programa principal
if __name__ == "__main__":
    numero = solicitar_numero()
    procesar_pares(numero)
