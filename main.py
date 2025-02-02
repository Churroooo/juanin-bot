import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

description = '''An example bot to showcase the discord.ext.commands extension
module.'''


bot = commands.Bot(command_prefix='?', description=description, intents=intents)
client = discord.Client(intents=intents)

TOKEN = "MTMzMzA5Mzg3MTkwMjc4NTU3Nw.G1bsSt.wWn3YMN1u-CbLKyVpES_dGEGLsClIMPYn5rUqo"

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


client.run(TOKEN)