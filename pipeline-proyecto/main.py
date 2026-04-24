# main.py
from scripts.ingesta import ejecutar_ingesta

def ejecutar_pipeline():
    print("--- Iniciando Pipeline de Datos ---")
    
    # PASO 1: Ingesta
    ejecutar_ingesta()
    
    # Aquí añadirás el PASO 2 (Transformación) en la siguiente sesión
    print("--- Pipeline finalizado con éxito ---")

if __name__ == "__main__":
    ejecutar_pipeline()