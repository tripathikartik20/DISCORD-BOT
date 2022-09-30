'''
discord bot 
28/6/2020
kartik tripathi
'''

#importing modules
#sdfs
from abc import get_cache_token
from http import client
import discord
import random
import json
from discord import user
from discord import channel
from discord.ext import commands
from discord import voice_client
from discord.ext.commands.core import guild_only




#making bot (intent are the previlage esclation for the bot so that it can access the member lisst or the the gluid)


# intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

def get_prefix(client, message):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]
# defing bot
client = commands.Bot(command_prefix = '\')

#assigning tasks
@client.command()
async def ping(ctx):
    await ctx.send(f'pong!{round(client.latency*1000)}ms')

@client.event
async def on_member_join(member):
    print(f'{member} has joined')
    
@client.event
async def on_member_remove(member):
    print(f'{member} has been removed')

@client.command()
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def ban(ctx,member:discord.member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx,*,member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name, user.discriminator)==(member_name,-member.discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned{user.mention}')
            return

@client.command(aliases = ['8ball,test'])
async def _8ball(ctx, *, question):
    responces = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question:{question}\n Answer: {random.choice(responces)}')


@client.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('no one in the voice chat!')

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client): # checks if bot is in vc
        await ctx.send("i left the voice channel as you said")
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("i haven't joined")

@client.command()
async def make_channel(ctx):
    guild = ctx.guild
    member = ctx.author
#    admin_role = get(guild.roles, name="Admin")
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True),
#        admin_role: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await guild.create_text_channel('secret', overwrites=overwrites)
'''
    You can use Guild.create_text_channel to create a text channel with certain permissions overwrites.
     The below creates a channel that is visible only to the caller, the bot, and members with the "Admin" role 
     (You'll need to change that to the appropriate role for your server)
'''

# calling bot
client.run('MTAyNDM2MDYxMDkyMzgxOTAxOA.G3HkAQ.hoFvhbKdQ4KYuSl8_nWbBmxlyEKy3nt4Stzr7A')
