"""define tournament model"""

from datetime import date


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

    NUMBER_OF_PLAYERS = 4
    NUMBER_OF_ROUNDS = 2

    def __init__(self,
                 name,
                 place,
                 time_control,
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

    def show_tournament_informations(self):
        """Show tournament information"""
        print("Bienvenue chers spectateurs nous allons commencer le tournoi '{}' qui se déroule à '{}',\
         nous sommes le {}. il y aura '{}' participants pour '{}' rounds".format(self.name,
                                                                                 self.place,
                                                                                 self.date,
                                                                                 self.player_numbers,
                                                                                 self.number_of_rounds))
