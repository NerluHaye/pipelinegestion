import os
import requests
from datetime import datetime


URL_ORIGEN = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-07/coffee_ratings.csv"
CARPETA_RAW = "data/raw"

def ejecutar_ingesta():
    
    if not os.path.exists(CARPETA_RAW):
        os.makedirs(CARPETA_RAW)
        print(f"Carpeta creada: {CARPETA_RAW}")

    try:
        
        print("Descargando datos...")
        respuesta = requests.get(URL_ORIGEN)
        respuesta.raise_for_status() # Control de errores

        
        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        nombre_archivo = f"ingesta_{fecha_hoy}.csv"
        ruta_final = os.path.join(CARPETA_RAW, nombre_archivo)

        with open(ruta_final, "wb") as f:
            f.write(respuesta.content)
            
        print(f"¡Éxito! Datos guardados en: {ruta_final}")

    except Exception as e:
        print(f"Error en la ingesta: {e}")

if __name__ == "__main__":
    ejecutar_ingesta()