import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from keep_alive import keep_alive
keep_alive()

# Kendi bot kodların buradan devam etsin...
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")
BOT_STATUS = os.getenv("BOT_STATUS", "youtube.com/semoizm")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

if OWNER_ID:
    bot.owner_id = int(OWNER_ID)

@bot.event
async def on_ready():
    print(f"--- {bot.user} (ID: {bot.user.id}) olarak giriş yapıldı! ---")
    if OWNER_ID:
        print(f"Bot Sahibi ID'si başarıyla tanımlandı: {OWNER_ID}")

    custom_activity = discord.CustomActivity(name=BOT_STATUS)
    await bot.change_presence(activity=custom_activity)
    print(f"Bot özel durumu ayarlandı: {BOT_STATUS}")

    try:
        synced = await bot.tree.sync()
        print(f"Toplam {len(synced)} adet slash komutu senkronize edildi.")
    except Exception as e:
        print(f"Komutlar senkronize edilirken hata oluştu: {e}")


async def load_extensions():
    for filename in os.listdir("./komutlar"):
        if filename.endswith(".py") and filename != "__init__.py":
            extension_name = f"komutlar.{filename[:-3]}"
            try:
                await bot.load_extension(extension_name)
                print(f"[YÜKLENDİ] {extension_name}")
            except Exception as e:
                print(f"[HATA] {extension_name} yükletilemedi: {e}")


async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())