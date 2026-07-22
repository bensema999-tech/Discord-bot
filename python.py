import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content == '!hello':
        await message.channel.send('Hello!')

client.run("MTUyNTExNzQ0MTczNzM2MzU4OQ.GCdjYl.CswkgQTW-cQr77W63-lVpbUbvCLq6-U6P6w9G4")
