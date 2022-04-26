from db.run_sql import run_sql
from models.games import Games
import repositories.game_repository as game_repo
import repositories.teams_repository as teams_repo
from models.league import League


def save(league):
    sql = "INSERT INTO league (position, team, games_played, points) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [league.position, league.team, league.games_played, league.points]
    results = run_sql(sql, values)
    print(results)
    id = results[0]['id']
    league.id = id

def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)

def select_all():
    league = []
    sql = "SELECT * FROM league"
    results = run_sql(sql)
    for result in results:
        teams = League(result["position"], result["team"], result["games_played"], result["points"])
        league.append(teams)
    return league


def order():
    sql = "SELECT * from league ORDER BY position ASC"
    result = run_sql(sql)
    return result
    