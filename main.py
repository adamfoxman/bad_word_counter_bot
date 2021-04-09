import discord
from discord.ext import commands
from counter import Counter

bot = commands.Bot(command_prefix='kurwa!', description='Bot liczący wulgarność studentów PB')

@bot.event()
async def on_ready():
    print("I'm ready to go!")
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name= 'people swearing'))

bot.run('ODI4MDMwNzY0NjU3ODAzMjg0.YGjpvg.Gxy_gLugFNlBMJA38zIIgDCvNTo')
