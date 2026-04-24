import os
import requests
from datetime import datetime

# Configuración de rutas automáticas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARPETA_RAW = os.path.join(BASE_DIR, "data", "raw")

URL_ORIGEN = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-07/coffee_ratings.csv"

def ejecutar_ingesta():
    # Garantiza la arquitectura de carpetas
    os.makedirs(CARPETA_RAW, exist_ok=True)

    try:
        print(f"Descargando datos desde: {URL_ORIGEN}")
        respuesta = requests.get(URL_ORIGEN)
        respuesta.raise_for_status()

        # Nombre de archivo con fecha para trazabilidad
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