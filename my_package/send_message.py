# my_package/send_message.py

import requests

class ServerClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def send_message(self, message):
        try:
            response = requests.post(self.endpoint, json={'message': message})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
iCx8*ZC4TPMs4tv