import discord
from discord.ext import commands

intents = discord.Intents.default() # THANK YOU PAUL
bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)

with open("token.txt", "r") as f:
    TOKEN =  f.readline()



# Basically looks for a specified user, joins the vc they are in, and rickrolls them
@ bot.command()
async def rickroll(ctx, member=None):
    await ctx.message.delete()

    if member==None:
        await ctx.send("Provide a user to rick roll")
        return

    if "<" in member:
        member = member.replace("<", "")
        member = member.replace(">", "")
        member = member.replace("@", "")
        id = int(member)
    else:
        await ctx.send("Provide the user with a ping (e.x @User123)")
        return

    for channel in ctx.guild.voice_channels:    
        members = channel.members

        for user in members:
            if user.id == id:
                voice = await channel.connect()
                voice.play(discord.FFmpegPCMAudio(executable=r"C:\Users\kesha\Development\PythonProjects\ffmpeg.exe", source="Rickroll.mp3"))
                return

    await ctx.send(f"It seems that user is not in a voice channel right now")
@ bot.command()
async def disconnect(ctx):
    await ctx.message.delete()
    for b in bot.voice_clients:
        await b.disconnect()
        return

    await ctx.send(f"I am not in a voice channel currently.")

@bot.command(aliases = ['purify'])
@commands.has_permissions(manage_channels = True)
async def purge(ctx, amount: int):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount+1)

# This messages prints as soon as the bot has logged on
@ bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

bot.run(TOKEN)