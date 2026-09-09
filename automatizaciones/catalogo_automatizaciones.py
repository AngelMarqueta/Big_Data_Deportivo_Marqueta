AUTOMATIONS = {
    "Módulo 1": [
        ("Limpieza automática de Basketball Reference", "Lee un CSV, conserva los nulos como datos ausentes y normaliza nombre y posición sin depender de variables externas.", """import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df['Player'] = df['Player'].astype('string').str.split('\\\\').str[0]
    df['Pos'] = df['Pos'].astype('string').str.split('-').str[0]
    return df"""),
        ("Detección y conversión de porcentajes", "Localiza por nombre las columnas porcentuales y admite valores con %, guiones y nulos.", """def convertir_porcentajes(df):
    df = df.copy()
    cols_pct = [col for col in df.columns if '%' in col]
    for col in cols_pct:
        texto = df[col].astype('string').str.replace('%', '', regex=False)
        df[col] = pd.to_numeric(texto.replace('-', pd.NA), errors='coerce') / 100
    return df"""),
        ("Limpieza completa de datos InStat", "Automatiza sustitución de guiones, porcentajes y columnas numéricas. Corrige el original: se itera sobre df.columns, no sobre la variable global jug_2b.", """def clean_data_instat(df, columnas_categoricas=None):
    df = df.copy().replace('-', pd.NA)
    columnas_categoricas = columnas_categoricas or [
        'Nombre', 'Posición', 'Equipo', 'Pierna',
        'Nacionalidad', 'Selección nacional'
    ]
    cols_pct = [col for col in df.columns if '%' in col]
    for col in cols_pct:
        df[col] = (pd.to_numeric(
            df[col].astype('string').str.replace('%', '', regex=False),
            errors='coerce') / 100)
    cols_num = [col for col in df.columns if col not in columnas_categoricas]
    for col in cols_num:
        if col not in cols_pct:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df"""),
    ],
    "Módulo 2": [
        ("Aplicar una función a varias columnas", "Encapsula la conversión de columnas y permite reutilizarla en nuevos conjuntos de datos.", """def convertir_columnas(df, columnas):
    df = df.copy()
    for col in columnas:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df"""),
        ("Función principal con funciones auxiliares", "Divide un proceso grande en lectura, limpieza y validación para poder probar cada parte.", """def preparar_datos(ruta):
    def leer(ruta_archivo):
        return pd.read_csv(ruta_archivo)
    def limpiar(df):
        return df.drop_duplicates().rename(columns=lambda c: c.strip())
    df = limpiar(leer(ruta))
    if df.empty:
        raise ValueError('El archivo no contiene registros')
    return df"""),
        ("Extraer una tabla de FBref", "Lee tablas HTML y selecciona la que contiene las columnas esperadas en lugar de asumir una posición fija.", """def extraer_tabla_fbref(url, columnas_obligatorias=('Player',)):
    tablas = pd.read_html(url)
    for tabla in tablas:
        tabla.columns = [c[-1] if isinstance(c, tuple) else c for c in tabla.columns]
        if set(columnas_obligatorias).issubset(tabla.columns):
            return tabla
    raise ValueError('No se encontró la tabla esperada')"""),
        ("Extraer varias páginas y concatenarlas", "Recorre URLs de equipos o temporadas, añade trazabilidad y concatena solo resultados compatibles.", """def extraer_temporadas(urls_por_temporada):
    partes = []
    for temporada, url in urls_por_temporada.items():
        tabla = extraer_tabla_fbref(url)
        tabla['temporada'] = temporada
        partes.append(tabla)
    if not partes:
        return pd.DataFrame()
    return pd.concat(partes, ignore_index=True, sort=False)"""),
        ("Basketball Reference por equipo y año", "Parametriza año y equipo y evita repetir manualmente la extracción.", """def basketball_equipo(equipo, anio):
    url = f'https://www.basketball-reference.com/teams/{equipo}/{anio}.html'
    tablas = pd.read_html(url)
    candidatas = [t for t in tablas if 'Player' in t.columns]
    if not candidatas:
        raise ValueError(f'Sin tabla de jugadores para {equipo} {anio}')
    return candidatas[0].assign(equipo=equipo, temporada=anio)"""),
        ("Basketball Reference para varias temporadas", "Automatiza el histórico y mantiene las claves de temporada y equipo.", """def basketball_historico(equipo, anios):
    datos = [basketball_equipo(equipo, anio) for anio in anios]
    return pd.concat(datos, ignore_index=True, sort=False)"""),
        ("Gráfico de barras reutilizable", "Devuelve figura y eje para que el llamador pueda guardar, anotar o combinar el gráfico.", """import matplotlib.pyplot as plt

def grafico_barras(df, categoria, valor, titulo):
    resumen = df.groupby(categoria, as_index=False)[valor].sum()
    resumen = resumen.sort_values(valor, ascending=False)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(resumen[categoria], resumen[valor], color='#1f77b4')
    ax.set(title=titulo, xlabel=categoria, ylabel=valor)
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    return fig, ax"""),
        ("Gráfico de dispersión reutilizable", "Representa la relación entre dos métricas y permite codificar una categoría deportiva.", """import seaborn as sns

def grafico_scatter(df, x, y, grupo=None, titulo=''):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x=x, y=y, hue=grupo, ax=ax)
    ax.set_title(titulo)
    fig.tight_layout()
    return fig, ax"""),
        ("Dispersión tridimensional", "Reproduce la automatización 3D del curso; conviene usarla para exploración, no para comparaciones exactas.", """def grafico_3d(df, x, y, z, color='#1f77b4'):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df[x], df[y], df[z], c=color, alpha=.7)
    ax.set(xlabel=x, ylabel=y, zlabel=z)
    return fig, ax"""),
        ("Crear e importar una librería propia", "Guarda las funciones estables en un módulo y reutilízalas con una importación normal.", """# archivo graficas_deportivas.py
def tasa_por_90(valor, minutos):
    return 0 if minutos == 0 else valor / minutos * 90

# cuaderno o programa principal
from graficas_deportivas import tasa_por_90
xg_90 = tasa_por_90(valor=4.2, minutos=900)"""),
        ("Porcentaje de participación", "Calcula automáticamente la parte del total del equipo aportada por cada jugador y protege la división entre cero.", """def porcentaje_participacion(df, valor, grupo='Equipo'):
    df = df.copy()
    total = df.groupby(grupo)[valor].transform('sum')
    df[f'pct_{valor}'] = df[valor].div(total.where(total.ne(0)))
    return df"""),
        ("Creación automática de nuevas columnas", "Recibe fórmulas como funciones para crear métricas reproducibles sin repetir asignaciones.", """def crear_metricas(df):
    df = df.copy()
    minutos_validos = df['Minutos'].where(df['Minutos'].gt(0))
    df['Goles_90'] = df['Goles'].div(minutos_validos).mul(90)
    df['Asistencias_90'] = df['Asistencias'].div(minutos_validos).mul(90)
    df['Contribuciones_90'] = df['Goles_90'] + df['Asistencias_90']
    return df"""),
    ],
    "Módulo 3": [
        ("Competición, temporada y partidos de StatsBomb", "Encadena los identificadores hasta obtener el partido elegido. Corrige el nombre info_jason del material a info_json.", """from statsbombpy import sb

def info_json(competicion, temporada):
    competiciones = sb.competitions()
    fila = competiciones.loc[
        competiciones['competition_name'].eq(competicion)
        & competiciones['season_name'].eq(temporada)
    ]
    if fila.empty:
        raise ValueError('Competición o temporada inexistente')
    return sb.matches(
        competition_id=int(fila.iloc[0]['competition_id']),
        season_id=int(fila.iloc[0]['season_id']))"""),
        ("Descarga automática de eventos", "Obtiene los eventos de un partido mediante su match_id y conserva el identificador en la salida.", """def event_data(match_id):
    eventos = sb.events(match_id=match_id)
    if eventos.empty:
        raise ValueError(f'El partido {match_id} no contiene eventos')
    eventos['match_id'] = match_id
    return eventos"""),
        ("Separar coordenadas de eventos", "Extrae x e y con seguridad cuando location está ausente o incompleto.", """def coordinates(df, columna='location'):
    df = df.copy()
    coords = df[columna].apply(
        lambda p: p if isinstance(p, (list, tuple)) and len(p) >= 2 else [pd.NA, pd.NA]
    )
    df[['x', 'y']] = pd.DataFrame(coords.tolist(), index=df.index)
    return df"""),
        ("Mapa automático de tiros", "Filtra tiros, escala su tamaño por xG y diferencia el resultado.", """def mapa_tiros(eventos, equipo):
    tiros = coordinates(eventos.query("type == 'Shot' and team == @equipo"))
    fig, ax = plt.subplots(figsize=(9, 6))
    colores = tiros['shot_outcome'].eq('Goal').map({True: '#e63946', False: '#457b9d'})
    ax.scatter(tiros['x'], tiros['y'], s=40 + 500 * tiros['shot_statsbomb_xg'],
               c=colores, alpha=.75, edgecolor='white')
    ax.set(title=f'Mapa de tiros · {equipo}', xlim=(0, 120), ylim=(80, 0), aspect='equal')
    return fig, ax"""),
        ("Flechas de pases", "Dibuja origen y destino de cada pase y distingue los incompletos.", """def mapa_pases(eventos, jugador):
    pases = coordinates(eventos.query("type == 'Pass' and player == @jugador"))
    destinos = pases['pass_end_location'].apply(lambda p: p if isinstance(p, list) else [pd.NA, pd.NA])
    pases[['x_fin', 'y_fin']] = pd.DataFrame(destinos.tolist(), index=pases.index)
    fig, ax = plt.subplots(figsize=(9, 6))
    for fila in pases.itertuples():
        ax.annotate('', (fila.x_fin, fila.y_fin), (fila.x, fila.y),
                    arrowprops={'arrowstyle': '->', 'alpha': .45})
    ax.set(xlim=(0, 120), ylim=(80, 0), aspect='equal', title=f'Pases · {jugador}')
    return fig, ax"""),
        ("Mapa de calor de acciones", "Automatiza la densidad espacial con una malla constante para permitir comparaciones.", """def mapa_calor(eventos, equipo, bins=(12, 8)):
    acciones = coordinates(eventos.query('team == @equipo')).dropna(subset=['x', 'y'])
    fig, ax = plt.subplots(figsize=(9, 6))
    mapa = ax.hist2d(acciones['x'], acciones['y'], bins=bins,
                    range=((0, 120), (0, 80)), cmap='magma')
    fig.colorbar(mapa[3], ax=ax, label='Acciones')
    ax.set(title=f'Densidad de acciones · {equipo}', ylim=(80, 0), aspect='equal')
    return fig, ax"""),
        ("Matriz o red de pases", "Calcula posiciones medias y conexiones; exige receptor y filtra enlaces débiles.", """def matriz_pases(pases, minimo=3):
    pases = coordinates(pases).dropna(subset=['player', 'pass_recipient', 'x', 'y'])
    nodos = pases.groupby('player', as_index=False).agg(x=('x', 'mean'), y=('y', 'mean'), pases=('id', 'count'))
    enlaces = (pases.groupby(['player', 'pass_recipient']).size()
               .rename('peso').reset_index().query('peso >= @minimo'))
    return nodos, enlaces"""),
        ("Exploración automática de clustering", "Prueba varios valores de k y devuelve inercia y silhouette para apoyar, no sustituir, la decisión analítica.", """from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def explore_cluster(X, valores_k=range(2, 9), random_state=42):
    resultados = []
    for k in valores_k:
        modelo = KMeans(n_clusters=k, n_init=20, random_state=random_state)
        etiquetas = modelo.fit_predict(X)
        resultados.append({'k': k, 'inercia': modelo.inertia_,
                           'silhouette': silhouette_score(X, etiquetas)})
    return pd.DataFrame(resultados)"""),
    ],
}
