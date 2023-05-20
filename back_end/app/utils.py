from app.constant import DB_Name, TwitterDataType, MastodonDataType

def get_doc_name_and_view_from_type(db_name, type):
    result = {
        DB_Name.TWITTER: {
            TwitterDataType.RELATED_TWEETS: [ "state", "state_view" ],
            TwitterDataType.UNRELATED_TWEETS: [ "state", "new-state" ]
        },
        DB_Name.MASTODON: {
            MastodonDataType.RELATED_TOOTS: [ "count", "relatetoot" ],
            MastodonDataType.RELATED_USERS: [ "count", "relateusr" ]
        }
    }
    
    return result[db_name][type]