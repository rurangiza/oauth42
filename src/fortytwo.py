"""
Official Documentation:
https://api.intra.42.fr/apidoc/guides/getting_started
"""


import requests
import uuid


class FortyTwoAPI:
    def __init__(self, redirect: str, uid: str, secret: str, callback: str):
        self.authorize_url: str = redirect
        self.token_url: str = "https://api.intra.42.fr/oauth/token"
        self.api_url: str = "https://api.intra.42.fr/v2/me"
        self.callback_url: str = callback

        self.code: str = None
        self.access_token: str = None

        self.client_id: str = uid # uid
        self.client_secret: str = secret

        self.redirect_uri: str = ""
        self.scope: str = "public"
        self.state: str = str(uuid.uuid4())
        self.response_type: str = "code"
        self.__token_aquired = False


    @property
    def authorization_url(self) -> str:
        """ URL to where to send user for authentication """
        return f"\
        {self.authorize_url}\
        client_id={self.client_id}\
        &redirect_uri={self.callback_url}\
        &scope={self.scope}\
        &response_type=code\
        &state={self.state}"


    def exchange_code_for_token(self, code) -> str:
        """ exchange temporary code for access token """
        parameters = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code,
            'redirect_uri': self.callback_url
        }
        response = requests.post(self.token_url, data=parameters)
        if response.status_code == 200:
            token_data = response.json()
            return token_data.get('access_token')
        else:
            return None


    def get_data(self):
        """ Make a request to the provider's API to get user information """
        if not self.access_token:
            self.access_token = self.exchange_code_for_token()
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = requests.get(self.api_url, headers=headers)

        if response.status_code == 200:
            user_data = response.json()
            return user_data
        else:
            return None
