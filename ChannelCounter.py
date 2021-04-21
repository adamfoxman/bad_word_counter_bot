from discord.ext import commands
from counter import Counter
from main import database
from tqdm.asyncio import tqdm


class ChannelCounter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.counter = Counter

    @commands.command(name='uzytkownicy')
    async def add_users(self, ctx):
        async for member in ctx.guild.fetch_members(limit=None):
            database.add_user(member.id)
            database.set_user_nick(author_id=member.id, author_nick=member.name)

    @commands.command(name='przelicz')
    async def count_here(self, ctx):
        for channel in ctx.guild.text_channels:
            print("Now in " + channel.name)
            async for message in tqdm(channel.history(limit=100000)):
                content = message.content
                k, j, p, ch, g, sz = Counter.count_swearings(self.counter, message=content)
                if k | j | p | ch | g | sz:
                    database.add_stats_to_user(guild=ctx.guild.id, author_id=message.author.id, k=k, j=j, p=p, ch=ch,
                                               g=g, sz=sz)
        print("I'm done!")


def setup(bot):
    bot.add_cog(ChannelCounter(bot))
