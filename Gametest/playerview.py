"""Base Player view."""

from tournament import Tournament


class PlayerView:
    """Gameset player view"""

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

    def show_players_status(self, player_list):
        """Show all Players status after round"""
        print("Voici le nouveau classement et score des joueurs après ce round:")
        for player in player_list:
            print("Joueur: {} Score: {} Points".format(player, player.score))




