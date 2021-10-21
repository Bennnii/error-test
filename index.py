from nextcord.ext import commands
from discord_ui import UI
from commands import normal_commands

TOKEN = 'TEST_TOKEN'

client = commands.Bot(command_prefix = "haru!")
client.ui = UI(client, {'auto_sync': False, "sync_on_cog": True})

normal_commands.register(client, client.ui)

@client.event
async def on_ready():
    print("Ready! Pterodactyl")
    print("\n-----------------------------------------------")
    print(f"{client.user} is now online!")
    print("All systems are running!")
    print("-----------------------------------------------\n")

client.run(TOKEN)