from client import client

# from database.DataBase import DataBase
from app.utilities.configreader import ConfigReader

# Carrega todas as funções dentro de app.
extensionList = [
    'function.helloworld'
]
for extension in extensionList:
    client.load_extension("app." + extension + "command")
    
@client.event
async def on_ready():
    mensagemInicial = "SUCESSFUL: Bot de Testes está online." if ConfigReader.get_mode() else "SUCESSFUL: NomeDoBot está online!"
    print(f'\033[32m{mensagemInicial:^15}')
    print('\033[33m=\033[m' * 50)

# Conecta ao banco de dados
# db = DataBase()

# Excecuta o bot.
client.run(ConfigReader.get_token())
