<h1 align="center">Bot-Script-for-Discord</h1>

Basic Python script for a Discord bot that sends quotes through commands, plays TTS quotes in voice channels and notifies when certain members enters a voice channel.
It was designed so that everytime someone types the word 'quote' in any sentence the bot would send a random quote that is stored in the *'.env'* file. This project
was developed as a personal project to have fun with friends during our calls in the app Discord. **Discord** is a VoIP and instant messaging social platform, users
have the ability to communicate with voice calls, video calls, text messaging, media and files in private chats or as part of communities called "servers" (these
communities are referred as **"guilds"** in the Discord API).

To provide more safety, it uses a *'.env'* file to read the quotes, bot token and id values that are stored there, in order to hide those values and ids from the
public eye in case anyone gets access to the code in the script. The submitted *'.env'* file in this reposotory already has a prototype of how your file should look.

-------------------------------

<h1 align="center">How To Use It</h1>

### Setup:


Before starting any script, you will firstly need to create the bot you want the script to work through the [Discord Developer Portal](https://discord.com/developers/applications).

To run this script the user will need to install **Python3** and **pip**, more specifically **version 3.10** of it (tutorial about it can be easily found through
Google) and requires a **Unix shell**. After that you will need to install the required Python libraries and dependencies that are used in it.
The first ones are the **discord.py**, which holds the Discord app API, **python-dotenv** and **gTTS** dependecies. For that just type in the console:

```s
pip3 install -U discord.py
pip3 install python-dotenv
pip3 install gTTS
```

The last dependency needed is **ffmpeg** to which requires both a sudo and pip installation:

```s
sudo apt install ffmpeg
pip3 install ffmpeg
```

### Instructions:

Both the script and *'.env'* file need to be in the same folder.

To run the script the user just needs to type in the terminal:

```s
python3 BotScript.py
```
