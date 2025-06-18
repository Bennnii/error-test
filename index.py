from nextcord.ext import commands
from commands import normal_commands

TOKEN = 'TEST'

client = commands.Bot(command_prefix = "haru!")

@client.event
async def on_ready():
    print("Successfully started instance✔️")
    print("\n-----------------------------------------------")
    print(f"{client.user} is now online!")
    print("All systems are running!")
    print("-----------------------------------------------\n")

client.run(TOKEN)
