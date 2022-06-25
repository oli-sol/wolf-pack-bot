"""
Adds cog to bot
"""
import discord
from discord.ext import commands


class ZephyrCog(commands.Cog):
    """Zephyr Cog"""
    def __init__(self, bot):
        """Initiates bot"""
        self.bot = bot
        self._last_member = None


    @commands.command()
    async def list_raiders(self, ctx, role: discord.Role):
        """Lists all members with this discord Role"""
        for member in role.members:
            await ctx.send(f'{member.display_name} - {member.id}')

    @commands.command()
    async def weekly_ping(self, ctx, role: discord.Role):
        """Ping all Raiders within given discord Role"""
        my_msg = ('Woof! It\'s another week. Respond with a thumbs up or down if you can raid this week:\n')
        for member in role.members:
            my_msg += (f'{member.mention}')
        msg = await ctx.send(my_msg)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")

    @commands.command()
    async def participation_ping(self, ctx, role: discord.Role, custom_msg):
        """Pings with custom message to poll for participation in a given activity"""
        for member in role.members:
            custom_msg += (f'{member.mention}')
        msg = await ctx.send(custom_msg + ". Respond thumbs up if you can make it.")
        await msg.add_reaction("👍")

    @list_raiders.error
    async def role_error(self, ctx, error):
        if isinstance(error, commands.RoleNotFound):
            await ctx.send("Invalid syntax. \nUse:     !list_raiders <role>")
    @weekly_ping.error
    async def role_error(self, ctx, error):
        if isinstance(error, commands.RoleNotFound):
            await ctx.send("Invalid syntax. \nUse:     !weekly_ping <role>")

def setup(bot):
    """Adds cog"""
    bot.add_cog(ZephyrCog(bot))
