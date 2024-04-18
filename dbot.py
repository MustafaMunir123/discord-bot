import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GUILD = os.getenv('DISCORD_GUILD_NAME')

# DISCORD_BOT_TOKEN=MTIxNjY1NDc0MzM0MzIwNjQ1MA.G2Aalr.B8nqBDPjDTPIE__N6bcqUa8ktrCRG1OeXPj8nE
# DISCORD_GUILD_NAME=TEST
# CLIENT_SECRET=pVo_EeGW4zRAy6qNKDNemZfUYf42xX8m


# client = discord.Client(intents=discord.Intents.default())


class CustomClient(discord.Client):
    
    # @client.event
    async def on_ready(self):
        for guild in client.guilds:
            print(guild)
            if guild.name == GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members} {guild}')
    
    async def on_message_edit(self, before, after):
        print(before.guild, before.content)

        message = f"{before.author} edited his message !!!\nOriginal: {before.content}\nEdited: {after.content}"
        await before.channel.send(message)


    async def on_message(self, message):
        print(message.author)
# @client.event
# async def on_message_edit()
intents = discord.Intents.default()
intents.message_content = True
client = CustomClient(intents=intents)
client.run(TOKEN)