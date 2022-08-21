import os
import math
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

def isset(dict, key):
    try:
        tmp = dict[key]
        return True
    except:
        return False

def send(data):
    webhook = DiscordWebhook(url=os.getenv("DISCORD_WEBHOOK_URL"))
    embed = DiscordEmbed(title=data["name"], description=os.getenv("TARGET_REPO_NAME"), color="cc99ff")
    embed.set_footer(text=data["published_at"])
    embed.set_author(name=data["author"]["login"], url=data["author"]["html_url"], icon_url=data["author"]["avatar_url"])
    for value in data["assets"]:
        embed.add_embed_field(name=value["name"], value=f"DL: {value['download_count']} / Size: {math.floor((int(value['size'])/1024/1024) * 10 ** 1)/(10 ** 1)}MB", inline=False)
    webhook.add_embed(embed)
    response = webhook.execute()
    return response

if os.getenv("DISCORD_WEBHOOK_URL") is None:
    print("Error: Webhook URL not found")
    exit

if os.getenv("TARGET_REPO_NAME") is None:
    print("Error: Repo Name not found")
    exit

gh_response = requests.get(f"https://api.github.com/repos/{os.getenv('TARGET_REPO_NAME')}/releases/latest", headers={"Accept": "application/vnd.github.v3+json"}).json();

if not isset(gh_response, "assets"):
    print(f"Response Error: {gh_response['message']}")
    exit

response = send(gh_response)
print(response)