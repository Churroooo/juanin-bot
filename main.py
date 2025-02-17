import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

description = '''An example bot to showcase the discord.ext.commands extension
module.'''


bot = commands.Bot(command_prefix='!', description=description, intents=intents)
client = discord.Client(intents=intents)

TOKEN = "MTMzMzA5Mzg3MTkwMjc4NTU3Nw.G8M5QX.1vAst8PHG5YOSF2PuRDKxOPXpw7BgJUme0ku9Q"

@client.event
async def on_ready():
    print(f"bot conectado como {client.user}")

@bot.command()
async def ayuda(ctx):
    await ctx.send(f"¡Hola! soy un bot creado por un chavo que estudia python y fui uno de sus proyectos mejor ejecutados. Puedo darte consejos para ser más sustentable en tu vida diaria, o simplemente charlar contigo. ¡Pregúntame lo que quieras! COMANDOS: !hola: saludo---!adios: despedida---!como_estas: pregunta como estoy---!consejo: te doy un consejo aleatorio sobre como ser más sustentable---!consejo1: te doy un seguimiento sobre el consejo 1, vienen enumerados así del 1 al 5.---!ping: te dirá tu latencia actual! Más comandos en camino...!")

@bot.command()
async def consejo(ctx):
    consejos = ['intentemos generar y plantar más arboles para nuestro futuro y el de siguientes generaciones.(consejo numero 1)', 'Pon en tu vida diaria la regla de las 3 R: Reducir, Reutilizar y Reciclar. (consejo numero 2)', 'No tires basura en la calle, no seas maleducado.(consejo numero 3)', 'No uses plásticos de un solo uso, usa bolsas de tela o de papel.(consejo numero 4)', "intenta ser un poco más ligero con tu uso de agua, no necesitas durar 30 minutos.(consejo numero 5)"]
    consejo_aleatorio = random.choice(consejos)
    await ctx.send(f'este te ayuda?: (usa el comando !consejo y el numero de el consejo si quieres seguimiento. EJ. "!consejo4) \n{consejo_aleatorio}')

@bot.command()
async def consejo1(ctx):
    await ctx.send(f'la granada, así como la maracuyá tiene maximo 1400 semillas por fruto, y cada semilla puede ser plantada para hacer un nuevo arbol de granada. ¡no desperdicies la oportunidad de plantar una de estas frutas y tener una fuente sustentable de comida y oxigeno!')

@bot.command()
async def consejo2(ctx):
    await ctx.send(f'Las 3 R son una regla de oro para la conservación del medio ambiente, si reducimos la cantidad de basura que generamos, reutilizamos lo que podamos y reciclamos lo que no, podemos hacer una gran diferencia en el mundo.')
    
@bot.command()
async def consejo3(ctx):
    await ctx.send(f'la basura en la calle no solo es antiestético, sino que también es peligroso para la vida silvestre y puede causar inundaciones. ¡no seas maleducado y tira tu basura en un bote, nada te cuesta!')

@bot.command()
async def consejo4(ctx):
    await ctx.send(f'los plásticos de un solo uso son una de las mayores fuentes de contaminación en el mundo, si usas bolsas de tela o de papel, puedes ayudar a reducir la cantidad de basura que generamos. ¡cada pequeño cambio cuenta!')

@bot.command()
async def consejo5(ctx):
    await ctx.send(f'el agua es un recurso limitado, si usas menos agua en tu vida diaria, puedes ayudar a conservar este recurso para futuras generaciones. ¡no necesitas durar 30 minutos en la ducha, seamos conscientes de nuestro uso de agua!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
@bot.command()
async def hola(ctx):
    await ctx.send(f"hola {ctx.author.mention}, ¿cómo estás?")

@bot.command(name="como_estas")
async def como_estas(ctx):
    await ctx.send(f"yo increíble. y tu, {ctx.author.mention}, ¿cómo estás?")

@bot.command()
async def joined(ctx, member: discord.Member):
    """dioss, alguien nuevo. ey, no sean penosos, ¡saluden! pero... ¿nos trajiste algo?"""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def meme(ctx):
    img_meme = random.choice(os.listdir("img"))
    with open(f"img/{img_meme}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture) #no he logrado que este comando funcione. si tú puedes lograrlo, hazmelo saber a mi github!

@bot.command()
async def ping(ctx):
    await ctx.send(f"🌿 Pong! Latencia: {round(bot.latency * 1000)}ms")

@bot.command()
async def adios(ctx):
    await ctx.send(f"luego nos vemos {ctx.author.mention}, cuídate!!")


bot.run(TOKEN)
