import json, os
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from utilities.configreader import ConfigReader


class DataBase:
    file_name = 'db-dev.json' if ConfigReader.get_config else 'db-prod.json'
    db_file = os.path.join(os.path.dirname(__file__), file_name)

    with open(db_file, 'r') as dbConfig:
        serviceAccountKey, databaseOptions = json.load(dbConfig)

    try:
        appCredential = credentials.Certificate(serviceAccountKey)
        defaultApp = firebase_admin.initialize_app(
            credential=appCredential,
            options=databaseOptions
        )
        print(f"\033[32mSUCESSFUL: Sucesso ao conectar no banco de dados.")
    except ValueError as e:
        print(f"\033[31mERROR: Erro ao conectar ao banco de dados: {e}")

    dbRef = db.reference(f"/")

