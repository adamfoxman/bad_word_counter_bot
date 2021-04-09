from discord.ext import commands
from counter import Counter

class ChannelCounter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.counter = Counter

    @commands.command(name='przelicztutaj')
    async def count_here(self, ctx, *args):
        for message in ctx.channel.history(limit=100000):
            message.