from flask import Blueprint, Flask, redirect, render_template, request

from models.teams import Teams
import repositories.teams_repository as teams_repo
import repositories.game_repository as game_repo
import repositories.league_repository as league_repo

league_bluprint = Blueprint("league", __name__)

# INDEX
@league_bluprint.route("/league")
def league():
    # ordered_league = league_repo.order()
    league = league_repo.positions()
    # league_repo.update_league(league)

   
    return render_template("league/index.html", league = league)
