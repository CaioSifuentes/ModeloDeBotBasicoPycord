import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from client import CLIENT, EXTENTION_LIST, BOT_NAME

# from database.database import DataBase
from utilities.configreader import ConfigReader

# Define se estamos em produção ou desenvolvimento.
ConfigReader.set_mode(dev_mode=True)

# Carrega todas as funções dentro de app.
for EXTENTION in EXTENTION_LIST:
    CLIENT.load_extension("app." + EXTENTION)
    
@CLIENT.event
async def on_ready():
    mensagemInicial = f"SUCESSFUL: {BOT_NAME} DevBot is Online!"
    print(f'\033[32m{mensagemInicial:^15}')
    print('\033[33m=\033[m' * 50)

# Conecta ao banco de dados
# db = DataBase()

# Excecuta o bot.
CLIENT.run(ConfigReader.get_token())
