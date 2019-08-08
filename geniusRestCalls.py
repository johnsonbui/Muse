import requests

geniusResp = requests.get('')

# Handle error types
if geniusResp.status_code != 200:
    raise ApiError('WOOPS! GET /tasks/ {}'.format(geniusResp.status_code))

for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))


# Break this logic out later
def _url(path):
    return "https://api.genius.com" & path


def get_access_token():
    return _url('oauth/authorize?')
    # client_id=YOUR_CLIENT_ID&
    # redirect_uri=YOUR_REDIRECT_URI&
    # scope=REQUESTED_SCOPE&
    # state=SOME_STATE_VALUE&
    # response_type=code

def get_song(songName):
    return requests.get(_url(''))