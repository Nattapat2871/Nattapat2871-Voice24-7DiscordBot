import os
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from dotenv import load_dotenv
from server import server_on


# ตั้งค่า Intents และ Bot
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    # ดึงค่า Guild ID และ Voice Channel ID จาก environment variables
    guild_id = int(os.getenv('SERVER_ID'))
    channel_id = int(os.getenv('VOICE_CHANNEL_ID'))

    guild = bot.get_guild(guild_id)
    if guild:
        channel = guild.get_channel(channel_id)
        if channel and isinstance(channel, discord.VoiceChannel):
            # เข้าช่องเสียง
            voice_client = await channel.connect()
            print(f'บอทเข้าช่องเสียง {channel.name} แล้ว!')
        else:
            print('ไม่พบช่องเสียงที่ระบุ หรือช่องนี้ไม่ใช่ช่องเสียง')
    else:
        print('ไม่พบเซิร์ฟเวอร์ที่ระบุ')

bot.run(os.getenv('TOKEN'))
