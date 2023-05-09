from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import csv, os, time, json

m = Mastodon(
        api_base_url=f'https://mastodon.au',
        access_token='xlwor8z4sdp5t5l9D6Vm8DZyDJcP2wFs1oRX4fg35UA')

class Listener(StreamListener):
    def on_update(self, status):
        print(json.dumps(status, indent=2, sort_keys=True, default=str))

m.stream_public(Listener())

