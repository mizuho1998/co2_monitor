
import json
import urllib.request

def post_slack(url, message):
    headers = {
        'Content-Type': 'application/json',
    }

    req = urllib.request.Request(url, json.dumps(message).encode(), headers)
    try:
        with urllib.request.urlopen(req) as res:
            return res.status, res.reason

    except Exception as e:
        return -1, "error"


if __name__ == '__main__':
    # test
    import settings
    import os

    settings.init()
    url = os.environ.get("SLACK_URL") 
    message = {
        'text': 'hello',
    }
    post_slack(url, message)
