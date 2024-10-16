import discord
from discord.ext.commands import Bot

# Cria a instância de 'client' do bot.
CLIENT = Bot(command_prefix=">>!", intents=discord.Intents.all())

# A lista de Cogs no seu projeto.
EXTENTION_LIST = [
    'helloworld'
]

BOT_NAME = 'YourBotName'
