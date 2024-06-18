# FortyTwoAPI
### Python library to facilitate the access of 42's API

```Python
...
from fortytwo import FortyTwoAPI

config = {
    "client_id": "",
    "client_secret": ,
    ""
}
api = FortyTwoAPI(config)

@app.get("/login/")
def login():
    link: str = api.uri()
    return render("login.html", {"authorize_uri": link})

@app.route("/callback/")
def callback():
    return redirect()

@app.get("/dashboard/")
def dashboard()
    data: json = api.getall()
    return render_template("dashboard.html", {"data": data})

```
