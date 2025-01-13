import discord, datetime
from discord import app_commands
from config import Config


class UilStudio(discord.Client):
    async def on_ready(self):
        await self.wait_until_ready()
        await app.sync()
        print(f"{self.user} 계정에 로그인했습니다.")


client = UilStudio(intents=discord.Intents.all())
app = app_commands.CommandTree(client)


@client.event
async def on_member_join(self, member):
    joined_at = member.joined_at.strftime("%Y년 %m월 %d일 %p %I:%M")
    await self.client.get_guild(Config.guild_id).get_channel(Config.join_channel_id).send(
        embed = discord.Embed(title=f"{member.name}님이 서버에 입장하셨습니다.", color=0x3c9bff)
        .set_thumbnail(url=member.avatar.url)
        .add_field(name="**유저**", value=f"**{member.mention} ({member.name})**", inline=False)
        .set_footer(text=joined_at)
    )

@client.event
async def on_member_remove(self, member):
    leave_at = datetime.datetime.now().strftime("%Y년 %m월 %d일 %p %I:%M")
    await self.client.get_guild(Config.guild_id).get_channel(Config.join_channel_id).send(
        embed = discord.Embed(title=f"{member.name}님이 서버에 입장하셨습니다.", color=0x3c9bff)
        .set_thumbnail(url=member.avatar.url)
        .add_field(name="**유저**", value=f"**{member.mention} ({member.name})**", inline=False)
        .set_footer(text=leave_at)
    )

client.run(Config.bot_token)