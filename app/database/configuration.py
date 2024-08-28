#datos para la conexion a BD
dataBaseName = "Gestordb"
userName = "root"
userPassword = ""
conectionPort= 3306
server = "localhost"

#creando la conexion
dataBaseConnection = f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{conectionPort}/{dataBaseName}"

print(dataBaseConnection)