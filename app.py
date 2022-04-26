from flask import Flask, render_template

from controllers.games_controller import games_blueprint

from controllers.teams_controller import teams_bluprint

from controllers.league_controller import league_bluprint

from controllers.players_controller import players_bluprint

app = Flask(__name__)

app.register_blueprint(games_blueprint)
app.register_blueprint(teams_bluprint)
app.register_blueprint(league_bluprint)
app.register_blueprint(players_bluprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)