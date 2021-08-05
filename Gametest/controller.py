"""Define the main controller"""

import sys
from time import sleep
from tournament import Tournament
from playercontroller import PlayerController
from tournamentcontroller import TournamentController

game_players = []

tournament_players = []
tournament_list = []
tournament = {'Nom': '', 'Lieu': '', 'Date': '', 'Nombres de tours': '', 'Rounds': '', 'Joueurs': '',
              'Contrôle du temps': '', 'Déscription': '', 'Vainqueur': ''}
match = []
round = {'1': '', '2': '', '3': '', '4': ''}
score = []

ranks = {}


class Controller(PlayerController, TournamentController):
    """Gameset Main Controller"""

    def choose(self):
        """Use to make a choice on the main page"""
        choice = input()
        if choice == "1":
            self.add_a_new_player(game_players)
            self.back_to_main_page()
        elif choice == "2":
            self.show_list_players(game_players)
            update = input("Voulez-vous modifier le classement d'un joueur\
            1.Oui/2.Non:")
            if update == 1 or "1":
                self.update_player_rank(game_players)
                self.back_to_main_page()
            elif update == 2 or "2":
                self.back_to_main_page()
        elif choice == "3":
            if len(game_players) < Tournament.NUMBER_OF_PLAYERS:
                print("Il n'y a pas assez de joueurs disponible pour un tournoi dans la liste\
                ( Joueurs requis:'{}' Disponible:'{}' )".format(Tournament.NUMBER_OF_PLAYERS, len(game_players)))
                add = input("Voulez-vous ajouter les participants maintenant\
                1.Oui/2.Non:")
                if add == "1" or 1:
                    for i in range(Tournament.NUMBER_OF_PLAYERS):
                        self.add_a_new_player(game_players)
                    self.back_to_main_page()
            else:
                self.new_tournament(tournament)
                for i in range(Tournament.NUMBER_OF_PLAYERS):
                    self.choose_a_player(game_players, tournament_players)
                    print("Ajout d'un nouveau joueur {} sur {}".format(len(tournament_players),
                                                                       Tournament.NUMBER_OF_PLAYERS))

            self.show_players(game_players)
            tournament["Joueurs"] = str(tournament_players)
            sleep(2)
            print("Nous allons commencer le tirage au sort...")
            sleep(2)
            self.rank_player(tournament_players, ranks)
            self.first_match(ranks, match)
            self.show_tournament_match(match)
            sleep(5)
            round["1"] = str(match)
            self.update_player_score(tournament_players)
            self.show_players_status(tournament_players)
            sleep(3)
            print("Classement:")
            self.player_ranking(tournament_players)
            sleep(5)
            match.clear()
            self.tournament_match(ranks, match)
            self.show_tournament_match(match)
            sleep(5)
        elif choice == "4":
            print(Tournament.__doc__)
            self.back_to_main_page()
        elif choice == "5":
            sys.exit()

    def continuer(self):
        continuer = input("Voulez-vous continuer ?\
    1.Oui/2.Non:")
        if continuer == "1" or 1:
            pass
        elif continuer == "2" or 2:
            self.tournament_main_page()
            self.choose()

    def back_to_main_page(self):
        main_page = input("voulez-vous revenir à la page principal ?\
    1.Oui/2.Non:")
        if main_page == "1" or 1:
            self.tournament_main_page()
            self.choose()
        elif main_page == "2" or 2:
            sys.exit()


game = Controller()

print("BIENVENUE DANS GAMESET !")
game.tournament_main_page()
game.choose()







