import discord
import os
import webserver
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Needed to receive member updates

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_member_update(before, after):
    premium_role_name = "🐉| Feng Academy Student"

    before_roles = set(before.roles)
    after_roles = set(after.roles)

    # Check if the Premium role was added
    for role in after_roles - before_roles:
        if role.name == premium_role_name:
            channel = discord.utils.get(after.guild.text_channels, name="🙋| member-log")
            if channel:
                await channel.send(f"🎉 Welcome {after.mention} to the Feng Academy!")

webserver.keep_alive()

bot.run(os.environ["DISCORD_SECRET"])

