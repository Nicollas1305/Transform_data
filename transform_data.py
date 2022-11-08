from pyautogui import sleep
import tabula
import pandas as pd
import shutil


file_path = "Anexo I - Lista completa de procedimentos (.pdf).pdf"
df = tabula.convert_into(file_path, "output_transform_data/output.csv", output_format= "csv", pages= '3-108')

print("Start Zip")
shutil.make_archive('Teste_Nicollas_Lima', 'zip', 'output_transform_data')
print("End Zip")