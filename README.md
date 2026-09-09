# Automatizaciones de Big Data Deportivo

Colección de automatizaciones y patrones de código para trabajar con datos de fútbol.

## Contenido

`automatizaciones/catalogo_automatizaciones.py` reúne las tareas automatizadas desarrolladas para el manual:

- Descarga y extracción de datos de partidos.
- Lectura de tablas HTML y concatenación de temporadas.
- Limpieza de porcentajes, guiones, columnas numéricas y duplicados.
- Validación de esquemas y control de archivos vacíos.
- Creación de métricas por 90 y porcentajes de participación.
- Descarga de eventos de StatsBomb.
- Separación de coordenadas espaciales.
- Mapas de tiros, pases, calor y redes de pase.
- Exploración de clustering.

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
