from flask import Blueprint, Flask, redirect, render_template, request

from models.teams import Teams
import repositories.teams_repository as teams_repo
import repositories.game_repository as game_repo
import repositories.league_repository as league_repo
import repositories.players_repository as player_repo

players_bluprint = Blueprint("players", __name__)

# INDEX
@players_bluprint.route("/players")
def players():
    # ordered_league = league_repo.order()
    # league = league_repo.positions()
    # league_repo.update_league(league)
    players = player_repo.select_all()
    print(players)

   
    return render_template("players/index.html", players = players)
