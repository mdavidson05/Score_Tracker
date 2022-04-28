from db.run_sql import run_sql
from models.games import Games
import repositories.game_repository as game_repo
import repositories.teams_repository as teams_repo
from models.league import League
from models.players import Players


def save(player):
    sql = "INSERT INTO players (name, appearances, goals, assists, yellow_cards, red_cards, MoM) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [player.name, player.appearances, player.goals, player.assist, player.yellow_cards, player.red_cards, player.MoM]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id


def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)

def select_all():
    players = []
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for result in results:
        player = Players(result["name"], result["appearances"], result["goals"], result["assists"], result["yellow_cards"], result["red_cards"], result["mom"])
        players.append(player)
    return players

def update(player):
    sql = "UPDATE players SET (name, appearances, goals, assists, yellow_cards, red_cards, MoM) = (%s, %s, %s,%s, %s, %s, %s) WHERE id = %s"
    # print(team)

    # update_position(team) 

    values = [player.name, player.appearances, player.goals, player.assists, player.yellow_cards, player.red_cards, player.MoM]

    run_sql(sql, values)



    
