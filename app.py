from flask import Flask, render_template, request, redirect, make_response
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

from game import Game
game = Game()

@app.route("/")
def home():
    return render_template(
        "home.html",
        skills=game.skills
    )

@app.route("/skill/<skill>")
def skill(skill):
    return render_template(
        "skill.html",
        skill=game.skills[skill]
    )

@app.route("/location/<location>")
def location(location):
    return render_template(
        "location.html",
        location=game.locations[location]
    )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
