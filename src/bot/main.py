"""
Discord Bot
"""

import os

from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

from bot.hello import Hello

bot = commands.Bot(command_prefix="!", intents=Intents.all())


def setup():
    """Load environment variables and initialize helper services."""
    load_dotenv()
    if not os.getenv("DISCORD_BOT_TOKEN"):
        load_dotenv(".env.local")

    token = os.getenv("DISCORD_BOT_TOKEN")
    hello_service = Hello()
    return token, hello_service


TOKEN, hello = setup()


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
            "DISCORD_BOT_TOKEN is not set! Please add your bot token to .env or .env.local."
        )
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
