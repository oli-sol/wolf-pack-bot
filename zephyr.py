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
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member

    @commands.command()
    async def list_raiders(self, ctx, role: discord.Role):
        """Lists all members with this discord Role"""
        for member in role.members:
            await ctx.send(f'{member.display_name} - {member.id}')

    @list_raiders.error
    async def role_error(self, ctx, error):
        if isinstance(error, commands.RoleNotFound):
            await ctx.send("Invalid syntax. \nUse:     !list_raiders <role>")


def setup(bot):
    """Adds cog"""
    bot.add_cog(ZephyrCog(bot))
