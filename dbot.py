import discord
from discord.ext import commands
from logger import get_logger
from config.auth import DiscordBot
from config.auth import RedditBot
import rbot

description = '''Discord Reddit Submission bot'''
bot = commands.Bot(command_prefix=DiscordBot.Prefix, description=description)

@bot.event
async def on_ready():
    logger.info('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
    await bot.change_presence(game=Game(name=DiscordBot.Game))

    subreddit = rbot.reddit.subreddit(RedditBot.subreddit)
    logger.info('Reddit Connection:\nTitle: {0.display_name}\nTitle: {0.title}\nDescription: {0.description}'.format(subreddit))

@bot.command()
async def submit(ctx):
    """submits link to reddit"""
    # TODO: Submission Matrix

bot.run(DiscordBot.Token)
