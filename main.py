import tweepy
import os
import dotenv
import datetime
import calendar
import math
import time
dotenv.load_dotenv()

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_secret = os.getenv('ACCESS_SECRET')

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def get_percent():
    total_days = 0
    cursor = 1
    while cursor < datetime.datetime.now().month:
        total_days += calendar.monthrange(datetime.datetime.now().year, cursor)[1]
        cursor += 1
    total_days += datetime.datetime.now().day
    return math.floor(round(100 * total_days / 365, 1))


print(f'{get_percent()}%')