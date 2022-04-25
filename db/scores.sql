
DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    position INT,
    team VARCHAR(100),
    games_played INT,
    points INT
    
   
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    home_team int REFERENCES teams(id) ON DELETE CASCADE,
    away_team int REFERENCES teams(id) ON DELETE CASCADE,
    result VARCHAR(100),
    date DATE
    
);

-- teams to games inner join table with game team id

-- each team will belong to a club make a club table
 -- club id