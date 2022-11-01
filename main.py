import os
from keep_alive import keep_alive
import discord
from discord.ext import commands
import json
from discord import Embed
from flask import Flask
from threading import Thread
import time
import requests
import logging
import numpy as np
import random
import asyncio
from time import sleep
from os import system
import sqlite3

from discord import app_commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='D!', intents=intents)

bot.author_id = 984583981540442124  # Change to your discord id!!!


@bot.event
async def on_ready():
	print('Logged on as {0.user} '.format(bot), end='')
	print(f'in {len(bot.guilds)} guilds!')
	print('D!logs')
	print('None')
	game = discord.Game("D!help")
	await bot.change_presence(status=discord.Status.do_not_disturb,
	                          activity=game)


bool

extensions = [
    'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.
print(os.getenv("DISCORD_BOT_SECRET"))


@bot.event
async def on_member_join(member):
	server = member.server
	fmt = 'Welcome {0.mention} to {1.name}!'
	await bot.send_message(server, fmt.format(member, server))


@bot.command()
async def clearmsg(ctx, amount=1000):
	await ctx.channel.purge(limit=amount + 1)


@bot.command()
@commands.has_permissions(ban_members=True
                          )  #bans members if admin role is true
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
	await user.ban(reason=reason)
	ban = discord.Embed(
	    title=f":boom: Banned {user.name}!",
	    description=f"Reason: {reason}\nBy: {ctx.author.mention}",
	    color=0xB026FF)
	await ctx.message.delete()
	await ctx.channel.send(embed=ban)
	await user.send(embed=ban)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
	await user.kick(reason=reason)
	ban = discord.Embed(
	    title=f":boot: Kicked {user.name}!",
	    description=f"Reason: {reason}\nBy: {ctx.author.mention}",
	    color=0xB026FF)
	await ctx.message.delete()
	await ctx.channel.send(embed=ban)
	await user.send(embed=ban)


@bot.command()  ## get mentioned users avatar
async def av(ctx, *, avamember: discord.Member = None):
	userAvatarUrl = avamember.avatar_url
	await ctx.send(userAvatarUrl)


@bot.command(name='membercount')
async def membercount(ctx):
	await ctx.send(ctx.guild.member_count)


@bot.command()
async def apply(ctx):
	embed = discord.Embed(
	    title="Click Here To Apply",
	    url="https://forms.gle/seke67nG4oZT62vaA",
	    description=
	    "Thank you for submitting this form. We will contact your discord via DMs. Please keep your DM's open and DO NOT change your username/handle or # tag until DMed.",
	    color=0x00008B)
	await ctx.send(embed=embed)


@bot.command()
async def Changelog(ctx):
	embed = discord.Embed(
	    title="Changelog",
	    url="",
	    description="Now: Added 'D!ex'. 'D!ex' will start a timer.",
	    color=0x00008B)
	await ctx.send(embed=embed)


@bot.command()
async def Downtime(ctx):
	embed = discord.Embed(title="Downtime Info",
	                      url="",
	                      description="None. ",
	                      color=0xFF5733)
	await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel = None):
	overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
	overwrite.send_messages = False
	await ctx.channel.set_permissions(ctx.guild.default_role,
	                                  overwrite=overwrite)
	await ctx.send('Channel locked.')


@lock.error
async def lock_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
		await ctx.send('You do not have permission to use this command!')


@bot.command(pass_context=True)
async def assign(ctx, role):
	member = ctx.message.author
	role = discord.utils.get(member.server.roles, name=role)
	await bot.add_roles(member, role)
	await bot.say("Role added! {}".format(member.mention))


class SlashBot(commands.Bot):
	def __init__(self) -> None:
		super().__init__(command_prefix=".", intents=discord.Intents.default())

	async def setup_hook(self) -> None:
		self.tree.copy_global_to(guild=discord.Object(id=12345678900987654))
		await self.tree.sync()


bot = SlashBot()


@bot.tree.command(name="ping", description="...")
async def _ping(interaction: discord.Interaction) -> None:
	await interaction.response.send_message("pong")


class SlashBot(commands.Bot):
	def __init__(self) -> None:
		super().__init__(command_prefix=".", intents=discord.Intents.default())

	async def setup_hook(self) -> None:
		self.tree.copy_global_to(guild=discord.Object(id=12345678900987654))
		await self.tree.sync()


bot = SlashBot()


@bot.tree.command(name="start-timer", description="ding ding ding")
async def ex(ctx, time: int):
	await ctx.send("Countdown started")

	def check(message):
		return message.channel == ctx.channel and message.author == ctx.author and message.content.lower(
		) == "cancel"

	try:
		m = await bot.wait_for("message", check=check, timeout=time)
		await ctx.send("Countdown cancelled")
	except asyncio.TimeoutError:
		await ctx.send(f"{ctx.guild.default_role} countdown finished")


class SlashBot(commands.Bot):
	def __init__(self) -> None:
		super().__init__(command_prefix=".", intents=discord.Intents.default())

	async def setup_hook(self) -> None:
		self.tree.copy_global_to(guild=discord.Object(id=12345678900987654))
		await self.tree.sync()


bot = SlashBot()


@bot.tree.command(name="ping", description="...")
async def _ping(interaction: discord.Interaction) -> None:
	await interaction.response.send_message("pong")


class SlashBot(commands.Bot):
	def __init__(self) -> None:
		super().__init__(command_prefix=".", intents=discord.Intents.default())

	async def setup_hook(self) -> None:
		self.tree.copy_global_to(guild=discord.Object(id=12345678900987654))
		await self.tree.sync()


bot = SlashBot()


@bot.tree.command(name="what-happened", description="What happened")
async def _Info(interaction: discord.Interaction) -> None:
	await interaction.response.send_message(
	    "This bot is currently underconstructions as the development team is trying to transfer all D! prefix commands to slash commands. Be paitant and there will be bugs here and there but yeah. that is what happened. "
	)


keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)
