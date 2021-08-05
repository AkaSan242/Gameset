"""Define the main controller"""

import sys
from time import sleep
from tournament import Tournament
from tournamentcontroller import TournamentController

game_players = []
game_tournament = []
tournament_players = []
tournament_list = []
tournament = {'Nom': '', 'Lieu': '', 'Date': '', 'Nombres de tours': '', 'Rounds': '', 'Joueurs': '',
              'Contrôle du temps': '', 'Déscription': '', 'Vainqueur': ''}
match = []
round = {}
ranks = {}


class Controller(TournamentController):
    """Gameset Main Controller"""

    def choose(self):
        """Use to make a choice on the main page"""
        choice = input()

        # Ajouter un joueur
        if choice == "1":
            number = input("Combien de Joueurs voulez vous ajouter ? (entrez un numéro):")
            for i in range(int(number)):
                self.add_a_new_player(game_players)
            self.back_to_main_page()
        # Liste des joueurs
        elif choice == "2":
            if len(game_players) == 0:
                print("Il n'y a aucun joueurs dans la liste")
                self.back_to_main_page()
            else:
                search_by = input("Vous voulez la liste des Joueurs par\
                1.Ordre Alphabétique 2.Classement:")

                if search_by == "1":
                    self.search_player_by_name(game_players)
                    update = input("Voulez-vous modifier le classement d'un joueur\
                            1.Oui/2.Non:")
                    if update == "1":
                        self.update_player_rank(game_players)
                        self.back_to_main_page()
                    elif update == "2":
                        self.back_to_main_page()

                elif search_by == "2":
                    self.search_player_by_rank(game_players)
                    update = input("Voulez-vous modifier le classement d'un joueur\
                                            1.Oui/2.Non:")
                    if update == "1":
                        self.update_player_rank(game_players)
                        self.back_to_main_page()
                    elif update == "2":
                        self.back_to_main_page()
        # Tournoi
        elif choice == "3":
            if len(game_players) < Tournament.NUMBER_OF_PLAYERS:
                print("Il n'y a pas assez de joueurs disponible pour un tournoi dans la liste\
                ( Joueurs requis:'{}' Disponible:'{}' )".format(Tournament.NUMBER_OF_PLAYERS, len(game_players)))

                add = input("Voulez-vous ajouter les participants maintenant\
                1.Oui/2.Non:")
                if add == "1":
                    for i in range(Tournament.NUMBER_OF_PLAYERS):
                        self.add_a_new_player(game_players)
                    self.back_to_main_page()
                elif add == "2":
                    self.back_to_main_page()

            else:
                self.new_tournament(tournament)
                sleep(2)
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
            for i in range(Tournament.NUMBER_OF_ROUNDS):
                self.tournament_round(tournament_players, ranks, round, match)
                self.continuer()

            tournament['Vainqueur'] = ranks['1']
            tournament['Rounds'] = str(round)
            print("Le gagnant du Tournoi {} est: '{}'".format(tournament['Nom'], tournament['Vainqueur']))

            resume = input("Quelles sont les remarques générales de ce Tournoi:")
            tournament['Déscription'] = resume
            game_tournament.append(tournament)

        # Liste des Tournois
        elif choice == "4":
            if len(game_tournament) == 0:
                print("Aucun Tournoi enregistrer")
                self.back_to_main_page()
            else:
                print(game_tournament)
                self.back_to_main_page()

        # Quitter
        elif choice == "5":
            print("GAMESET ET MAT ! CIAO")
            sys.exit()

    def continuer(self):
        continuer = input("Voulez-vous continuer ?\
    1.Oui/2.Non:")
        if continuer == "2":
            self.tournament_main_page()
            self.choose()
        elif continuer == "1":
            print("THE SHOW GOES ON ! ")

    def back_to_main_page(self):
        self.tournament_main_page()
        self.choose()


game = Controller()

print("BIENVENUE DANS GAMESET !")
game.tournament_main_page()
game.choose()







