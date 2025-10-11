import uuid
import re
from functools import wraps

# Initialize Flask
from flask import Flask, render_template, request, redirect, make_response
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
bcrypt = Bcrypt(app)

# Initialize Database if doesn't already exist
from db import *
for model in [ItemModel, PlayerModel, InventoryModel, ExperienceModel]:
    if not db.table_exists(model):
        model.create_table()

# Initialize Game
from game import Game
from player import Player
game = Game()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        player = authentication_check(request)
        if not player:
            return redirect('/login',code=302)
        return f(player, *args, **kwargs)

    return decorated_function

def authentication_check(request):
    session_token = request.cookies.get('session')

    # Challenge 1. Check session token exists.
    if not Player.session_exists(session_token):
        return False

    # Challenge 2. Check token hasn't expired.
    player = Player(session_token=session_token)
    if player._record.session_expiration < datetime.datetime.now():
        return False

    return player

# ROUTES - ACCESS

@app.route("/login", methods=["GET", "POST"])
def login():
    match request.method:
        case 'GET':
            return render_template("access/login.html")
        case 'POST':
            username = request.form.get("username").lower()
            password = request.form.get("password")

            # Challenge 1. Check player exists.
            if not Player.username_exists(username):
                return render_template("access/login.html", error="Invalid username or password.")

            # Challenge 2. Check password is correct.
            r = Player(username=username)._record
            if not bcrypt.check_password_hash(r.password, password):
                return render_template("access/login.html", error="Invalid username or password.")

            r.session_token = str(uuid.uuid4())
            r.session_expiration = datetime.datetime.now()+datetime.timedelta(days=30)
            r.save()

            response = make_response(redirect('/'))
            response.set_cookie('session', r.session_token, expires=r.session_expiration)
 
            return response

@app.route("/logout")
def logout():
    player = authentication_check(request)

    r = player._record
    r.session_expiration = datetime.datetime(year=1970, month=1, day=1)
    r.save()

    return redirect("/")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    match request.method:
        case 'GET':
            return render_template("access/signup.html")
        case 'POST':
            username = request.form.get("username").lower()
            password = request.form.get("password")

            # Challenge 1. Check username isn't taken.
            if Player.username_exists(username):
                return render_template("access/signup.html", error=f"Sorry, the username <b>{username}</b> is taken.")

            # Challenge 2. Check no spaces in username.
            if ' ' in username:
                return render_template("access/signup.html", error=f"You can't put spaces in your username.")

            # Challenge 3. Check password meets requirements.
            if len(password) < 8:
                return render_template("access/signup.html", error="Password must be 8+ characters.")

            password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
            session_token = str(uuid.uuid4())
            session_expiration = datetime.datetime.now()+datetime.timedelta(days=30)

            player = Player(
                username=username, 
                password=password_hash, 
                session_token=session_token,
                session_expiration=session_expiration
            )

            response = make_response(redirect('/'))
            response.set_cookie('session', session_token, expires=session_expiration)
 
            return response

@app.route("/")
@login_required
def home(player):
    return render_template("access/home.html", player=player, game=game)

# ROUTES - PLAYER
#   /player
#   /player/skills/<skill>
#   /player/journal/<skill>
#   /player/inventory

@app.route('/player')
@login_required
def player(player):
    return render_template('/player/player.html', player=player, game=game)

@app.route('/player/skills/<skill>')
@login_required
def skill(player, skill):
    return render_template('/player/skill.html', player=player, game=game, skill=skill)

@app.route('/player/journal/<chapter>')
@login_required
def journal(player, chapter):
    return render_template('/player/journal.html', player=player, game=game, chapter=chapter)

@app.route('/player/backpack')
@login_required
def backpack(player):
    return render_template('/player/backpack.html', player=player, game=game)

# ROUTES - ITEMS
# /item/<item>
@app.route('/item/<item>')
@login_required
def item(player, item):
    return render_template('/access/item.html', player=player, game=game, item=game.items.get(item))

# ROUTES - LOCATIONS
#   /locations
#   /locations/<skill>
#   /locations/<skill>/<location>
#   /locations/<skill>/<location>/<action>


# FORMATTERS
@app.template_filter()
def snake_case(s):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower().replace(' ', '')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
