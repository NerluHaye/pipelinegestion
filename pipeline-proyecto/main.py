
from scripts.ingesta import ejecutar_ingesta
from scripts.validacion import validar_y_limpiar

def ejecutar_pipeline():
    
    
    
    
    ejecutar_ingesta()
    
    
    
    validar_y_limpiar()
    
    print("\n--- PIPELINE FINALIZADO CON ÉXITO ---")

if __name__ == "__main__":
    ejecutar_pipeline()