import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

description = '''An example bot to showcase the discord.ext.commands extension
module.'''


bot = commands.Bot(command_prefix='?', description=description, intents=intents)
client = discord.Client(intents=intents)

TOKEN = "aquí el token!"

@client.event
async def on_ready():
    print(f"bot conectado como {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower() in ["hola", "buenos dias", "hello", "hey", "hi"]:
        await message.channel.send(f"¡holaa, {message.author.name}! ¿como estás?, pero más importante ¿trajiste pizza?")
@bot.command()
async def joined(ctx, member: discord.Member):
    """dioss, alguien nuevo. ey, no sean penosos, ¡saluden! pero... ¿nos trajiste algo?"""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
    
@bot.command()
async def adios(ctx):
    await ctx.send(f"luego nos vemos {ctx.author.mention}, cuídate!!")

@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! Latencia: {round(bot.latency * 1000)}ms")

client.run(TOKEN)
