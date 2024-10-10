import os
import discord
import asyncio
from discord.ext import commands

from myserver import server_on

# กำหนดการตั้งค่าบอท
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# กำหนดเวลา 2 ชั่วโมงครึ่ง (9000 วินาที)
TIME_INTERVAL = 9000  # 2 ชั่วโมงครึ่ง

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    bot.loop.create_task(notification_task())

# ฟังก์ชันสำหรับแจ้งเตือนทุก ๆ 2 ชั่วโมงครึ่ง
async def notification_task():
    await bot.wait_until_ready()
    channel = bot.get_channel("1272892370513559654")  # ใส่ ID ของแชนแนลที่จะส่งแจ้งเตือน
    while not bot.is_closed():
        await channel.send("ถึงเวลาเข้าเวรแล้ว!")
        await asyncio.sleep(TIME_INTERVAL)  # รอ 2 ชั่วโมงครึ่งก่อนแจ้งเตือนครั้งต่อไป

# รันบอท

server_on()

bot.run(os.getenv('TOKEN'))
