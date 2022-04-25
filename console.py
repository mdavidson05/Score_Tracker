import pdb
from models.games import Games
from models.teams import Teams

import repositories.game_repository as games_repo
import repositories.teams_repository as teams_repo

teams_repo.delete_all()
games_repo.delete_all()

team1 = Teams(2,'Man U', 3, 7)
teams_repo.save(team1)

team2 = Teams(3, "Chelsea", 3, 7)
teams_repo.save(team2)

game = Games(team1.id, team2.id, "Draw", "12/12/2022")
games_repo.save(game)
