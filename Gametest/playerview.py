"""Base Player view."""

from time import sleep
from player import Player
from tournament import Tournament


class PlayerView:
    """Gameset player view"""

    def add_a_new_player(self, player_list):
        """Add a new player in the game"""
        player_name = input("Quel est le prénom du joueur:")
        player_last_name = input("Quel est le nom du Joueur:")
        player_birth_date = input("Date de Naissance:")
        player_gender = input("Sexe (Homme, Femme, Personnel):")
        player_rank = input("Classement:")

        new_player = Player(player_name,
                            player_last_name,
                            player_birth_date,
                            player_gender,
                            player_rank)

        player_list.append(new_player)
        print("Ajout du nouveau joueur '{}' terminé".format(player_name))
        sleep(2)
        PlayerView.show_player(self, player_name, player_last_name, player_birth_date, player_gender, player_rank)

    def show_players(self, players):
        """Present all players of tournament """
        print("Voici les {} participants du Tournoi:".format(Tournament.NUMBER_OF_PLAYERS))
        for players in players:
            print("{} Classement:'{}' Score:'{}'".format(players, players.rank, players.score))

    def show_list_players(self, player_list):
        """Present all players of list """
        print("Voici les {} Joueurs disponible:".format(len(player_list)))
        for players in player_list:
            print(players)
        if len(player_list) == 0:
            print("Il n'y a aucun joueur disponible")

    def show_player(self, name, last_name, birth_date, gender, rank):
        """Show player informations"""
        print("Prénom:'{}' Nom:'{}' Date de naissance:'{}' Genre:'{}' Classement: '{}'".format(name,
                                                                                               last_name,
                                                                                               birth_date,
                                                                                               gender,
                                                                                               rank))