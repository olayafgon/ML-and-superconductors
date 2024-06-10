# ARCHIVO DE CONFIGURACIÓN DEL PROYECTO

# GENERAL
RESULTS_FOLDER = r'.\..\results' # Ruta relativa a la carpeta donde se guardan los resultados y logs

# DESCARGA DE DATOS DE AFLOWLIB
# True si se quieren descargar los datos, False si ya están descargados (deberán estar en DATA_FOLDER_PATH)
DATA_DOWNLOAD = False 
# True si se quieren leer los datos de data_raw y guardarlos en csv, False si quieres leer los guardados en data
READ_DATA_RAW = False 
# Velocidad límite de descompresión
SPEED_LIMIT = 2 * 500 * 1024 * 1024 # 2*500Mb/s
# Rutas a los datos
DATA_FOLDER_PATH = r'.\..\data' 
DOS_CSV_PATH = r'.\..\data\dos_data.csv'
SUPERCON_CSV_PATH = r'.\..\data\3DSC\3DSC_ICSD_only_IDs.csv'
# Redes de Bravais sobre las que se desea trabajar
STRUCTURES = ["BCC", "BCT", "CUB", "FCC", "HEX", "MCL", "MCLC", "ORC", "ORCC", "ORCF", "ORCI", "RHL", "TET", "TRI"] 
# Tipo de archivo en Aflowlib ('DOSCAR.static.xz' o '_dosdata.json.xz')
DATA_FILE_TYPE = '_dosdata.json.xz'
# Limites de energía respecto a Fermi en la lectura
EFERMI_LIMIT = 15
EFERMI_GRID_POINTS = 1999 # Esto funciona para limite en 15, recalcular para otros limites


## Test
PATH_TEST_FIGURES = r'.\..\results\test' 