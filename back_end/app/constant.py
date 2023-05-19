from enum import Enum

class DB_Name(Enum):
    TWITTER = "twitter"
    MASTODON = "mastodon"
    SUDO1 = "sudo"
    SUDO2 = "sa2"

class TwitterDataType(Enum):
    STATE = "state"
    RELATED_TWEETS = "related-tweets"

class MastodonDataType(Enum):
    RELATED_TOOTS = "related-toots"
    RELATED_USERS = "related-users"