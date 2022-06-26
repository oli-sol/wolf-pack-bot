import discord
from discord.ext import commands
from google.cloud import datastore


class Raid(commands.Cog):
    """Raid Cog"""

    def __init__(self, client):
        # sets client variable so it can be used in cog
        self.client = client
        self.db_client = datastore.Client()

    @commands.command()
    async def bis(self, ctx, role: discord.Role, cmd, item="None"):
        if cmd.lower() == "needed":
            # fetch all entities from DB for a specific role name/kind/table
            query = self.db_client.query(kind=role.name)
            results = list(query.fetch())

            # create dict to store response data
            needed = {}

            # loop through each member, add item to list if missing
            for member in results:
                needed[member["Name"]] = ""

                if not member["Weapon"]:
                    needed[member["Name"]] += "Weapon, "
                if not member["Head"]:
                    needed[member["Name"]] += "Head, "
                if not member["Chest"]:
                    needed[member["Name"]] += "Chest, "
                if not member["Hands"]:
                    needed[member["Name"]] += "Hands, "
                if not member["Legs"]:
                    needed[member["Name"]] += "Legs, "
                if not member["Feet"]:
                    needed[member["Name"]] += "Feet, "
                if not member["Earring"]:
                    needed[member["Name"]] += "Earring, "
                if not member["Necklace"]:
                    needed[member["Name"]] += "Necklace, "
                if not member["Bracelet"]:
                    needed[member["Name"]] += "Bracelet, "
                if not member["Ring"]:
                    needed[member["Name"]] += "Ring, "

                # cleanup string to remove comma and space at end
                needed[member["Name"]] = needed[member["Name"]][:-2]

            # if dict isn't empty, send
            if needed:
                await ctx.send("The following items are still needed for BiS! *wags tail*\n\n")

                # construct response string, send
                for key, value in needed.items():
                    response = key + ": " + value
                    await ctx.send(response)


def setup(client):
    client.add_cog(Raid(client))
