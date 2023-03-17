# ------------------------------------------ #
#          Bot script for Discord            #
# ------------------------------------------ #
#         Project done by Manittas           #
#          Python 3.10.4 version             #
# ------------------------------------------ #

import os
import discord
import random
import ffmpeg
from dotenv import load_dotenv
from gtts import gTTS

# Loads the .env file that resides on the same level as the script and the opus file
# Grabs the API token from the .env file, this way, our bot token key is secured and hidden
# Gets the general channel id and member id to check when entering a voicechat
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
INTEREST_MEMBER_ID = int(os.getenv("USER_ID"))

# Gets the intents for the .Client()
intents = discord.Intents.default()
intents.message_content = True

# Gets the client object from discord.py which is synonymous with bot
bot = discord.Client(intents=intents)

# Get number of lines in the env file
fp = open(r".env", "r")
total_lines = len(fp.readlines())
fp.close()

#
# Gets random quote from the quotes list
# --------------------------------------
def get_quote():

    # total lines minus 3 since the range goes until x+1 and we have the token, channel id and user id in the env file
    return os.getenv(str(random.randint(1, (total_lines-3))))

#
# Event listener for when the bot is on
# -------------------------------------
@bot.event
async def on_ready():

    # Sends a message on the terminal stating the script is on everytime it is run
    print("Bot script for Discord Bot running with success!")

    # Checks in how many discord servers the bot is in
    servers_count = 0

    for server in bot.guilds:

        # Prints the ID, server name and increments the servers count
        print(f" > ({server.id}, name: {server.name})")
        servers_count += 1
    
    # Prints the total number of servers in which the bot is in
    print(f"Bot is in ({servers_count}) servers.")

#
# Event listener for when a user enters a voicechat
# -------------------------------------------------
@bot.event
async def on_voice_state_update(member, before, after):

    # Checks if the member entered a channel
    if member.id == INTEREST_MEMBER_ID:
        if before.channel is None and after.channel is not None:
            
            # Sends a message in the main chat everytime the member enters a voicecall
            message_channel = member.guild.get_channel(CHANNEL_ID)
            await message_channel.send("The member entered a voice channel!")

#
# Event listener for when someone sends a command
# -----------------------------------------------
@bot.event
async def on_message(message):

    # Saves the command string so that it reads the string no matter if the chars are lower or upper case in the string
    command = message.content.upper()

    # Checks if message corresponds to a command
    if command.find("QUOTE") != -1:
        # Sends back a message to the channel
        quote = get_quote()
        await message.channel.send(quote)

        # Checks if bot is connected to the voice chat
        for voice_client in bot.voice_clients:
            if voice_client.guild == message.guild:
                if voice_client.is_connected():
                    
                    # Sends a tts quote in the voice chat every x times
                    sound = gTTS(text=quote, lang="pt", slow=False)
                    sound.save("tts-audio.mp3")

                    # Plays the tts
                    try:
                        voice_client.play(discord.FFmpegPCMAudio('tts-audio.mp3'))
                    
                    # Handle exceptions
                    except ClientException as e:
                        print(f"ERROR <BotScript>: Client exception occured:\n'{e}'")
                    except TypeError as e:
                        print(f"ERROR <BotScript>: Type error:\n'{e}'")
    
    # Calls the bot to voicechat to do tts when anyone types 'enter voice'
    if command == "ENTER VOICE":

        # Checks if bot is already connected to vc and moves it to the new channel if different
        for vc in bot.voice_clients:
            if vc.guild == message.guild:
                if vc.channel.id == message.author.voice.channel.id:
                    return
                try:
                    await vc.move_to(message.author.voice.channel)
                except:
                    print("ERROR <BotScript>: can't connect to new voice.")

        # if it wasn't on a chat connects to the chat
        try:
            await message.author.voice.channel.connect()
        except:
            print("ERROR <BotScript>: can't connect to voice.")
    
    # Disconnects bot from voice channel when someone types 'leave voice'S
    if command == "LEAVE VOICE":
        for vc in bot.voice_clients:
            if vc.guild == message.guild:
                try:
                    await vc.disconnect()
                except:
                    print(f"ERROR <BotScript>: bot is not connected to voice chat in '{message.guild.name}' server, can't disconnect.")

# Executes the bot with the specified token
bot.run(DISCORD_TOKEN)