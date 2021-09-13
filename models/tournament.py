"""define tournament model"""

from time import strftime
from tinydb import TinyDB


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
        date=strftime("%Y %m %d %H:%M"),
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

    def __str__(self):
        """used in print"""
        return (
            f"Nom:{self.name} Lieu:{self.place} Date:{self.date}"
            f" Participants:{self.player_list}"
            f"Nombre de rounds:{self.number_of_rounds},"
            f" Contrôle du temmps:{self.time_control}"
        )

    def serialized_tournament(self):
        return {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "number of players": self.player_numbers,
            "number of rounds": self.number_of_rounds,
            "time control": self.time_control,
            "description": self.description,
            "tour list":
                [tour.serialized_tour() for tour in self.tour_list],
            "player list":
                [player.serialized_player() for player in self.player_list],
        }

    def save_tournament(self):
        """Use to record the tournament in the database"""
        db = TinyDB("db.json")
        tournament_table = db.table("tournament")
        tournament_table.insert(self.serialized_tournament())
