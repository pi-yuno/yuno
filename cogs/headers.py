#!/usr/bin/env python


import os
import discord
from discord.ext import commands
import requests

prefix = ["gh ", "git ", "do ", "<@1185650759287713843> "]

intents = discord.Intents.all()

bot = commands.Bot(prefix, intents=intents)

YUNO = os.environ["YUNO"]

reactions = ['airkiss', 'angrystare', 'bite', 'bleh', 'blush', 'brofist', 'celebrate', 'cheers', 'clap', 'confused', 'cool', 'cry', 'cuddle', 'dance', 'drool', 'evillaugh', 'facepalm', 'handhold', 'happy', 'headbang', 'hug', 'kiss', 'laugh', 'lick', 'love', 'mad', 'nervous', 'no', 'nom', 'nosebleed', 'nuzzle', 'nyah', 'pat', 'peek', 'pinch', 'poke', 'pout', 'punch', 'roll', 'run', 'sad', 'scared', 'shout', 'shrug', 'shy', 'sigh', 'sip', 'slap', 'sleep', 'slowclap', 'smack', 'smile', 'smug', 'sneeze', 'sorry', 'stare', 'stop', 'surprised', 'sweat', 'thumbsup', 'tickle', 'tired', 'wave', 'wink', 'woah', 'yawn', 'yay', 'yes']


def downimg(url:str):
    try:
        response = requests.get(url=url)
    except:
        return False
    if response.status_code == 200:
        file_format = response.headers["Content-Type"][6:]
        with open(f"file.{file_format}", "wb") as file:
            file.write(response.content)
        return f"file.{file_format}"
    else:
        return False

