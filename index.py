from nextcord.ext import commands
from commands import normal_commands

TOKEN = 'Nzg4ODIzMTc4OTQ3NDYxMTIw.GWhQ9-.5wS0qvfOf2iUjdmCMYcpXbrP0EQFSPOBJcy2J0'

client = commands.Bot(command_prefix = "haru!")

@client.event
async def on_ready():
    print("Successfully started instance✔️")
    print("\n-----------------------------------------------")
    print(f"{client.user} is now online!")
    print("All systems are running!")
    print("-----------------------------------------------\n")

client.run(TOKEN)
