# Pipeline de Ingesta de Datos - Proyecto Final

## 1. Descripción del Proyecto
Este proyecto implementa la primera fase funcional de un pipeline de datos: la **Ingesta Automatizada**. El objetivo es extraer datos desde una fuente de origen (en este caso, un dataset estructurado en formato CSV) y almacenarlos de forma organizada en una arquitectura local siguiendo buenas prácticas de ingeniería de datos.

## 2. Arquitectura de Directorios
El proyecto sigue una estructura modular para garantizar el orden y la trazabilidad:

- `scripts/`: Contiene el motor lógico del pipeline (`ingesta.py`).
- `data/`: Directorio raíz para el almacenamiento de información (ignorado por Git).
  - `raw/`: Zona de aterrizaje (**Landing Zone**) para los datos crudos, sin procesar.
- `config/`: Archivos de configuración y rutas.
- `requirements.txt`: Listado de librerías necesarias para la ejecución.

## 3. Flujo de Ingesta (Paso a Paso)
El script de ingesta realiza las siguientes acciones de forma lineal:
1. **Verificación de Entorno**: Comprueba la existencia de las carpetas de destino y las crea si es necesario.
2. **Extracción (Extract)**: Conecta con la fuente de origen mediante protocolos HTTP (librería `requests`).
3. **Control de Errores**: Valida que la respuesta sea exitosa (Status 200) antes de escribir en disco.
4. **Almacenamiento con Trazabilidad**: Guarda el archivo en la carpeta `data/raw/` añadiendo un sello de fecha (`YYYY-MM-DD`) al nombre del archivo para mantener un historial de cargas.

## 4. Requisitos e Instalación
Para que este pipeline sea **reproducible**, es necesario contar con Python 3.x e instalar las dependencias:

```bash
RECUERDE TIRAR ESTE COMANDO EN EL TERMINAL PRIMERO
pip install requests
