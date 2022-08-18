# made by $age, hope this helps or is needed
# use the help command for more info
# enjoy



# Importing
import os
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from discord.ext import tasks

# config
token = TOKENHERE #token
bprefix = "!" #prefix
bownerid = 997869002359578714 #yourid
timetowait = 0 #time to wait before dms, (seconds), You can make this faster by doing something like 1 / 5 (0.2 seconds)

#intents
intents = discord.Intents.all()
client = commands.Bot(command_prefix = f'{bprefix}',owner_id = bownerid , intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
  print(" ")
  print(f"             Logged in as {client.user}")
  print(" ")
  print(f"Guilds: {len(client.guilds)}")
  mems = 0
  for g in client.guilds:
    mems = mems + g.member_count
  print(f"Members: {mems}")
  print(f"Bot Invite = https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot")

@client.command()
async def help(ctx):
  e = discord.Embed(description = ''':link: **HELP COMMANDS** :link: \n
                                  :gear: **dmallo** - Dm all online users in your server \n
                                  `!dmallo #channel message` \n
                                  :gear: **dmall** - Dm All users offline and online in your server \n
                                  `!dmall #channel message` \n
                                  This script currently only works with `messages` as it helps your bot not get banned.''')
  await ctx.send(embed = e)


@client.command()
async def dmallo(ctx,channel: discord.TextChannel,*,message):
  guild = ctx.guild
  sent = 0
  offline = 0
  e = discord.Embed(description = f":gear: Starting DMS to <#{channel.id}> with the message `{message}` | ONLINE USERS ONLY")
  a = await ctx.channel.send(embed = e)
  for member in guild.members:
    if member.status == discord.Status.offline:
      offline = offline + 1
      print(f"[{offline}] | (offline) | {member} | {member.id} ")
    else:
      try:
        await member.send(f"<#{channel.id}> {message}")
        sent = sent + 1
        print(f"[{sent}] | DM was sent to | {member} | {member.id} ")
      except:
        offline = offline + 1
        print(f"[{offline}] | DM couldn't be sent to | {member} | {member.id} ")
    await asyncio.sleep(timetowait)
  b = discord.Embed(description = f"Sent DMS to `{sent}` Users | `{offline}` users were offline or could not be DMD")
  await a.edit(embed = b)
  
@client.command()
async def dmall(ctx,channel: discord.TextChannel,*,message):
  guild = ctx.guild
  sent = 0
  notsent = 0
  e = discord.Embed(description = f":gear: Starting DMS to <#{channel.id}> with the message `{message}` | ALL USERS")
  a = await ctx.channel.send(embed = e)
  for member in guild.members:
    try:
      await member.send(f"<#{channel.id}> {message}")
      sent = sent + 1
      print(f"[{sent}] | DM was sent to | {member} | {member.id} ")
    except:
        notsent = notsent + 1
        print(f"[{notsent}] | DM couldn't be sent to | {member} | {member.id} ")
    await asyncio.sleep(timetowait)
  b = discord.Embed(description = f"Sent DMS to `{sent}` Users | `{notsent}` users could not be DMD")
  await a.edit(embed = b)  

client.run(f"{token}")
