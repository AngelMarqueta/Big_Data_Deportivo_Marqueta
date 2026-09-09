# Automatizaciones de Big Data Deportivo

Colección de automatizaciones y patrones de código para trabajar con datos de fútbol.

## Contenido

Cada automatización tiene ahora su propio archivo `.py`, organizado en `modulo_1`, `modulo_2` y `modulo_3`. El archivo `automatizaciones/catalogo_automatizaciones.py` se conserva como índice de referencia.

Las tareas cubren:

- Descarga y extracción de datos de partidos.
- Lectura de tablas HTML y concatenación de temporadas.
- Limpieza de porcentajes, guiones, columnas numéricas y duplicados.
- Validación de esquemas y control de archivos vacíos.
- Creación de métricas por 90 y porcentajes de participación.
- Descarga de eventos de StatsBomb.
- Separación de coordenadas espaciales.
- Mapas de tiros, pases, calor y redes de pase.
- Exploración de clustering.

Hay 23 automatizaciones independientes. Los nombres de archivo empiezan por un número para facilitar su consulta y mantener el orden del material.

El archivo es un catálogo de funciones y ejemplos. Algunas funciones esperan que el programa principal defina objetos como `pandas.DataFrame`, `eventos` o `pases`.

## Instalación

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Uso responsable

- Comprueba los términos de uso, robots.txt y límites de cada proveedor.
- Conserva la fuente, fecha, temporada y versión del dato.
- No guardes tokens, contraseñas ni datos personales en el repositorio.
- Revisa manualmente una muestra antes de publicar métricas o informes.

## Licencia y atribución

El catálogo contiene código educativo y patrones reutilizables. Los datos descargados de terceros mantienen la licencia y las condiciones de atribución de su proveedor.
