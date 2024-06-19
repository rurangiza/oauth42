from src.oauth42 import Oauth42, Token

from flask import (
    Flask, 
    request, session,
    render_template, redirect, url_for
)
from secrets import token_hex

from dotenv import load_dotenv
from os import getenv
load_dotenv()


app = Flask(__name__)
app.secret_key = token_hex() # session needs this


UID = getenv("CLIENT_ID")
SECRET = getenv("CLIENT_SECRET")
REDIRECT = getenv("REDIRECT_URI")

# store info which will help get both the authorization_uri and access token
client = Oauth42(UID, SECRET, REDIRECT)


@app.get("/")
def home():
    """
    Page to redirect to the authorization page
    """
    # 1. generate authorization URL (authorization_endpoint)
    url: str = client.auth_url
    return render_template("index.html",  url=url)


@app.route("/callback/")
def callback():
    """
    Exchange authorization code with access token
    Then stores is in session
    """
    authorization_code = request.args.get('code')
    if request.args.get('state') != client.state:
        return
    
    # 2. exchange authorization code for access token
    token: str = client.get_token(authorization_code)
    # 3. store the token in a session
    session['token'] = token
    
    return redirect(url_for("dashboard"))


@app.get("/dashboard/")
def dashboard():
    """
    At this point, you have the access token so you can send
    requests to access the user's data on Intra 42
    """
    token = Token(session.get('token'))
    data = token.get("/v2/me")

    context = {
        "name": f'{data.get("first_name")} {data.get("last_name")}',
        "email": data.get("email"),
        "image": data.get("image").get("link"),
        "data": data
    }

    return render_template("dashboard.html", context=context)
