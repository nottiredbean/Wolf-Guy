import os
import random, requests
from random import randint, randrange
import time
from time import strftime
import datetime
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound, CheckFailure, MissingRequiredArgument
import platform
from flask import Flask
from threading import Thread

app = Flask("")


@app.route("/")
def index():
	return "<h1></h1>"


Thread(target=app.run, args=("0.0.0.0", 8080)).start()

import asyncio
import datetime
import os
import traceback
import json
import logging
import args
from discord.utils import get
import bs4
from bs4 import BeautifulSoup
import urllib3
import re
import praw
import string
import corona
import aiohttp
from time import gmtime
import humanfriendly
from os import system
from discord import FFmpegPCMAudio
import ffmpeg
import PIL
from PIL import Image, ImageDraw, ImageFont
import io
import sys
import argparse
import ffmpeg
import functools
import itertools
import math
import youtube_dl
from async_timeout import timeout
from discord.ext import commands
from AntiSpam import AntiSpamHandler

amounts = {}

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=".", intents=intents)
bot.handler = AntiSpamHandler(bot)



@bot.event
async def on_ready():
	print("Bot is running!")
	await bot.change_presence(activity=discord.Game(".help for all commands"))

@bot.event
async def on_message(message):
    await bot.handler.propagate(message)
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, CommandNotFound):
		await ctx.message.delete()
		await ctx.send(
		    "❌Command not found, If you think this is an issue please join the support server - https://dsc.gg/thewolfers"
		)
		return
	elif isinstance(error, CheckFailure):
		await ctx.send(
		    "❌You don't had enough permission to execute this command, If you think this is an issue please join the support server - https://dsc.gg/thewolfers"
		)
		return
	elif isinstance(error, commands.CommandOnCooldown):
		seconds = error.retry_after
		m, s = divmod(seconds, 60)
		h, m = divmod(m, 60)
		d, h = divmod(h, 24)
		await ctx.send(
		    f"You're on cooldown. Please wait {int(h)} hours, {int(m)} minutes and {int(s)} seconds"
		)
		return


@bot.command()
@commands.has_permissions(manage_channels=True)
async def kick(ctx, Member: discord.Member, *, reason=None):
	await Member.kick(reason=reason)
	await ctx.send(f'Kicked {Member.mention}')


@bot.command()
@commands.has_permissions(manage_channels=True)
async def ban(ctx, Member: discord.Member, *, reason=None):
	await Member.ban(reason=reason)
	await ctx.send(f'Banned {Member.mention}')


@bot.command()
@commands.has_permissions(manage_channels=True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()

	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name,
 member_discriminator):
			await ctx.guild.unban(user)
			await ctx.channel.send(f"Unbanned: {user.mention}")



@bot.command()
async def random(ctx):
	await ctx.send(randint(1, 100))


from flask import Flask
from threading import Thread


@bot.command()
async def support(ctx):
	await ctx.send('For Support please contact The Lonely Wolf#1795'
	'or join the support server'
	'https://dsc.gg/thewolfers')


@bot.command()
async def YouTube(ctx):
	await ctx.send(
	    'YouTube-https://www.youtube.com/channel/UC98qVfkpBTcmTMKPMoDg40Q')


@bot.command()
async def Twitch(ctx):
	await ctx.send('Twitch- https://twitch.tv/thelonelywolfer')


@bot.command()
async def Twitter(ctx):
	await ctx.send('Twitter- https://twitter.com/thelonelywolfer')


@bot.command()
async def Instagram(ctx):
	await ctx.send('Instagram- https://instagram.com/thelonelywolfer')


@bot.command()
async def donate(ctx):
	await ctx.send('https://paypal.me/thelonelywolfer')

@bot.command()
async def Socials(ctx):
  await ctx.channel.trigger_typing()
  await ctx.send(embed=e)
e = discord.Embed(color=0x3366FF)
e.add_field(name="YouTube", value= "https://www.youtube.com/channel/UC98qVfkpBTcmTMKPMoDg40Q")
e.add_field(name="Twitter", value="https://twitter.com/thelonelywolfer")
e.add_field(name="Instagram", value="https://instagram.com/thelonelywolfer")
e.add_field(name="Twitch", value="https://twitch.tv/thelonelywolfer")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, user: discord.Member, role: discord.Role):
  author = ctx.author
  await user.add_roles(role)
  await ctx.send(f"Added **{role.name}** to **{user}**")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, user: discord.Member, role: discord.Role):
	author = ctx.author
	await user.remove_roles(role)
	await ctx.send(f"Removed **{role.name}** from **{user}**")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def NewChannel(ctx, *, arg):
	await ctx.guild.create_text_channel(name=f"{arg}")


@bot.command()
@commands.has_permissions(manage_roles=True)
async def NewRole(ctx, *, arg):
	await ctx.guild.create_role(name=f"{arg}")


@bot.command()
@commands.has_permissions(administrator=True)
async def lock(ctx):
	await ctx.channel.set_permissions(
	    ctx.guild.default_role, send_messages=False)
	await ctx.send(f"Locked {ctx.channel.mention}!")


