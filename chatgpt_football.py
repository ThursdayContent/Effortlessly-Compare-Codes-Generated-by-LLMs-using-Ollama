import pandas as pd

# Your JSON data
data = [
  {
      "matches": [
        {
          "home_team": {
            "name": "Arsenal",
            "goals": 3
          },
          "away_team": {
            "name": "Tottenham Hotspur",
            "goals": 1
          },
          "date": "2023-10-24",
          "venue": "Emirates Stadium",
          "metrics": {
            "possession": {
              "home_team": 60,
              "away_team": 40
            },
            "shots": {
              "home_team": 15,
              "away_team": 10
            },
            "corners": {
              "home_team": 6,
              "away_team": 3
            },
            "yellow_cards": {
              "home_team": 1,
              "away_team": 2
            },
            "red_cards": {
              "home_team": 0,
              "away_team": 0
            }
          }
        },
        {
          "home_team": {
            "name": "Liverpool",
            "goals": 2
          },
          "away_team": {
            "name": "Manchester City",
            "goals": 2
          },
          "date": "2023-10-22",
          "venue": "Anfield",
          "metrics": {
            "possession": {
              "home_team": 50,
              "away_team": 50
            },
            "shots": {
              "home_team": 12,
              "away_team": 11
            },
            "corners": {
              "home_team": 5,
              "away_team": 4
            },
            "yellow_cards": {
              "home_team": 2,
              "away_team": 1
            },
            "red_cards": {
              "home_team": 0,
              "away_team": 0
            }
          }
        },
       {
      "home_team": {
        "name": "Arsenal",
        "goals": 3,
        "players": [
          {
            "name": "Bukayo Saka",
            "goals": 1,
            "assists": 1
          },
          {
            "name": "Gabriel Martinelli",
            "goals": 2
          }
        ]
      },
      "away_team": {
        "name": "Tottenham Hotspur",
        "goals": 1,
        "players": [
          {
            "name": "Harry Kane",
            "goals": 1
          }
        ]
      },
      "date": "2023-10-24",
      "venue": "Emirates Stadium",
      "metrics": {
        "possession": {
          "home_team": 60,
          "away_team": 40
        },
        "shots": {
          "home_team": 15,
          "away_team": 10
        },
        "corners": {
          "home_team": 6,
          "away_team": 3
        },
        "yellow_cards": {
          "home_team": 1,
          "away_team": 2
        },
        "red_cards": {
          "home_team": 0,
          "away_team": 0
        }
      }
    },
    {
      "home_team": {
        "name": "Liverpool",
        "goals": 2,
        "players": [
          {
            "name": "Mohamed Salah",
            "goals": 1
          },
          {
            "name": "Sadio Mane",
            "goals": 1
          }
        ]
      },
      "away_team": {
        "name": "Manchester City",
        "goals": 2,
        "players": [
          {
            "name": "Kevin De Bruyne",
            "goals": 1
          },
          {
            "name": "Riyad Mahrez",
            "goals": 1
          }
        ]
      },
      "date": "2023-10-22",
      "venue": "Anfield",
      "metrics": {
        "possession": {
          "home_team": 50,
          "away_team": 50
        },
        "shots": {
          "home_team": 12,
          "away_team": 11
        },
        "corners": {
          "home_team": 5,
          "away_team": 4
        },
        "yellow_cards": {
          "home_team": 2,
          "away_team": 1
        },
        "red_cards": {
          "home_team": 0,
          "away_team": 0
        }
      }
    }
  ]
}

]

# Initialize lists to store data
home_team_shots = []
away_team_shots = []

# Iterate through matches in the data
for match in data[0]['matches']:
    home_team_shots.append(match['metrics']['shots']['home_team'])
    away_team_shots.append(match['metrics']['shots']['away_team'])

# Create a DataFrame
df = pd.DataFrame({
    'Home Team Shots': home_team_shots,
    'Away Team Shots': away_team_shots
})

print(df)
