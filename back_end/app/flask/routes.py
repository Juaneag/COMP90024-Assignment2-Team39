from app.core import fetch_data
from app.constant import DB_Name, TwitterDataType, MastodonDataType

def healthcheck():
    return { "message" : "OK!" }

def sudo1():
    return fetch_data(DB_Name.SUDO1)

def sudo2():
    return fetch_data(DB_Name.SUDO2)

def twitter_state():
    return fetch_data(DB_Name.TWITTER, TwitterDataType.STATE)

def twitter_tweets():
    return fetch_data(DB_Name.TWITTER, TwitterDataType.RELATED_TWEETS)

def mastodon_toots():
    return fetch_data(DB_Name.MASTODON, MastodonDataType.RELATED_TOOTS)

def mastodon_users():
    return fetch_data(DB_Name.MASTODON, MastodonDataType.RELATED_USERS)