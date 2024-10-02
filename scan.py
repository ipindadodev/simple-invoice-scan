import os
from datetime import datetime, timedelta
import re

# Function to generate the date range for each quarter based on the year and quarter
def get_quarter_range(year, quarter):
    if quarter == "1T":
        start = datetime(year, 1, 1)
        end = datetime(year, 3, 31) + timedelta(days=10)
    elif quarter == "2T":
        start = datetime(year, 4, 1)
        end = datetime(year, 6, 30) + timedelta(days=10)
    elif quarter == "3T":
        start = datetime(year, 7, 1)
        end = datetime(year, 9, 30) + timedelta(days=10)
    elif quarter == "4T":
        start = datetime(year, 10, 1)
        end = datetime(year, 12, 31) + timedelta(days=10)
    return start, end

# Get the current directory where the script is running
root_dir = os.getcwd()

# Function to check if a file is outside the allowed date range for its quarter
def is_file_outside_quarter(file_date, start_quarter, end_quarter):
    return not (start_quarter <= file_date <= end_quarter)

# Create a file to save the report
with open("fras_potencialmente_no_tratadas.txt", "w") as report:
    # Write the initial message in the report file
    report.write("Las facturas aquí reseñadas es muy probable que no hayan sido incluidas en las declaraciones trimestrales por no encontrarse disponibles o por error u omisión.\n\nPor favor, revísalas o las declaraciones correspondientes para comprobarlo.\n\nCabe una mínima posibilidad de que se haya escapado alguna, pero el proceso es automático, por lo que esta es una buena base para empezar.\n\nDisculpa las molestias.\n\n")

    # Regular expression to extract the year and quarter from the folder names (e.g., 20241T)
    folder_pattern = re.compile(r'(\d{4})([1-4]T)')
    
    # Loop through the folders in the current directory
    for quarter, quarter_num in [("1T", 1), ("2T", 2), ("3T", 3), ("4T", 4)]:
        for folder in os.listdir(root_dir):
            match = folder_pattern.match(folder)
            if match:
                year = int(match.group(1))
                current_quarter = match.group(2)
                
                if current_quarter == quarter:
                    folder_path = os.path.join(root_dir, folder)
                    if os.path.isdir(folder_path):
                        # Get the start and end dates of the current quarter
                        start_quarter, end_quarter = get_quarter_range(year, current_quarter)
                        
                        for file in os.listdir(folder_path):
                            file_path = os.path.join(folder_path, file)
                            if os.path.isfile(file_path):
                                # Get the modification date of the file
                                file_date = datetime.fromtimestamp(os.path.getmtime(file_path))
                                # Check if the file is outside the quarter's date range
                                if is_file_outside_quarter(file_date, start_quarter, end_quarter):
                                    # Write the file path and the inclusion date in the report
                                    report.write(f"Archivo incluido: {folder} > {file} | Fecha de inclusión: {file_date.strftime('%d/%m/%Y')}\n")
        
        # Add two blank lines after the group of files for each quarter
        report.write("\n\n")

print("Reporte generado: fras_potencialmente_no_tratadas.txt")
