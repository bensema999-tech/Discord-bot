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

client.run(MTUyODk0MjI3NTc3MjY3ODE2NQ.GuudPy.N8Ho1d211-F_fOtY6khUdm6sITZKCmrGkNL-II)
