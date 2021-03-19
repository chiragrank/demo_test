import os
import json
from flask import Flask, request
from flask_cors import CORS
from firebase_admin import db, credentials, initialize_app


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "this is a demo app"
CORS(app)


## Please make sure to set the environment variable.
cred = credentials.Certificate(
    os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))
initialize_app(cred, {"databaseURL": os.environ.get("FIREBASE_URL")})
ref = db.reference("/")


@app.route("/save_data", methods=["Post"])
def save_data():
    user_data = request.get_json()
    ref.child("DEMO_TEST").push().set(user_data) # "DEMO_TEST" is optional and can be replaced with dynamic based on the request if required
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


if __name__ == '__main__':
    app.secret_key = "this is a demo app"
    app.run()