@bot.command()
@commands.has_permissions(administrator=True)
async def unlock(ctx):
	await ctx.channel.set_permissions(
	    ctx.guild.default_role, send_messages=True)
	await ctx.send(f"Unlocked {ctx.channel.mention}!")


@bot.command()
@commands.has_permissions(administrator=True)
async def public(ctx):
	await ctx.channel.set_permissions(
	    ctx.guild.default_role, read_messages=True)
	await ctx.send("This channel is now public!")


@bot.command()
@commands.has_permissions(administrator=True)
async def private(ctx):
	await ctx.channel.set_permissions(
	    ctx.guild.default_role, read_messages=False)
	await ctx.send("This channel is now private!")


@bot.command()
@commands.has_permissions(manage_channels=True)
async def NewNSFW(ctx, *, name):
	await ctx.guild.create_text_channel(name, nsfw=True)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def NewCategory(ctx, *, name):
	await ctx.guild.create_category(name)


@bot.command()
async def NewVoice(ctx, *, name):
	await ctx.guild.create_voice_channel(name)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def DeleteChannel(ctx):
	await ctx.channel.delete()


bot.remove_command("help")


@bot.command()
async def help(ctx):
	await ctx.channel.trigger_typing()
	e=discord.Embed(color=0x3366FF)
	e.add_field(name="donate", value="Donate to support us")
	e.add_field(name="invite", value="Useful links")
	e.add_field(name="Socials", value="Shows the developers socials")
	e.add_field(name="Moderation commands", value=".moderation")
	e.add_field(name="Economy commands", value=".economy")

	e.set_footer(
	    text=
	    "If you had any problems, please contact to the developer(The Lonely Wolf#1795) and if you want to use the .nick command you will have to keep the bot at the highest role in the server"
	)
	await ctx.author.send(embed=e)
	await ctx.send("DM sent!")


@bot.command()
async def vote(ctx):
	await ctx.send('https://top.gg/bot/787337762919546911')

@bot.command()
async def economy(ctx):
	e = discord.Embed(color=0x3366FF)
	e.add_field(name="**__Economy commands__**", value="** **")
	e.add_field(name="register", value="Create an account")
	e.add_field(name="balance", value="Shows your balance")
	e.add_field(name="beg", value="Earn coins by begging")
	e.add_field(name="leaderboard", value="Top richest users")
	e.set_footer(
	    text=
	    "If you had any problems, please contact to the developer.(The Lonely Wolf#1795)"
	)
	await ctx.author.send(embed=e)
	await ctx.send("DM sent!")


@bot.command()
@commands.has_permissions(manage_roles=True)
async def tempmute(time=0):
    time_list = re.split('(\d+)',time)
    if time_list[2] == "s":
        time_in_s = int(time_list[1])
    if time_list[2] == "min":
        time_in_s = int(time_list[1]) * 60
    if time_list[2] == "h":
        time_in_s = int(time_list[1]) * 60 * 60
    if time_list[2] == "d":
        time_in_s = int(time_list[1]) * 60 * 60 * 60
    return time_in_s


print(tempmute("15h"))

@bot.command(pass_context=True)
async def balance(ctx):
	id = str(ctx.message.author.id)
	if id in amounts:
		await ctx.send("You have {} in the bank".format(amounts[id]))
	else:
		await ctx.send("You do not have an account")


@bot.command(pass_context=True)
async def register(ctx):
	id = str(ctx.message.author.id)
	if id not in amounts:
		amounts[id] = 100
		await ctx.send("You are now registered")
		_save()
	else:
		await ctx.send("You already have an account")


@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
	beg = randint(0, 1000)
	per = randint(0, 10)
	id = str(ctx.message.author.id)
	if id in amounts:
		amounts[id] += beg
		await ctx.send(
		    f"**Your friend** had donated {beg} to {ctx.author.mention}!")
		_save()
	elif per == 10:
		await ctx.send(f"**Your friend:** I'm poor.")


def _save():
	with open('amounts.json', 'w+') as f:
		json.dump(amounts, f)


@bot.command(pass_context=True)
async def transfer(ctx, amount: int, other: discord.Member):
	primary_id = str(ctx.message.author.id)
	other_id = str(other.id)
	if primary_id not in amounts:
		await ctx.send("You do not have an account")
	elif other_id not in amounts:
		await ctx.send("The other party does not have an account")
	elif amounts[primary_id] < amount:
		await ctx.send("You cannot afford this transaction")
	else:
		amounts[primary_id] -= amount
		amounts[other_id] += amount
		await ctx.send("Transaction complete")
	_save()


@bot.command()
async def save():
	_save()


leaderboards = []
for key, value in amounts.items():
	leaderboards.append(LeaderBoardPosition(key, value))

top = sorted(leaderboards, key=lambda x: x.coins, reverse=True)


