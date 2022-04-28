from db.run_sql import run_sql
from models.games import Games
import repositories.game_repository as game_repo
import repositories.teams_repository as teams_repo


def save(game):
    sql = "INSERT INTO games (home_team, away_team, home_goals, away_goals, date) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [game.home, game.away, game.home_goals, game.away_goals, game.date]
    results = run_sql(sql, values)
    # print(results)
    id = results[0]['id']
    game.id = id


def select_all():
    games = []
    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for result in results:
        # game = game_repo.select(result["id"])
        home_team = teams_repo.select(result["home_team"])
        away_team = teams_repo.select(result["away_team"])

        game_select = Games(home_team, away_team, result["home_goals"], result["away_goals"], result["date"], result["id"])
        games.append(game_select)
    return games


def select(id):
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    game = Games(result["home_team"], result["away_team"], result["home_goals"], result["away_goals"], result["date"], result["id"])
    # print(game)
    return game


def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM games WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(game):
    sql = "UPDATE games SET (home_team, away_team, home_goals, away_goals, date) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [game.home, game.away, game.home_goals, game.away_goals, game.date, game.id]
    # print(values)
    run_sql(sql, values)

