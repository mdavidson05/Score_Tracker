from flask import Blueprint, Flask, redirect, render_template, request

from models.teams import Teams
import repositories.teams_repository as teams_repo
import repositories.game_repository as game_repo
import repositories.league_repository as league_repo

league_bluprint = Blueprint("league", __name__)

# INDEX
@league_bluprint.route("/league")
def league():
    # league = league_repo.select_all()
    ordered_league = league_repo.order()
   
    return render_template("league/index.html", league = ordered_league)


# # NEW
# @league_bluprint.route("/teams/new")
# def new_team():
#     return render_template("teams/new.html")


# # CREATE
# @teams_bluprint.route("/teams", methods=["POST"])
# def create_team():
#     position = request.form["position"]
#     team = request.form["team"]
#     games_played = request.form["games_played"]
#     points = request.form["points"]

    
#     new_team = Teams(position, team, games_played, points, id =None)

#     teams_repo.save(new_team)
#     return redirect("/teams")


# # EDIT
# @teams_bluprint.route("/teams/<id>/edit")
# def edit_team(id):
#     team = teams_repo.select(id)
#     print(team)
#     return render_template('teams/edit.html', team=team)


# # UPDATE
# @teams_bluprint.route("/teams/<id>", methods=["POST"]) #id is being passed as a LIST
# def update_team(id):
#     position = request.form["position"]
#     team = request.form["team"]
#     games_played = request.form["games_played"]
#     points = request.form["points"]


#     teams = Teams(position, team, games_played, points, id)
    
#     teams_repo.update(teams)
#     return redirect("/teams")

# # DELETE
# @teams_bluprint.route("/teams/<id>/delete", methods=["POST"])
# def delete_team(id):
#     teams_repo.delete(id)
#     return redirect("/teams")

# @bitings_blueprint.route("/bitings/<id>", methods=["POST"])
# def update_biting(id):
#     human_id = request.form["human_id"]
#     zombie_id = request.form["zombie_id"]
#     human = human_repository.select(human_id)
#     zombie = zombie_repository.select(zombie_id)
#     biting = Biting(human, zombie, id)
#     biting_repository.update(biting)
#     return redirect("/bitings")