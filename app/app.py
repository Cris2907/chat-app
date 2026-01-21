from flask import (
    Flask,
    abort,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
    send_from_directory,
)
import os

app = Flask(__name__)

PUBLIC_REACT_DEV_SERVER = "http://localhost:5173"


def serve_public_spa():

    vite_path = request.path
    # We want to go one folder up, to the parent
    
    vite_path = os.path.dirname(request.path)
    if vite_path.startswith("/frontend"):
        vite_path = vite_path.replace("/public-react", "") or "/"
    vite_url = f"{PUBLIC_REACT_DEV_SERVER}{vite_path or '/'}"
    return redirect(vite_url)



@app.route("/")
def home():
    # Redirect the user to the Vite development server
    return redirect("http://localhost:5173")