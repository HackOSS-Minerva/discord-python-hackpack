"""
Discord Bot
"""

import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents
try:
    from bot.hello import Hello
except ImportError:
    from hello import Hello

load_dotenv()
if not os.getenv('DISCORD_BOT_TOKEN'):
    load_dotenv('.env.local')

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

bot = commands.Bot(command_prefix="!", intents=Intents.all())
hello = Hello()


@bot.event
async def on_member_join(member):
    """Run when a new member joins the Discord server."""
    print(f"New Member Joined! {hello.get_greeting(member.name)}")


# Slash command (/ping)
@bot.tree.command(name="ping", description="Check bot latency")
async def slash_ping(interaction):
    """Check bot latency."""
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f"Pong! 🏓 ({latency}ms)")


@bot.event
async def on_ready():
    """Run when the bot initially loads."""
    await bot.tree.sync()
    try:
        hello.print_message(f"Hello World! Logged in as {bot.user}")
    except RuntimeError as err:
        print(err)


def main():
    """Start and run the Discord bot."""
    if not TOKEN:
        raise ValueError(
            "DISCORD_BOT_TOKEN is not set! Please add your bot token to .env or .env.local.")
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
