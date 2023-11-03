"""
Here Im testing how I can get the members on a list and this would send an Webhook!
"""

import asyncio
import discord
from discord import Webhook
import aiohttp

intents = discord.Intents.default()
intents.members = True
members = discord.Guild.name

async def anything(url):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session=session)
        embed = discord.Embed(title=member_list)

        await webhook.send(embed=embed)
if __name__ == "__main__":
    url = "webhook url"
    loop = asyncio.new_event_loop()
    loop.run_until_complete(anything(url))
    loop.close
