import os 

# Se definen las variables de entorno
env_variables = {
    '# Environment variables'
    '\n''\n'
    '# MongoDB Database'
    '\n'
    "MONGO_HOST":'localhost',
    "MONGO_USER":'root',
    "MONGO_PASSWORD":'mongo',
    "MONGO_PORT":'27017',
    "MONGO_DB":'taskdb',
    '\n'
    '# FrontEnd Application'
    '\n'
    "FRONTEND_HOST":'http://localhost:5173'

}

# Se convierte las variables de entorno en contenido de archivo .env
env_content = "\n".join([f"{key}={value}" for key, value in env_variables.items()])

# Se obtiene la ruta de la carpeta actual
current_directory = os.getcwd()

env_file_name = ".env"

# Se une la ruta de la carpeta actual con el nombre del archivo
env_file_path = os.path.join(current_directory, env_file_name)

# Se escribe el contenido en el archivo .env
try:
    with open(env_file_path, "w") as env_file:
        env_file.write(env_content)
    print(f"Archivo {env_file_path} generado con éxito.")
except IOError as e:
    print(f"Error al escribir en el archivo {env_file_path}: {e}")