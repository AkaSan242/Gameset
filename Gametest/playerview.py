"""Base Player view."""

from time import sleep
from player import Player
from tournament import Tournament
from operator import attrgetter

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

    def show_players(self, player_list):
        """Present all players of tournament """
        print("Voici les {} participants du Tournoi:".format(Tournament.NUMBER_OF_PLAYERS))
        for players in player_list:
            print("{} Classement:'{}' Score:'{}'".format(players, players.rank, players.score))

    def show_list_players(self, player_list):
        """Present all players of the list """
        print("Voici les {} Joueurs disponible:".format(len(player_list)))
        for players in player_list:
            print("Prénom: {} Nom: {} Classement: {}".format(players.name, players.last_name, players.rank))
        if len(player_list) == 0:
            print("Il n'y a aucun joueurs disponible")

    def show_player(self, name, last_name, birth_date, gender, rank):
        """Show player informations"""
        print("Prénom:'{}' Nom:'{}' Date de naissance:'{}' Genre:'{}' Classement: '{}'".format(name,
                                                                                               last_name,
                                                                                               birth_date,
                                                                                               gender,
                                                                                               rank))

    def update_player_rank(self, player_list):
        """Update player rank"""
        print("Mise à jour du classement:")
        for i in range(len(player_list)):
            print("{}.{}".format(i, player_list[i]))

        choose_player = input("Choisissez un joueur (entrez son numéro):")
        player = player_list[int(choose_player)]
        new_rank = input("Quel est le nouveau classement de {}:".format(player))
        player.rank = new_rank

    def update_player_score(self, player_list):
        """Add score for player after round"""
        print("C'est l'heure d'ajouter les résultats:")
        for i in range(len(player_list)):
            player = player_list[i]
            add_score = input("Quel est le score de {}:".format(player))
            score = add_score
            player.score += int(score)

    def show_players_status(self, player_list):
        """Show all Players status after round"""
        print("Voici le nouveau classement et score des joueurs après ce round:")
        for player in player_list:
            print("Joueur: {} Classement: {} Score: {} Points".format(player, player.rank, player.score))

    def player_ranking(self, player_list):
        """Ranking player by score"""
        for player in player_list:
            new_ranking = player_list.sort(player.score)
            print(new_ranking)
