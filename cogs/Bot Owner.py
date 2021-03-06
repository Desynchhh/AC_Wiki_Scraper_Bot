import discord
from discord.ext import commands

from helpers.checks import is_bot_owner
from scraper_v2 import run_scraper

import time

class BotOwner(commands.Cog):
    def __init__(self, bot:discord.ext.commands.Bot):
        self.bot = bot

    
    @commands.command()
    @commands.check(is_bot_owner)
    async def gettotalservers(self, ctx:discord.ext.commands.Context):
        await ctx.send(f"I am currently in {len(self.bot.guilds)} servers!")
    

    @commands.command()
    @commands.check(is_bot_owner)
    async def getservers(self, ctx:discord.ext.commands.Context):
        await ctx.send([server.name for server in self.bot.guilds])


    @commands.command()
    @commands.check(is_bot_owner)
    async def updatejson(self, ctx:discord.ext.commands.Context):
        """Forcefully runs scrapers, updating the local critter data.

        :type ctx: discord.ext.commands.Context"""
        t1 = time.time()
        async with ctx.typing():
            await run_scraper()
        await ctx.send(f'Updated JSON data in {round(time.time()-t1, 2)} seconds.')
    

    @commands.command()
    @commands.check(is_bot_owner)
    async def reloadcogs(self, ctx:discord.ext.commands.Context):
        """Reloads all cogs used by the bot in case of live changes.

        :type ctx: discord.ext.commands.Context"""
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                self.bot.reload_extension(f'cogs.{filename[:-3]}')
        await ctx.send('Reloaded cogs!')


def setup(bot:discord.ext.commands.Bot):
    bot.add_cog(BotOwner(bot))
