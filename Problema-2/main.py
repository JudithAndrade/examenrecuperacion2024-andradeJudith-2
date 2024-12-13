# Programa para decodificar un texto numérico basado en un diccionario

def cargar_diccionario(nombre_archivo):
    """
    Carga el diccionario desde un archivo de texto.
    Cada línea del archivo debe tener el formato: "número palabra".

    :param nombre_archivo: Nombre del archivo de diccionario.
    :return: Un diccionario con claves numéricas (str) y valores de palabras.
    """
    diccionario = {}
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split(" ", 1)
                if len(partes) == 2:
                    clave, palabra = partes
                    diccionario[clave] = palabra
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return diccionario

def decodificar_numero(numero_entrada, diccionario):
    """
    Decodifica un número de entrada basado en un diccionario.

    :param numero_entrada: Número entero o cadena de pares de dígitos.
    :param diccionario: Diccionario con claves numéricas (str) y palabras como valores.
    :return: Frase decodificada.
    """
    numero_str = str(numero_entrada)
    frase = []

    for i in range(0, len(numero_str), 2):
        par = numero_str[i:i+2]
        palabra = diccionario.get(par, "[?]")  # Usa [?] si el par no está en el diccionario
        frase.append(palabra)

    return " ".join(frase)

def main():
    """
    Función principal para ejecutar el programa.
    """
    nombre_archivo = "diccionario.txt"
    numero_entrada = input("Introduce el número de entrada (pares de dígitos): ")

    # Cargar el diccionario desde el archivo
    diccionario = cargar_diccionario(nombre_archivo)

    # Decodificar el número
    if diccionario:
        frase_decodificada = decodificar_numero(numero_entrada, diccionario)
        print("Frase decodificada:", frase_decodificada)
    else:
        print("No se pudo cargar el diccionario.")

if __name__ == "__main__":
    main()
