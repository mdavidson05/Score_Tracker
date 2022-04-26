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


# def order():
#     sql = "SELECT * from league ORDER BY points DESC"
#     result = run_sql(sql)
#     return result
# #RETURN ORDERED BY POINTS

def update(player):
    sql = "UPDATE players SET (name, appearances, goals, assists, yellow_cards, red_cards, MoM) = (%s, %s, %s,%s, %s, %s, %s) WHERE id = %s"
    # print(team)

    # update_position(team) 

    values = [player.name, player.appearances, player.goals, player.assists, player.yellow_cards, player.red_cards, player.MoM]

    run_sql(sql, values)

# def update_league(league):
#     sql = "UPDATE league SET (position, team, games_played, points) = (%s, %s, %s, %s) WHERE id = %s"

#     values = [league.position, league.team, league.games_played, league.points]

#     run_sql(sql, values)
#     # return result

# def positions():
#     teams = []
#     data = order()
#     position = 1
#     for dat in data:
#         #as we're passing in an ordred list and not a list of object we have to use list indices to extract the relevant data from the ordered list to create our new instance of the Teams class
#         league = League(position, dat[2], dat[3], dat[4])
#         update_league(league)
#         teams.append(league)
#         position += 1
#     return teams



# def update_position(team):
#     teams = teams_repo.select_all()
#     positions = []
#     for position in teams:
#         teams += position.points
    
    
    #for each object in teams find points
    #if  team1.points > team2.points
    #update team1 & team2 position

    