@bot.command()
async def leaderboard(ctx):

	with open('amounts.json', 'r') as f:
		data = json.load(f)

	top_users = {
	    k: v
	    for k, v in sorted(
	        data.items(), key=lambda item: item[1], reverse=True)
	}

	names = ''
	for postion, user in enumerate(top_users):
		names += f'{postion+1} - <@!{user}> with {top_users[user]}\n'

	embed = discord.Embed(title="Leaderboard")
	embed.add_field(name="Names", value=names, inline=False)
	await ctx.send(embed=embed)


def _save():
	with open('amounts.json', 'w+') as f:
		json.dump(amounts, f)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def clear(ctx, limit: int):
	await ctx.message.delete()
	await ctx.channel.purge(limit=limit)
	await ctx.send("Deleted %s messages!" % limit, delete_after=1)


@bot.command()
async def servercount(ctx):
	await ctx.send("I'm in " + str(len(bot.guilds)) + " servers")


@bot.command()
async def avatar(ctx, member: discord.User = None):
	await ctx.send(f"{member.avatar_url}")


@bot.command()
@commands.has_permissions(administrator=True)
async def nick(ctx, member: discord.Member, *, name):
	await member.edit(nick=name)
	await ctx.send(f"Renamed {member.mention} to {name}")

		
@bot.command()
async def moderation(ctx):
 e=discord.Embed(color=0x3366FF)
 e.add_field(name="addrole",value="Adds a role to the mentioned member")
 e.add_field(name="removerole",value="Removes a role to the mentioned member")
 e.add_field(name="clear",value="Deletes messages")
 e.add_field(name="kick", value="Kicks a member")
 e.add_field(name="ban", value="Bans a member")
 e.add_field(name="tempmute", value="Temporary mutes a member")
 e.add_field(name="slowmode",value="Sets the slowmode of a channel.")
 e.add_field(name="nuke", value="Nukes a channel")
 e.add_field(name="setautorole", value="Automatically gives the role to members who joined the server")
 e.add_field(name="removeautorole", value="Removes the auto role.")
 e.add_field(name="NewCategory", value="Creates a new Category")
 e.add_field(name="NewChannel", value="Creates a New category")
 e.add_field(name="NewRole", value="Creates a New Role")
 e.add_field(name="NewNSFW", value="Creates a new NSFW channel")
 e.add_field(name="NewVoice", value="Creates a new Voice channel")
 e.add_field(name="DeleteChannel", value="deletes your current channel.")
 e.set_footer(text="If you had any problems, please contact to the developer.(The Lonely Wolf#1795)") 
 await ctx.author.send(embed=e)
 await ctx.send("DM sent!")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def setautorole(ctx,arg:discord.Role=None):
    print(ctx.guild.id)
    with open("auto.json") as f:
       data = json.load(f)
       print(data)
       id = str(ctx.guild.id)
    if id not in data:
      data[id]=int(arg.id)
      print(data[id])
      with open("auto.json", 'w') as f:
        json.dump(data, f)
        await ctx.send(f"{arg.mention} will be assigned to new members!")
        
@bot.command()
async def autorole(ctx):
  with open("auto.json") as f:
   data=json.load(f)
   if data in str(ctx.guild.id):
   # data=json.load(f)
    role=data[str(ctx.guild.id)]
    await ctx.send(f"<&{int(role)}>")
   else:
    await ctx.send("There's no auto roles.")

@bot.command()
async def membercount(ctx):
  await ctx.send(f"{len(ctx.guild.members)} members") 

@bot.command()
async def invite(ctx):
  await ctx.send ("https://discord.com/oauth2/authorize?client_id=787337762919546911&permissions=8&scope=bot")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def removeautorole(ctx,arg:discord.Role=None):
  with open("auto.json") as f:
    data = json.load(f)
    id = str(ctx.guild.id)
    del data[id]
    await ctx.send(f"{arg.mention} will no longer be assigned to new members!")
    with open("auto.json", 'w') as f:
        json.dump(data, f)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, amount):
  if amount:
   await ctx.channel.edit(reason='Bot Slowmode Command', slowmode_delay=int(amount))
   await ctx.send("Slowmode set to %s seconds!"%amount)
  else:
   await ctx.send("Slowmode was %s seconds!"%amount)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def nuke(ctx):
	p = ctx.channel.position
	print(p)
	clhannel = await ctx.channel.clone()
	await ctx.channel.delete()
	e = discord.Embed(
	    title="✅ Nuked this channel.", description=None, color=0x3366FF)
	e.set_footer(text=f"{time.ctime()}")
	await clhannel.send(embed=e)
	await clhannel.edit(position=int(p))


@bot.event
async def on_message(message):
	await bot.process_commands(message)

	if (message.content.startswith(f'{bot.user.mention}')):
		await message.channel.send("Hi, my prefix is `.`")


@bot.command()
@commands.has_permissions(administrator=True)
async def restart(ctx):
	e = discord.Embed(title="Restarting...", description=None, color=0)
	await ctx.send(embed=e)
	os.execl(sys.executable, sys.executable, *sys.argv)


bot.run("TOKEN")
