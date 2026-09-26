import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Hayato Bot شغال: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    # مانع الروابط
    if "http://" in message.content or "https://" in message.content or "discord.gg" in message.content:
        if not message.author.guild_permissions.manage_messages:
            await message.delete()
            await message.channel.send(f"{message.author.mention} ممنوع نشر الروابط!", delete_after=5)
            return
            
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send("البوت شغال 24 ساعة! ✅")

bot.run(os.getenv("TOKEN"))
