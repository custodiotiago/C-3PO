import discord
import random

TOKEN = 'seu_token_de_autenticacao'

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

bot = discord.Client()

@bot.event
async def on_ready():
    print('Logado como {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.content.startswith('!quote'):
        quote = random.choice(c3po_quotes)
        response = f'"{quote}"'
        await message.channel.send(response)

bot.run(TOKEN)
