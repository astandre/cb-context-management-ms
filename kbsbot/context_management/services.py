from requests import Session
import requests
import os

CHANNEL_HANDLER = os.environ.get('CHANNEL_HANDLER')
# CHANNEL_HANDLER = "http://127.0.0.1:5005"

session = Session()
session.trust_env = False
session.verify = False
session.headers["Accept"] = "application/json"
session.headers["Content-Type"] = "application/json"


def get_last_thread(user):
    """
    This methods retrieves users last conversation thread

    Args:
            :param  user: id of the user to be retrieved.

    """
    url = CHANNEL_HANDLER + "/thread/last"
    try:
        r = session.get(url, json={"user": user})
        if r.status_code == 200:
            response = r.json()
            return response
    except requests.exceptions.RequestException as e:
        print(e)
