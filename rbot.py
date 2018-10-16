import praw
from config.auth import RedditBot

reddit = praw.Reddit(client_id=RedditBot.client_id,
                     client_secret=RedditBot.client_secret,
                     user_agent=RedditBot.user_agent,
                     username=RedditBot.username,
                     password=RedditBot.password)
