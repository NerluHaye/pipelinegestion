import pandas as pd
import os

# Configuración de rutas automáticas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_RAW = os.path.join(BASE_DIR, "data", "raw")
RUTA_PROCESSED = os.path.join(BASE_DIR, "data", "processed")
RUTA_REPORTS = os.path.join(BASE_DIR, "data", "reports")

def validar_y_limpiar():
    # 1. Buscar el archivo más reciente descargado en la etapa previa
    if not os.path.exists(RUTA_RAW):
        print("Error: No existe la carpeta raw. Ejecuta primero ingesta.py")
        return
        
    archivos = [f for f in os.listdir(RUTA_RAW) if f.endswith('.csv')]
    if not archivos:
        print("No se encontraron archivos CSV para validar.")
        return
    
    archivo_reciente = os.path.join(RUTA_RAW, sorted(archivos)[-1])
    df = pd.read_csv(archivo_reciente)
    reporte = []

    # --- VALIDACIÓN ESTRUCTURAL ---
    # Verificar columnas obligatorias y tipos 
    cols_obligatorias = ['total_cup_points', 'species', 'country_of_origin']
    for col in cols_obligatorias:
        if col not in df.columns:
            reporte.append(f"ESTRUCTURA: Falta la columna obligatoria '{col}'.")

    # --- LIMPIEZA BÁSICA ---
    # Eliminar duplicados y nulos en columnas críticas 
    antes = len(df)
    df = df.drop_duplicates().dropna(subset=cols_obligatorias)
    reporte.append(f"LIMPIEZA: Se eliminaron {antes - len(df)} registros duplicados o con nulos.")

    # --- VALIDACIÓN SEMÁNTICA ---
    # Coherencia lógica: puntaje de café entre 0 y 100 [cite: 5, 9]
    if 'total_cup_points' in df.columns:
        fuera_rango = df[(df['total_cup_points'] < 0) | (df['total_cup_points'] > 100)]
        if not fuera_rango.empty:
            reporte.append(f"SEMÁNTICA: {len(fuera_rango)} filas con puntajes fuera de rango (0-100).")
            df = df[(df['total_cup_points'] >= 0) & (df['total_cup_points'] <= 100)]

    # --- GUARDAR RESULTADOS ---
    os.makedirs(RUTA_PROCESSED, exist_ok=True)
    os.makedirs(RUTA_REPORTS, exist_ok=True)

    # Guardar dataset procesado [cite: 22]
    df.to_csv(os.path.join(RUTA_PROCESSED, "datos_limpios.csv"), index=False)
    
    # Generar reporte de errores 
    with open(os.path.join(RUTA_REPORTS, "reporte_errores.txt"), "w") as f:
        f.write("REPORTE DE VALIDACIÓN Y CALIDAD\n")
        f.write("==============================\n")
        f.write("\n".join(reporte) if reporte else "Validación exitosa: No se detectaron errores.")
    
    print(f"Validación terminada. Datos en 'processed' y reporte en 'reports'.")

if __name__ == "__main__":
    validar_y_limpiar()