import os
from datetime import datetime, timedelta
import re

# Función para generar los márgenes del trimestre según el año y el trimestre
def obtener_margen_trimestre(año, trimestre):
    if trimestre == "1T":
        inicio = datetime(año, 1, 1)
        fin = datetime(año, 3, 31) + timedelta(days=10)
    elif trimestre == "2T":
        inicio = datetime(año, 4, 1)
        fin = datetime(año, 6, 30) + timedelta(days=10)
    elif trimestre == "3T":
        inicio = datetime(año, 7, 1)
        fin = datetime(año, 9, 30) + timedelta(days=10)
    elif trimestre == "4T":
        inicio = datetime(año, 10, 1)
        fin = datetime(año, 12, 31) + timedelta(days=10)
    return inicio, fin

# Obtener el directorio actual de ejecución del script
root_dir = os.getcwd()

# Función para revisar si el archivo está fuera del rango permitido
def archivo_fuera_de_trimestre(fecha_archivo, inicio_trimestre, fin_trimestre):
    return not (inicio_trimestre <= fecha_archivo <= fin_trimestre)

# Crear un archivo para guardar el reporte
with open("fras_potencialmente_no_tratadas.txt", "w") as reporte:
    # Escribir el mensaje inicial en el archivo
    reporte.write("Las facturas aquí reseñadas es muy probable que no hayan sido incluidas en las declaraciones trimestrales por no encontrarse disponibles o por error u omisión.\n\nPor favor, revísalas o las declaraciones correspondientes para comprobarlo.\n\nCabe una mínima posibilidad de que se haya escapado alguna, pero el proceso es automático, por lo que esta es una buena base para empezar.\n\nDisculpa las molestias.\n\n")

    # Expresión regular para extraer el año y trimestre de las carpetas (ejemplo: 20241T)
    patron_carpeta = re.compile(r'(\d{4})([1-4]T)')
    
    # Recorrer las carpetas en el directorio actual
    for trimestre, trimestre_num in [("1T", 1), ("2T", 2), ("3T", 3), ("4T", 4)]:
        for carpeta in os.listdir(root_dir):
            match = patron_carpeta.match(carpeta)
            if match:
                año = int(match.group(1))
                trimestre_actual = match.group(2)
                
                if trimestre_actual == trimestre:
                    carpeta_path = os.path.join(root_dir, carpeta)
                    if os.path.isdir(carpeta_path):
                        # Obtener los márgenes del trimestre actual
                        inicio_trimestre, fin_trimestre = obtener_margen_trimestre(año, trimestre_actual)
                        
                        for archivo in os.listdir(carpeta_path):
                            archivo_path = os.path.join(carpeta_path, archivo)
                            if os.path.isfile(archivo_path):
                                # Obtener la fecha de modificación del archivo
                                fecha_modificacion = datetime.fromtimestamp(os.path.getmtime(archivo_path))
                                # Comprobar si está fuera del trimestre
                                if archivo_fuera_de_trimestre(fecha_modificacion, inicio_trimestre, fin_trimestre):
                                    # Escribir la ruta y la fecha de inclusión en el archivo
                                    reporte.write(f"Archivo incluido: {carpeta} > {archivo} | Fecha de inclusión: {fecha_modificacion.strftime('%d/%m/%Y')}\n")
        
        # Añadir dos saltos de línea tras las facturas de cada trimestre
        reporte.write("\n\n")

print("Reporte generado: fras_potencialmente_no_tratadas.txt")
