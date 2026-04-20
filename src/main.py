import os
import discord
from discord import app_commands
from src.logging_setup import configure_logging

configure_logging()

import structlog
log = structlog.get_logger()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name="hello", description="Say hello to Aya")
async def hello(interaction: discord.Interaction) -> None:
    await interaction.response.send_message("Hello! I'm Aya. 👋")


@client.event
async def on_ready() -> None:
    await tree.sync()
    log.info("aya_ready", user=str(client.user))


client.run(os.environ["DISCORD_TOKEN"])
