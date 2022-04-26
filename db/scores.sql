DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS league;
DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    -- position INT,
    team VARCHAR(100),
    games_played INT,
    points INT
    );

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    home_team int REFERENCES teams(id) ON DELETE CASCADE,
    away_team int REFERENCES teams(id) ON DELETE CASCADE,
    home_goals INT,
    away_goals INT,
    date DATE
    
);

CREATE TABLE league (
    id SERIAL PRIMARY KEY,
    position INT,
    team VARCHAR(100),
    -- goals for,
    -- goals against,
    -- won
    --lost
    -- drawn
    --goal difference
    games_played INT,
    points INT

);

CREATE TABLE players (
    id serial PRIMARY KEY,
    name VARCHAR(100),
    appearances int,
    goals int,
    assists int,
    yellow_cards int,
    red_cards int,
    MoM int,
    team INT REFERENCES teams(id) ON DELETE CASCADE


)

-- CREATE TABLE players
-- sql = "SELECT * FROM customers ORDER BY name"

-- SIMULATE MATCHES

-- teams to games inner join table with game team id

-- each team will belong to a club make a club table
-- club id