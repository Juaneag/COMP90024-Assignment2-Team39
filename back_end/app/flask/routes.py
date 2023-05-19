from app.core import fetch_data
from app.constant import DB_Name, TwitterDataType, MastodonDataType

def healthcheck():
    return { "message" : "OK!" }

def data_home_and_community_care():
    return fetch_data(DB_Name.HOME_AND_COMMUNITY_CARE)

def data_voluntary_work():
    return fetch_data(DB_Name.VOLUNTARY_WORK)

def data_unpaid_assistance():
    return fetch_data(DB_Name.UNPAID_ASSISTANCE)

def data_twitter_related_tweets():
    return fetch_data(DB_Name.TWITTER, TwitterDataType.RELATED_TWEETS)

def data_twitter_unrelated_tweets():
    return fetch_data(DB_Name.TWITTER, TwitterDataType.UNRELATED_TWEETS)

def data_mastodon_toots():
    return fetch_data(DB_Name.MASTODON, MastodonDataType.RELATED_TOOTS)

def data_mastodon_users():
    return fetch_data(DB_Name.MASTODON, MastodonDataType.RELATED_USERS)