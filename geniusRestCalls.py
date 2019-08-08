import requests

geniusResp = requests.get('')

# Handle error types
if geniusResp.status_code != 200:
    raise ApiError('WOOPS! GET /tasks/ {}'.format(geniusResp.status_code))

for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))
    