import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Needed to receive member updates

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_member_update(before, after):
    premium_role_name = "premium"

    before_roles = set(before.roles)
    after_roles = set(after.roles)

    # Check if the Premium role was added
    for role in after_roles - before_roles:
        if role.name == premium_role_name:
            channel = discord.utils.get(after.guild.text_channels, name="premium-welcome")
            if channel:
                await channel.send(f"🎉 Welcome {after.mention} to Premium!")

bot.run("no token for u")

