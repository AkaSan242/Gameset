"""define tournament model"""

from datetime import date
from tinydb import TinyDB, Query
db = TinyDB('db.json')
tournament_table = db.table('tournament')


class Tournament:
    """tournament

    Organisation of a tournament
            a tournament has:

            -Name: The name of the tournament
            -Place: Where is the tournament
            -Date: dates of all match days
            -Number of player per tournament (default '8')
            -Number of round in the tournament(default '4')
            -time control: bullet, blitz or quick hit
            -description of the tournament
            """

    NUMBER_OF_PLAYERS = 8
    NUMBER_OF_ROUNDS = 4

    def __init__(self,
                 name,
                 place,
                 time_control,
                 tour_list=list,
                 player_list=list,
                 date=date.today(),
                 player_numbers=NUMBER_OF_PLAYERS,
                 number_of_rounds=NUMBER_OF_ROUNDS,
                 description=''
                 ):
        """Tournament Informations"""
        self.name = name
        self.place = place
        self.date = date
        self.player_numbers = player_numbers
        self.number_of_rounds = number_of_rounds
        self.time_control = time_control
        self.description = description
        self.tour_list = tour_list
        self.player_list = player_list

    def serialized_tournament(self):
        """Use to record the tournament in the database"""
        serialized_tournament = {
            'name': self.name,
            'Place': self.place,
            'date': self.date,
            'player number': self.player_numbers,
            'time controle': self.time_control,
            'participants': self.player_list,
            'number of rounds': self.number_of_rounds,
            'description': self.description,
            'rounds': self.tour_list
        }

        tournament_table.insert(serialized_tournament)
