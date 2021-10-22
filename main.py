from discord.ext import commands
import live
from tabelas import brasileirao
from tabelas import bundesliga
from tabelas import calcio
from tabelas import la_liga
from tabelas import liga_NOS
from tabelas import ligue_1
from tabelas import premierleague
from decouple import config

# Prefixo utilizado

bot = commands.Bot ('!')

## Mensagem de confirmação do bot

@bot.event
async def on_ready():
    print (f'Estou pronto e conectado como {bot.user}')

## Comandos para o envio das tabelas das principais competições do mundo

@bot.command (name='brasileirao')
async def send_tabela(ctx):
    name = ctx.author.name

    response = '🇧🇷 Brasileirão Table 🇧🇷 ' + '\n' + brasileirao.tabela

    await ctx.send (response)

@bot.command (name='bundesliga')
async def send_tabela(ctx):
    name = ctx.author.name

    response = ':flag_de: Bundesliga Table :flag_de:  ' + '\n' + bundesliga.tabela

    await ctx.send (response)

@bot.command (name='serie-a')
async def send_tabela(ctx):
    name = ctx.author.name

    response = '🇮🇹 Serie A Table 🇮🇹 ' + '\n' + calcio.tabela

    await ctx.send (response)

@bot.command (name='la-liga')
async def send_tabela(ctx):
    name = ctx.author.name

    response = '🇪🇸 La Liga Table 🇪🇸 ' + '\n' + la_liga.tabela

    await ctx.send (response)

@bot.command (name='liga-nos')
async def send_tabela(ctx):
    name = ctx.author.name

    response = '🇵🇹 Liga NOS Table 🇵🇹 ' + '\n' + liga_NOS.tabela

    await ctx.send (response)

@bot.command (name='ligue-1')
async def send_tabela(ctx):
    name = ctx.author.name

    response = '🇫🇷 Ligue 1 Table 🇫🇷 ' + '\n' + ligue_1.tabela

    await ctx.send (response)

@bot.command (name='premier-league')
async def send_tabela(ctx):
    name = ctx.author.name

    response = '🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League Table 🏴󠁧󠁢󠁥󠁮󠁧󠁿 ' + '\n' + premierleague.tabela

    await ctx.send (response)

## Comando para o envio dos jogos ao vivo

@bot.command (name='live')
async def send_ao_vivo(ctx):
    name = ctx.author.name

    response = ':anger: Live Games :anger: ' + '\n' + live.jogos_ao_vivo

    await ctx.send (response)





## Token para a conexão do bot (utilizar .env para escondê-lo)

TOKEN = config ('TOKEN_DISCORD')
bot.run(TOKEN)
