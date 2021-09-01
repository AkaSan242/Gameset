"""define tournament model"""

import datetime
from tinydb import TinyDB, Query
from operator import attrgetter
from .player import Player
from .tour import Tour


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

    def __init__(
        self,
        name,
        place,
        time_control,
        tour_list,
        player_list,
        date=datetime.date.today(),
        player_numbers=NUMBER_OF_PLAYERS,
        number_of_rounds=NUMBER_OF_ROUNDS,
        description="",
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
        self.serialized_player = []
        self.serialized_tour = []

    def __str__(self):
        """used in print"""
        return (
            f"Nom:{self.name} Lieu:{self.place} Date:{self.date} Participants:{self.player_list}"
            f"Nombre de rounds:{self.number_of_rounds}, Contrôle du temmps:{self.time_control}"
        )

    def save_tournament(self):
        """Use to record the tournament in the database"""
        db = TinyDB("db.json")
        tournament_table = db.table("tournament")
        now = datetime.datetime.now()
        self.date = datetime.datetime.timestamp(now)

        serialized_tournament = {
            "name": self.name,
            "Place": self.place,
            "date": self.date,
            "player number": self.player_numbers,
            "time controle": self.time_control,
            "number of rounds": self.number_of_rounds,
            "player 1": self.serialized_player[0],
            "player 2": self.serialized_player[1],
            "player 3": self.serialized_player[2],
            "player 4": self.serialized_player[3],
            "player 5": self.serialized_player[4],
            "player 6": self.serialized_player[5],
            "player 7": self.serialized_player[6],
            "player 8": self.serialized_player[7],
            "description": self.description,
        }

        tournament_table.insert(serialized_tournament)
