import discord
from discord.ext import commands
import scraping

bot = commands.Bot ('!')

@bot.event
async def on_ready():
    print (f'Estou pronto e conectado como {bot.user}')

@bot.event
async def on_message (message):
    if message.author == bot.user:
        return

    if 'série b' in message.content:
        await message.channel.send (f'Por favor {message.author.name} pare, os cruzeirenses, vascaínos e botafoguenses deste Discord já sofrem demais!')

    await bot.process_commands(message)


@bot.command (name='tabela')
async def send_vasco(ctx):
    name = ctx.author.name

    response = scraping.tabela

    await ctx.send (response)


bot.run('TOKEN')
