from flask import Flask, redirect, render_template, request, url_for
import git

app = Flask(__name__)
app.config["DEBUG"] = True

comments = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))

# Webhook link to GitHub
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
