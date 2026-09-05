import requests


class MALClient:

    BASE_URL = "https://api.myanimelist.net/v2"

    def __init__(self, api_key):
        self.headers = {"X-MAL-CLIENT-ID": api_key}

    def get_user_anime_list(self, username):
        url = f"{self.BASE_URL}/users/" f"{username}/animelist"

        params = {"offset": 0, "fields": "list_status"}

        response = requests.get(url, headers=self.headers, params=params, timeout=60)

        return response.json()
