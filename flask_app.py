
# A very simple Flask Hello World app for you to get started with...

<<<<<<< HEAD
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)
app.config["DEBUG"] = True
comments = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))


=======
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
>>>>>>> 7a142734abae71e262233fdeb488b19bece722d2
