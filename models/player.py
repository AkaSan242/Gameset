"""Define player model"""

from tinydb import TinyDB, Query


class Player:
    """player
    A player is define by:

    -First name
    -Last name
    -Birth date
    -Gender
    -Rank"""

    def __init__(self, name, last_name, birth_date, gender, rank, score=0):
        """player informations needed for the game"""
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.score = int(score)

    def __str__(self):
        """Used in print"""
        return f"{self.name}"

    def __repr__(self):
        """Used in print"""
        return f"{self.name} {self.last_name}"

    def serialized_player(self):
        return {
            "name": self.name,
            "last name": self.last_name,
            "birth date": self.birth_date,
            "gender": self.gender,
            "rank": self.rank,
            "score": self.score,
        }

    def save_player(self):
        """Use to record a player in the database"""
        db = TinyDB("db.json")
        player_table = db.table("players")
        player_table.insert(self.serialized_player())
