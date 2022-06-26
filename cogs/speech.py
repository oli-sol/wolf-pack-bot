import random

import discord
from discord.ext import commands


class Speech(commands.Cog):
    """Speech Cog"""

    def __init__(self, client):
        # sets client variable so it can be used in cog
        self.client = client
        self._last_member = None

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.mention}! *wags tail*'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member

    @commands.command()
    async def roast_me(self, ctx):
        name = ctx.author.mention

        roasts = [
            f'{name} you\'re my favorite person besides every other person I\'ve ever met. Woof!',
            f'{name} I envy people who have never met you. Woof!',
            f'Bark! {name} if you were an inanimate object, you’d be a participation trophy. *wags tail*',
            f'{name} you are a pizza burn on the roof of the world\'s mouth. Woof!',
            f'{name} you have the charm and charisma of a burning orphanage. *wags tail contently*',
            f'Bark! {name} if there was a single intelligent thought in your head it would have died from loneliness.',
            f'{name} I want you to be the pallbearer at my funeral so you can let me down one last time. Woof!'
        ]

        response = random.choice(roasts)
        await ctx.channel.send(response)

    @commands.command()
    async def joke(self, ctx):
        name = ctx.author.mention

        jokes = [
            f'{name} What do you call a dog that has been left outside in the cold for an extended period of time?\n '
            f'\nA chili-dog.\n\nWoof!',
            f'{name} What kind of dog likes taking a bath every day?\n '
            f'\nA shampoo-dle.\n\n*wags tail*',
            f'{name} What do you call a dog magician?\n\nA labracadabrador.\n\n*wags tail*',
            f'{name} Why did the two-legged dog to come to an abrupt halt?\n\nIt had two paws.\n\nWoof!',
            f'{name} What do you get when you cross a dog with a phone?\n\nA golden receiver.\n\n*wags tail*',
            f'{name} What could be more incredible than a talking dog?\n\nA spelling bee.\n\nWoof!',
            f'{name} Why did the dog upgrade his phone plan?\n\nTo get collar ID.\n\n*wags tail*',
            f'{name} Why are dogs so loud?\n\nThey have built-in sub-woofers.\n\nWoof!',
            f'{name} What do you call a dog that can\'t bark?\n\nA hushpuppy.\n\n*wags tail*',
            f'{name} Where does a Labrador’s food go before it can be sold in stores?\n\nTo the lab for '
            f'testing.\n\n*wags tail contently* ',
            f'{name} Whenever I go to the park, the ducks always try to bite me.\n\nMust be because I\'m '
            f'pure bread.\n\n*wags tail contently*'
        ]

        response = random.choice(jokes)
        await ctx.channel.send(response)


def setup(client):
    client.add_cog(Speech(client))
