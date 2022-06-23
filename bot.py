import discord 
from discord.ext import commands, tasks

from random import choice
client = commands.Bot(command_prefix='%')
status = ['The Flob', 'Music', 'Bà con trong net']
@client.event
async def on_ready():
  change_status.start()
  print('Bot :ok!')

@client.command(name='Ping',help='Kiểm tra tốc độ mạng')
async def ping(ctx):
  await ctx.reply(f'🏓 Pong! ``{round(client.latency *1000)}ms``')
  
@tasks.loop(seconds=10)
async def change_status():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=choice(status))) 
client.run(TOKEN)
