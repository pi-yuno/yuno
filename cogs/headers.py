#!/usr/bin/env python


import os
import discord
from discord.ext import commands

prefix = ["do ", "Do ", "<@1185650759287713843>"]

intents = discord.Intents.all()

bot = commands.Bot(prefix, intents=intents)

YUNO = os.environ["YUNO"]

reactions = ['airkiss', 'angrystare', 'bite', 'bleh', 'blush', 'brofist', 'celebrate', 'cheers', 'clap', 'confused', 'cool', 'cry', 'cuddle', 'dance', 'drool', 'evillaugh', 'facepalm', 'handhold', 'happy', 'headbang', 'hug', 'kiss', 'laugh', 'lick', 'love', 'mad', 'nervous', 'no', 'nom', 'nosebleed', 'nuzzle', 'nyah', 'pat', 'peek', 'pinch', 'poke', 'pout', 'punch', 'roll', 'run', 'sad', 'scared', 'shout', 'shrug', 'shy', 'sigh', 'sip', 'slap', 'sleep', 'slowclap', 'smack', 'smile', 'smug', 'sneeze', 'sorry', 'stare', 'stop', 'surprised', 'sweat', 'thumbsup', 'tickle', 'tired', 'wave', 'wink', 'woah', 'yawn', 'yay', 'yes']
