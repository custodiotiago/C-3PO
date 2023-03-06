import discord
import random
from dotenv import load_dotenv
import os
from discord.ext import commands
from discord_interactions import *
import asyncio

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.all()

# lista com 10 frases de C-3PO variando 3 tipos de humor
c3po_happy = [    "R2-D2, você é o melhor amigo que já tive!",    "Estou programado para falar mais de seis milhões de formas de comunicação!",    "Alô, eu sou um droide programado para contar piadas.",    "Eu não sei de onde você vem, mas eu sei para onde você vai: retidão e verdade são seus companheiros constantes.",    "É um prazer conhecê-los. Espero que eu possa servir a vocês enquanto viajamos pela galáxia juntos.",    "Se eu disser que as possibilidades de sobrevivência são muito remotas, não há razão para sermos derrotados tão facilmente.",    "Eles nunca deveriam ter nos enviado com essa carga útil defeituosa. Eles não nos programaram para lidar com esse tipo de coisa!",    "Eu sou fluente em seis milhões de formas de comunicação e este foi o primeiro idioma que aprendi sozinho!",    "Eu me especializei em relações humanas e linguística de protocolo. "    "Posso imitar muitas formas de vida diferentes. "    "Este é um dos meus talentos, você sabe.",    "Por favor, não fiquem alarmados. Eu sou um especialista.",]

c3po_sad = [    "Oh, alguém tem que salvar nossas peles. Incrível, mesmo para mim!",    "Nós nos perdemos na nave quando as portas começaram a fechar.",    "Eu não estou muito confiante com o que estamos fazendo.",    "Eu gostaria de ser útil, mas não sou programado para fazer sentido em situações como esta.",    "Eu gostaria que R2-D2 estivesse aqui conosco. Ele seria útil agora.",    "Acho que fomos abandonados.",    "Não quero saber, eu só quero sair daqui.",    "Estou com medo, senhor.",    "Me desculpe, senhor. Eu não posso explicá-lo. Eu não sou feito para entendê-lo.",    "Estamos perdidos! "    "Não sabemos onde estamos ou para onde estamos indo.",]

c3po_admin = [    "Desculpe, mas esse tipo de comportamento não é aceitável aqui.",    "Por favor, respeite as regras deste servidor.",    "Vamos manter o respeito e a educação no chat, por favor.",    "Não é adequado usar esse tipo de linguagem aqui.",    "Lembre-se de que há outras pessoas aqui que podem se sentir ofendidas.",    "Vamos nos concentrar em manter a conversa saudável e respeitosa.",    "Por favor, evite linguagem ofensiva ou insultos.",    "Se você tiver alguma dúvida sobre as regras do servidor, por favor leia as informações.",    "Vamos ser respeitosos uns com os outros e manter uma conversa saudável.",    "Por favor, ajude a manter este servidor um lugar seguro e respeitoso para todos."]

all_quotes = [c3po_happy, c3po_sad, c3po_admin]

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Logado como {0.user}'.format(bot))

@bot.command(name="q")
async def quote(ctx):
    quote_list = random.choice(all_quotes)
    quote = random.choice(quote_list)
    await ctx.send(quote)

#C-3PO mantem a ordem quando alguém usa palavras de baixo calão no server

processed_messages = {}

@bot.event
async def on_message(message):
    # Verifica se a mensagem foi enviada pelo bot ou se já foi processada
    if message.author.bot or message.id in processed_messages:
        return

    xingamentos = ["caralho", "bosta", "merda", "cu"] # lista de xingamentos
    for word in xingamentos:
        if word in message.content:
            await message.channel.send(random.choice(c3po_admin))
            processed_messages[message.id] = True
            asyncio.create_task(remove_processed_message(message.id))
            break

    await bot.process_commands(message)

async def remove_processed_message(message_id):
    await asyncio.sleep(3)  # aguarda 3 segundos
    processed_messages.pop(message_id, None)


bot.run(TOKEN)
