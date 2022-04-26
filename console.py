import pdb
from models.games import Games
from models.teams import Teams
from models.league import League

import repositories.game_repository as games_repo
import repositories.teams_repository as teams_repo
import repositories.league_repository as league_repo

teams_repo.delete_all()
games_repo.delete_all()
league_repo.delete_all()

team1 = Teams('Man C', 3, 7)
teams_repo.save(team1)

team2 = Teams("Chelsea", 3, 7)
teams_repo.save(team2)

team3 = Teams("Arsenal", 3, 9)
teams_repo.save(team3)

team4 = Teams('Man U', 3, 6)
teams_repo.save(team4)

game = Games(team1.id, team2.id, 1, 0, "12/12/2022")
games_repo.save(game)

game2 = Games(team3.id, team4.id, 3, 9, "12/12/2022")
games_repo.save(game2)


#for league in leagues
#order = league.points

league1 = League(1, team1.team, team1.games_played, team1.points)
league_repo.save(league1)

league2 = League(2, team2.team, team2.games_played, team2.points)
league_repo.save(league2)

league3 = League(3, team3.team, team3.games_played, team3.points)
league_repo.save(league3)

league4 = League(4, team4.team, team4.games_played, team4.points)
league_repo.save(league4)

league_repo.positions()
#IF ALL ELSE FAILS JUST NUKE IT FROM ORBIT/ ORDER BY POINTS