"""Define player model"""


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
        self.rank = int(rank)
        self.score = int(score)

    def __str__(self):
        """Used in print"""
        return f"'{self.name}'"