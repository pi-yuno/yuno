#!/usr/bin/env python


import os
import discord
from discord.ext import commands

prefix = "do "
intents = discord.Intents.all()
bot = commands.Bot(prefix, intents=intents)
YUNO = os.environ["YUNO"]
