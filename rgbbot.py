import discord
from discord.ext import commands
import datetime
from discord.utils import get
import asyncio
from time import sleep
from colorsys import hls_to_rgb
import youtube_dl
import os
import requests
import random
from random import randint, choice, choices
import io
import sqlite3
import random as r
import requests
import io
import typing
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import requests
from io import BytesIO
client = commands.Bot( command_prefix = '*')

@client.command()
async def color_role(ctx):
    roleid = 801489893926502440
    role = discord.utils.get(ctx.guild.roles, id= roleid) 
    colors = [0xff0000, 0xff3300, 0xff4d00, 0xff5500, 0xff5e00, 0xff6f00, 0xff7700, 0xff8800, 0xff9500, 0xffa600, 0xffae00, 0xffdd00, 0xffee00, 0xeaff00, 0xccff00, 0xb7ff00, 0x9dff00, 0x73ff00, 0x00ff59, 0x00ff7b, 0x00ff95, 0x00ffb3, 0x00ffcc, 0x00ffea, 0x00fbff, 0x00e1ff, 0x00d9ff, 0x00ccff, 0x00bbff, 0x00a2ff, 0x008cff, 0x0073ff, 0x0059ff, 0x2b00ff, 0x4c00ff, 0x6200ff, 0x8400ff, 0x9d00ff, 0xaa00ff, 0xbf00ff, 0xcc00ff, 0xe100ff, 0xff00f2, 0xff00dd, 0xff00c8, 0xff00ae, 0xff00a2, 0xff0084, 0xff0062, 0xff0040, 0xff002f]
    colo = 0
    while True:
        if colo <= 50:
            await role.edit(color= discord.Colour(colors[colo]))
            await asyncio.sleep(2)
            colo = colo + 1
        else:
            colo = 0

token= os.environ.get('BOT_TOKEN')
client.run( token )
