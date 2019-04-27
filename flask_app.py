
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, this is a basic message.'

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('./myproject')
        origin = repo.remotes.origin
        repo.create_head('master',
        origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
        origin.pull()
        return '', 200
    else:
        return '', 400