import discord
from discord.ext import commands

TOKEN = 'MTE1MTA2NzQ4NDUxNDk2MzQ4OA.GG6Skd.VThO0LL_fHMlsVZLVC8nV9GLQpepE3c52VTY1c'  # Пожалуйста, смените свой токен!

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='привет')
async def greet(ctx):
    await ctx.send(f'Привет, {ctx.author.mention}!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

bot.run(TOKEN)