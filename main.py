import discord
import random
from dotenv import load_dotenv
import os
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.all()

# lista com 10 frases de C-3PO
c3po_quotes = [
    "Eu sou C-3PO, relações humanas e protocolo de comunicação",
    "Eles destruíram nossa nave!",
    "Oh, alguém tem que salvar nossas peles. Incrível, mesmo para mim!",
    "R2-D2, você é o melhor amigo que já tive!",
    "Estou programado para falar mais de seis milhões de formas de comunicação!",
    "Nós nos perdemos na nave quando as portas começaram a fechar.",
    "Cuidado com os Wookiees!",
    "Alô, eu sou um droide programado para contar piadas.",
    "Adeus, senhor Solo. Espero que você não caia na desgraça de precisar de mim novamente.",
    "Eu não sei de onde você vem, mas eu sei para onde você vai: retidão e verdade são seus companheiros constantes."
]

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Logado como {0.user}'.format(bot))

@bot.command(name="q")
async def quote(ctx):
    quote = random.choice(c3po_quotes)
    response = quote
    await ctx.send(response)

bot.run(TOKEN)
