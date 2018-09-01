# Dosukoi
from github_webhook import Webhook
from flask import Flask
import subprocess

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    print("Got push with: {0}".format(data))
    try:
      res = subprocess.call('git pull ; git checkout -f infra ; docker-compose up -d')
    except Exception as e:
      print(e)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)