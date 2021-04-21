import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from counter import Counter
from database import Database

load_dotenv()
token = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='kur!', description='Bot liczący wulgarność studentów PB', intents=intents)
database: Database = Database("database.json")
bot.load_extension('ChannelCounter')

@bot.event
async def on_ready():
    print("I'm ready to go!")
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name= 'people swearing'))


bot.run(token)
