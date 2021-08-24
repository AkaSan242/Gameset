"""Base Tournament view"""

from operator import attrgetter


class TournamentView:
    """Gameset Tournament view"""

    def rank_player(self, players):
        """ranking players for match"""
        i = 1
        for player in players:
            player.rank = i
            i += 1

    def player_ranking(self, player_list):
        """Ranking player by score"""
        new_ranking = sorted(player_list, key=attrgetter('score'), reverse=True)
        i = 1
        for elt in new_ranking:
            print("{}.{}".format(i, elt))
            i += 1
        self.rank_player(new_ranking)

    def show_tournament_informations(self, name, place, time_control, date, player_numbers, number_of_rounds):
        """Show tournament information"""
        print("Tournoi:'{}' Lieu:'{}' Date:'{}' Participants:'{}' Rounds:'{}' Contrôle du temps:'{}' ".format
              (name,
               place,
               date,
               player_numbers,
               number_of_rounds,
               time_control))

    def show_tournament_match(self, match_list):
        """Show all matchs of the round"""
        print("Voici tout les matchs du prochain round:")
        for elt in match_list:
            print(elt)

    def tournament_main_page(self):
        """Print Main menu"""
        print("Menu Principal")
        print("1.Ajouter un Joueur")
        print("2.Liste des joueurs")
        print("3.Commencer un Tournoi")
        print("4.Liste des Tournois")
        print("5.Liste Des Matchs")
        print("6.Quitter")

    def tournament_list_main_page(self, tournament):
        """Print Tournament list Main menu"""
        print("Tournoi:'{}' Date:'{}' Lieu:'{}' Contrôle du Temps:'{}' Remarques:'{}'".format
              (tournament.name,
               tournament.date,
               tournament.place,
               tournament.time_control,
               tournament.description))

        print("1.Liste des Participants")
        print("2.Listes des Rounds et Matchs")

    def start_continue_tournament(self):
        print("Que voulez-vous faire ?")
        print("1.Nouveau Tournoi")
        print("2.Continuer un Tournoi")
