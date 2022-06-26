from discord.ext import commands
from google.cloud import datastore


class Raid(commands.Cog):
    """Raid Cog"""

    def __init__(self, client):
        # sets client variable so it can be used in cog
        self.client = client
        self.db_client = datastore.Client()

    @commands.command()
    async def query(self, ctx):
        query = self.db_client.query(kind="Member")
        results = list(query.fetch())
        await ctx.send(results)


def setup(client):
    client.add_cog(Raid(client))
