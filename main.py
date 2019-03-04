import discord
import asyncio

client = discord.Client()
token = input ("Token: ")
@client.event
async def on_ready():
    print('=========================')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('=========================')
    SERVER = input ("Server ID: ")
    newowner = input ("ID to transfer to: ")
    server = client.get_server(SERVER)
    owner = server.get_member(newowner)
    await client.edit_server(server, owner=owner)
    input ("Ownership Transferred.")

client.run(token, bot=False)
