from discord import Message
from discord.ext import commands
from counter import Counter
from main import mongo_database
from tqdm.asyncio import tqdm


class ChannelCounter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.counter = Counter

    @commands.command(name='setup')
    async def add_users(self, ctx):
        # try:
        #     mongo_database.drop_server_table(ctx.guild.id)
        # except:
        #     await ctx.send("Failed dropping this server's user table.")
        # else:
        await ctx.send("Fetching all users...")
        async for member in ctx.guild.fetch_members(limit=None):
            mongo_database.add_user(guild=ctx.guild.id, author_id=member.id)
            mongo_database.set_user_nick(guild=ctx.guild.id, author_id=member.id, author_nick=member.name)
        await ctx.send("Done!")

    def get_message_stats(self, guild: str, message: Message):
        content = message.content
        k, j, p, ch, g, sz, xd = Counter.count_swearings(self.counter, message=content)
        if k | j | p | ch | g | sz | xd:
            mongo_database.add_stats_to_user(guild=guild, author_id=message.author.id, k=k, j=j, p=p, ch=ch,
                                             g=g, sz=sz, xd=xd)

    @commands.command(name='count')
    async def count_here(self, ctx):
        msg_amount: int = 0;
        await ctx.send("Starting counting...")
        for channel in ctx.guild.text_channels:
            print("Now in " + channel.name)
            await ctx.send("Now in " + channel.name + ". Messages processed to this moment: " + str(msg_amount),
                           delete_after=5.0)
            async for message in tqdm(channel.history(limit=None)):
                self.get_message_stats(ctx.guild.id, message)
                msg_amount = msg_amount + 1
        await ctx.send("I'm done! Messages processed: " + str(msg_amount))


def setup(bot):
    bot.add_cog(ChannelCounter(bot))
