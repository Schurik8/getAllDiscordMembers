"""
Here I have tested how I can indentify the members
"""

import discord
from discord.ext import commands

intents = discord.Intents.all()

guild_id = input("Put here your Guild ID: ")

if guild_id is int:
    guild = int(guild_id)
    guild_name = discord.Guild(id=guild).name
    file_name = guild_name, ".txt"
    members = discord.Guild(id=guild).members
    for member in members:
        with open(file_name, "w") as file:
            file.write(member)
