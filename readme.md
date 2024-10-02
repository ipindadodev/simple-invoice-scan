# Facturas No Tratadas - Script Python

Este script está diseñado para ayudar a detectar facturas que han sido incluidas fuera del rango correspondiente a su trimestre, con un margen de 10 días, y generar un reporte indicando las facturas potencialmente no tratadas en su debido momento.

## ¿Cómo funciona?

El script recorre automáticamente las carpetas que siguen el formato `[año]1T`, `[año]2T`, `[año]3T`, y `[año]4T` (por ejemplo, `20241T`, `20242T`, etc.). Para cada carpeta, revisa los archivos que contienen, los cuales se suponen que son facturas. Si la fecha de modificación del archivo (que se toma como la fecha de inclusión) está fuera del trimestre al que corresponde la carpeta más un margen de 10 días, el archivo se incluirá en el reporte `fras_no_tratadas.txt`.

### Márgenes trimestrales

El script utiliza los siguientes márgenes para los trimestres:

- **1T**: del 1 de enero al 31 de marzo (+ 10 días de margen).
- **2T**: del 1 de abril al 30 de junio (+ 10 días de margen).
- **3T**: del 1 de julio al 30 de septiembre (+ 10 días de margen).
- **4T**: del 1 de octubre al 31 de diciembre (+ 10 días de margen).

Si un archivo tiene una fecha de modificación fuera de este rango, el script lo detectará como fuera de su trimestre.

## ¿Cómo deben organizarse las facturas?

Las facturas deben estar organizadas en carpetas cuyo nombre siga el formato:

[YYYY]1T [YYYY]2T [YYYY]3T [YYYY]4T


Donde `YYYY` es el año y `1T`, `2T`, `3T`, y `4T` corresponden a los trimestres del año. Por ejemplo, para el año 2024, las carpetas se verían así:

- `20241T/` 
- `20242T/`
- `20243T/`
- `20244T/`

Dentro de cada una de estas carpetas, puedes colocar las facturas que correspondan a ese trimestre. El nombre de los archivos de las facturas puede ser cualquier formato válido de archivo.

## Reporte generado

El script generará un archivo llamado `fras_no_tratadas.txt` en el mismo directorio donde se ejecuta el script. Este archivo contiene un listado de las facturas que han sido incluidas fuera del rango correspondiente a su trimestre. 

### Estructura del reporte:

1. Al inicio, se incluye el mensaje:
Las facturas aquí reseñadas es muy probable que no hayan sido incluídas en las declaraciones trimestrales por no encontrarse disponibles o por error u omisión.

Por favor, revísalas para comprobarlo.


2. Luego, para cada trimestre, se incluirá un bloque con las facturas que están fuera de su margen. Cada factura se describe con el formato:
    - Archivo incluído: [nombre de la carpeta] > [nombre del archivo] | Fecha de inclusión: [dd/mm/yyyy].


3. Los bloques de facturas de cada trimestre están separados por tres líneas en blanco para facilitar la lectura.

## Ejecución del script

### Requisitos

- Python 3.x
- Las facturas deben estar organizadas en las carpetas de trimestres según lo descrito anteriormente.

### Ejecución

Para ejecutar el script, simplemente colócalo en el directorio raíz donde están las carpetas de los trimestres (por ejemplo, `20241T`, `20242T`, etc.) y ejecuta el script:

```bash
python scan.py
```

El reporte fras_no_tratadas.txt se generará en el mismo directorio.

Este script es útil para auditar las facturas y asegurarte de que todas han sido tratadas en el trimestre adecuado, ayudando a evitar errores de inclusión tardía o por omisión.
