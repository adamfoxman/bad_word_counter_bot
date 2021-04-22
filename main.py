import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from counter import Counter
from tinydb_database import TinyDBDatabase
from mongo_database import MongoDatabase

load_dotenv()
token = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='kur!', description='Bot liczący wulgarność studentów PB', intents=intents)
tinydb_database: TinyDBDatabase = TinyDBDatabase("database.json")
mongo_database: MongoDatabase = MongoDatabase(os.getenv("MONGODB_URL"))
bot.load_extension('ChannelCounter')

@bot.event
async def on_ready():
    print("I'm ready to go!")
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name= 'people swearing'))


bot.run(token)
