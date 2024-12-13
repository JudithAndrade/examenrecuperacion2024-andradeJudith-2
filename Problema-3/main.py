import string

def limpiar_texto(linea):
    """
    Limpia una línea de texto eliminando caracteres no alfabéticos
    y convirtiendo todo a minúsculas.
    """
    # Usamos una lista para filtrar solo los caracteres que son letras o espacios
    return ''.join([c.lower() for c in linea if c.isalpha() or c.isspace()])

def ordenar_palabras(linea):
    """
    Ordena las palabras en una línea alfabéticamente.
    """
    palabras = linea.split()  # Dividimos en palabras
    return ' '.join(sorted(palabras))  # Ordenamos y unimos

def procesar_archivo(nombre_archivo):
    """
    Procesa un archivo de texto, limpia y ordena cada línea.
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()  # Leemos las líneas del archivo
        
        lineas_procesadas = []

        for linea in lineas:
            linea_limpia = limpiar_texto(linea)  # Limpiamos la línea
            linea_ordenada = ordenar_palabras(linea_limpia)  # Ordenamos las palabras
            lineas_procesadas.append(linea_ordenada)  # Guardamos la línea procesada

        return lineas_procesadas

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def guardar_resultados(nombre_archivo_salida, lineas):
    """
    Guarda las líneas procesadas en un archivo de salida.
    """
    try:
        with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo:
            for linea in lineas:
                archivo.write(linea + '\n')
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def main():
    """
    Función principal para ejecutar el programa.
    """
    nombre_archivo_entrada = input("Ingrese el nombre del archivo de entrada: ").strip()
    nombre_archivo_salida = input("Ingrese el nombre del archivo de salida: ").strip()

    # Procesamos el archivo y obtenemos las líneas ordenadas
    lineas_ordenadas = procesar_archivo(nombre_archivo_entrada)

    if lineas_ordenadas:
        guardar_resultados(nombre_archivo_salida, lineas_ordenadas)
        print(f"Se han guardado las líneas procesadas en '{nombre_archivo_salida}'.")

if __name__ == "__main__":
    main()
