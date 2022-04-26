from db.run_sql import run_sql
from models.teams import Teams
import repositories.teams_repository as teams_repo


def save(team):
    sql = "INSERT INTO teams (team, games_played, points) VALUES (%s, %s, %s) RETURNING id"
    values = [team.team, team.games_played, team.points]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id


def select_all():
    teams = []
    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for result in results:
        team_select = Teams(result["team"], result["games_played"], result["points"], result["id"])
        teams.append(team_select)
    return teams


def select(id):
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    team = Teams(result["team"], result["games_played"], result["points"], result["id"])
    return team


def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(team):
    sql = "UPDATE teams SET (team, games_played, points) = (%s, %s, %s) WHERE id = %s"
    # print(team)

    values = [team.team, team.games_played, team.points, team.id]

    run_sql(sql, values)
    
