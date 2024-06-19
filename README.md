# Oauth 42
### Python Oauth2 wrapper for 42's API

```Python
...
from oauth42 import Oauth42, Token

"""
Initialize the Oauth42 object for later use:
>> UID: the CLIENT_ID from 42's intra
>> SECRET: the CLIENT_SECRET from 42's intra
>> REDIRECT_URI: where to be redirected after authorization
"""
client = Oauth42(UID, SECRET, REDIRECT_URI)


"""
Generate the authorization URL, where to send students so they
login and give limited access to their data
"""
authorization_url: str = client.auth_url


"""
In the view corresponding to your REDIRECT_URI
You'll receive a code as a query parameter, which can be
exchanged for an access token
>> param: authorization_code
"""
access_token: str = client.get_token(authorization_code)
# store in session

"""
The Token() will later facilitate api calls, by giving access
to the token.get() method
>> param: access_token
"""
# retrieve access token from session
token = Token(access_token)


"""
The token.get() method allows to send GET requests to endpoints
using the access token
>> param: endpoint
"""
student_data: json = token.get("/v2/me")

student_data.get("first_name")
student_data.get("email")
student_data.get("image").get("link")
...

```

### Useful Links
- [Introduction to Oauth2](https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2)
- [42 Web Application Flow](https://api.intra.42.fr/apidoc/guides/web_application_flow)
- [42 Endpoints](https://api.intra.42.fr/apidoc)
- [Oauth2 RFC](https://datatracker.ietf.org/doc/html/rfc6749)
