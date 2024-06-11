import discord
import requests
from discord.ext import commands
from discord_token import my_token

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)


def get_friend_list(key, steamid):
    link =  f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={key}&steamid={steamid}&relationship=friend"
    response = requests.get(url=link)
    return  response.json()


def get_player_summaries(key, steamid):
    link = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={steamid}"
    response = requests.get(url=link)
    return response.json()


def get_player_achieve(key, steamid, appid):
    link = f"http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={appid}&key={key}&steamid={steamid}"
    response = requests.get(url=link)
    return response.json()


def get_player_recently_games(key, steamid, count):
    link = f"http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key={key}&steamid={steamid}&count={count}&format=json"
    response = requests.get(url=link)
    return response.json()

def get_player_

@bot.command()
async def friends(ctx, key, steamid):
    data = get_friend_list(key, steamid)
    for friend in data["friendslist"]["friends"]:
        await ctx.send(friend["steamid"])


@bot.command()
async def summaries(ctx, key, steamid):
    data = get_player_summaries(key, steamid)
    player = data["response"]["players"]
    name = player[0]["personaname"]
    steam_id = player[0]["steamid"]
    info = f"""
    name: {name}
    steamid: {steam_id}"""
    embed = discord.Embed(title="Player Summaries",
                          url="https://realdrewdata.medium.com/",
                          description=info, color=0xFF5733)
    await ctx.send(embed=embed)


@bot.command()
async def achieve(ctx, key, steamid, appid):
    data = get_player_achieve(key, steamid, appid)


bot.run(token=my_token)