# lapo script
# made by asmpro
# date: 26/3/2023
# TG:@asmprotk

from telethon import TelegramClient
import time
api_id = 12345678
api_hash = "9759ca9382e57eaf3bdf1c68002a8261"
client = TelegramClient("session", api_id, api_hash)
client.start()

t = time.strftime("%A\n%d/%m/%Y\n%I:%M:%S %p")


async def main():
    await client.send_message("asmprotk", f"**Laptop is opened!**\n{t}")
with client:
    client.loop.run_until_complete(main())
