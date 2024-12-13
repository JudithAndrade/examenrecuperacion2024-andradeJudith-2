def cargar_diccionario(ruta_archivo):
    diccionario = {}
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                clave, palabra = linea.strip().split(' ', 1)
                diccionario[clave] = palabra
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}.")
        exit(1)
    except Exception as e:
        print(f"Error al cargar el diccionario: {e}")
        exit(1)
    return diccionario

def decodificar_numero(numero, diccionario):
    pares = [numero[i:i+2] for i in range(0, len(numero), 2)]
    frase = []
    for par in pares:
        palabra = diccionario.get(par, "[clave no encontrada]")
        frase.append(palabra)
    return ' '.join(frase)

def validar_entrada(entrada):
    if entrada.isdigit():
        return entrada
    else:
        print("Error: Debe ingresar un número entero positivo.")
        return None

def main():
    """Funcion principal del programa. """
    ruta_diccionario = "Problema-2/diccionario.txt"

    # Cargar el diccionario
    diccionario = cargar_diccionario(ruta_diccionario)

    # Solicitar número de entrada al usuario
    entrada = input("Ingrese el número de entrada: ")
    numero = validar_entrada(entrada)
    if not numero:
        return

    # Decodificar el número
    frase = decodificar_numero(numero, diccionario)

    # Imprimir la frase decodificada
    print("Frase decodificada:", frase)

if __name__ == "__main__":
    main()
