from src.fortytwo import FortyTwoAPI
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

# initialize
api = FortyTwoAPI(
    redirect=os.getenv("AUTHORIZE_URL"),
    uid=os.getenv("CLIENT_ID"),
    secret=os.getenv("CLIENT_SECRET"),
    callback=os.getenv("CALLBACK_URL")
)

@app.get("/")
def home():
    # go to authorization URL
    url: str = api.authorization_url
    return render_template("index.html",  url=url)

@app.route("/callback/")
def callback():
    code = request.args.get('code')
    # exchange code for access token, 
    data = api.get_data(code)
    return data

@app.get("/dashboard/")
def dashboard():
    pass

