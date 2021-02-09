import discord
from discord.ext import commands
import random
import json

# The prefix for all the commands
client = commands.Bot(command_prefix = '-')

with open('auth.json') as f:
    data = json.load(f)

# Displays that the bot is ready
@client.event
async def on_ready():
    print('Bot is ready.')

    async def on_disconnect(self):
        print("Bot disconnected.")

# Lets the user know where to drop using -drop
@client.command()
async def drop(ctx):
    locations = ['Stealthy Stronghold', 'Colossal Coliseum', 'Salty Towers', 'Hunter’s Haven', 'Lazy Lake', 'Retail Row', 'Catty Corner', 'Misty Meadows', 'Slurpy Swamp', 'Holly Headges', 'Sweaty Sands', 'Coral Castle', 'Dirty Docks', 'Craggy Cliffs', 'Steamy Stacks']
    await ctx.send("You are dropping at: " + random.choice(locations))

    

client.run(data['token'])