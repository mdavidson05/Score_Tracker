from flask import Blueprint, Flask, redirect, render_template, request

from models.games import Games
import repositories.game_repository as game_repo
import repositories.teams_repository as team_repo
import repositories.league_repository as league_repo

games_blueprint = Blueprint("games", __name__)

# INDEX
@games_blueprint.route("/games")
def games():
    games = game_repo.select_all()
    teams = team_repo.select_all()
    return render_template("games/index.html", games=games, teams = teams)


# NEW
@games_blueprint.route("/games/new")
def new_team():
    teams = team_repo.select_all()
    return render_template("games/new.html", teams = teams)


# CREATE
@games_blueprint.route("/games", methods=["POST"])
def create_game():
    home_team_id = request.form["home"]
    home_team = team_repo.select(home_team_id)
    # print(home_team)
    away_team_id = request.form["away"]
    away_team = team_repo.select(away_team_id)
    # print(away_team)
    home_goals = request.form["home_goals"]
    away_goals = request.form["away_goals"]

    date = request.form["date"]

    new_game = Games(home_team.id, away_team.id, home_goals, away_goals, date, id = None)

    # print(new_game)
    # league_repo.save(new_game)
    game_repo.save(new_game)
    return redirect("/games")


# EDIT
@games_blueprint.route("/games/<id>/edit")
def edit_game(id):
    games = game_repo.select(id)
    teams = team_repo.select_all()
    # print(games)
    return render_template('games/edit.html', games=games, teams = teams)


# UPDATE
@games_blueprint.route("/games/<id>", methods=["POST"])
def update_game(id):
    home_team_id = request.form["home"]
    # print(home_team.__dict__)

    away_team_id = request.form["away"]
    # away_team = team_repo.select(id)
 
    home_goals = request.form["home_goals"]
    away_goals = request.form["away_goals"]

    date = request.form["date"]

    games = Games(home_team_id, away_team_id, home_goals, away_goals, date, id)

    game_repo.update(games)
    return redirect("/games")


# DELETE
@games_blueprint.route("/games/<id>/delete", methods=["POST"])
def delete_team(id):
    game_repo.delete(id)
    return redirect("/games")

