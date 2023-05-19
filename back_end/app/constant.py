from enum import Enum

class DB_Name(Enum):
    TWITTER = "twitter"
    MASTODON = "mastodon"
    HOME_AND_COMMUNITY_CARE = "sudo"
    VOLUNTARY_WORK = "sa2"
    UNPAID_ASSISTANCE = "unpaid"

class TwitterDataType(Enum):
    RELATED_TWEETS = "related-tweets"
    UNRELATED_TWEETS = "unrelated-tweets"

class MastodonDataType(Enum):
    RELATED_TOOTS = "related-toots"
    RELATED_USERS = "related-users"