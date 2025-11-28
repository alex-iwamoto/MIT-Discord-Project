#
//  discord_only.py
//  
//
//  Created by Alexander Iwamoto Araujo on 27/11/25.
//

from dotenv import load_dotenv
import discord
import os

# load environment variables from .env file
load_dotenv()

# set up intents
intents = discord.Intents.default()
intents.message_content = True # Ensure that your bot can read this message content

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged ins as {0.user}'.format(client))
    
@client.event
async def on_message():
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))

