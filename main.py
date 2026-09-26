from flask import Flask
from threading import Thread
import os
import discord
from discord.ext import commands

# --- كود عشان رندر ما يفصل ---
app = Flask('')
@app.route('/')
def home():
    return "Hayato is online!"

def run():
    app.run(host='0.0.0.0', port=10000)

Thread(target=run).start()
# --------------------------------

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Hayato Bot شغال: {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # رد تلقائي
    if "احبك" in message.content.lower() or "أحبك" in message.content.lower():
        await message.channel.send(f"حبك برص {message.author.mention} 😂")

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

bot.run(os.getenv("TOKEN"))
