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

    def show_player(self):
        """Show player informations"""
        print("Prénom:'{}' Nom:'{}' Date de naissance:'{}' Genre:'{}' Classement: '{}'".format(self.name,
                                                                                               self.last_name,
                                                                                               self.birth_date,
                                                                                               self.gender,
                                                                                               self.rank))

    def show_player_current_score(self):
        """Show player score after round"""
        print("Joueur: {} Points: {}".format(self.name, self.score))

    def show_player_current_rank(self):
        """Show player score after round"""
        print("Joueur: {} Classement: {}".format(self.name, self.rank))

    def __str__(self):
        """Used in print"""
        return f"'{self.name}'"