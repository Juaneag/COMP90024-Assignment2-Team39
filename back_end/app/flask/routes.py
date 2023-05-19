from app.core import fetch_data
from app.constant import DB_Name, TwitterDataType, MastodonDataType

def healthcheck():
    return { "message" : "OK!" }

def sudo1():
    data = fetch_data(DB_Name.SUDO1)
    return { "data": data }

def sudo2():
    data = fetch_data(DB_Name.SUDO2)
    return { "data": data }

def twitter_state():
    data = fetch_data(DB_Name.TWITTER, TwitterDataType.STATE)
    return data

def twitter_tweets():
    data = fetch_data(DB_Name.TWITTER, TwitterDataType.RELATED_TWEETS)
    return data

def mastodon_toots():
    data = fetch_data(DB_Name.MASTODON, MastodonDataType.RELATED_TOOTS)
    return data

def mastodon_users():
    data = fetch_data(DB_Name.MASTODON, MastodonDataType.RELATED_USERS)
    return data