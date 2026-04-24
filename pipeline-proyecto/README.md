# Pipeline de Datos - Coffee Quality Project

## 1. Descripción
Este proyecto consiste en un pipeline automatizado para la gestión de datos de calidad de café. El flujo abarca desde la descarga de datos crudos hasta la preparación para su carga en bases de datos relacionales.

## 2. Estructura del Proyecto
- `scripts/ingesta.py`: Descarga los datos desde la fuente original.
- `scripts/validacion.py`: Limpia y filtra los datos (Actividad 2.3.2).
- `data/raw/`: Almacena los archivos CSV originales con sello de fecha.
- `data/processed/`: Contiene los datos limpios listos para usar.
- `data/reports/`: Logs de errores y trazabilidad del proceso.

## 3. Proceso de Ingesta
El script de ingesta conecta con un repositorio de GitHub para extraer un dataset de "Coffee Ratings". 
- **Trazabilidad**: Los archivos se guardan como `ingesta_YYYY-MM-DD.csv` para evitar pérdidas de datos.
- **Robustez**: Incluye manejo de excepciones para evitar caídas si falla la conexión.

## 4. Validación y Carga (Actividad 2.4.2)
Siguiendo los requisitos de la guía técnica:
- Se eliminan nulos y duplicados.
- Se valida que los puntajes de cata estén en el rango lógico (0-100).
- Se prepara la información para la carga en base de datos, asegurando la integridad de los tipos de datos.

## 5. Requisitos
- Python 3.x
- Librerías: `requests`, `pandas`

```bash
pip install requests pandas
