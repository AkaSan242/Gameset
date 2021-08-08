"""Define the main controller"""

import sys
from time import sleep
from .tournamentcontroller import TournamentController


class Controller(TournamentController):
    """Gameset Main Controller"""
    def __init__(self,
                 player_list, tournament_list,
                 tournament_player_list, tournament_dic,
                 match_list, round_dic, ranks_dic):

        self.player_list = player_list
        self.tournament_list = tournament_list
        self.tournament_player_list = tournament_player_list
        self.tournament_dic = tournament_dic
        self.match_list = match_list
        self.round_dic = round_dic
        self.ranks_dic = ranks_dic

    def choose(self):
        """Use to make a choice on the main page"""
        choice = input()

        # Ajouter un joueur
        if choice == "1":
            number = input("Combien de Joueurs voulez vous ajouter ? (entrez un numéro):")
            for i in range(int(number)):
                self.add_a_new_player(self.player_list)
            self.back_to_main_page()
        # Liste des joueurs
        elif choice == "2":
            if len(self.player_list) == 0:
                print("Il n'y a aucun joueurs dans la liste")
                self.back_to_main_page()
            else:
                search_by = input("Vous voulez la liste des Joueurs par\
                1.Ordre Alphabétique 2.Classement:")

                if search_by == "1":
                    self.search_player_by_name(self.player_list)
                    update = input("Voulez-vous modifier le classement d'un joueur\
                            1.Oui/2.Non:")
                    if update == "1":
                        self.update_player_rank(self.player_list)
                        self.back_to_main_page()
                    elif update == "2":
                        self.back_to_main_page()

                elif search_by == "2":
                    self.search_player_by_rank(self.player_list)
                    update = input("Voulez-vous modifier le classement d'un joueur\
                                            1.Oui/2.Non:")
                    if update == "1":
                        self.update_player_rank(self.player_list)
                        self.back_to_main_page()
                    elif update == "2":
                        self.back_to_main_page()
        # Tournoi
        elif choice == "3":
            if len(self.player_list) < Tournament.NUMBER_OF_PLAYERS:
                print("Il n'y a pas assez de joueurs disponible pour un tournoi dans la liste\
                ( Joueurs requis:'{}' Disponible:'{}' )".format(Tournament.NUMBER_OF_PLAYERS, len(self.player_list)))

                add = input("Voulez-vous ajouter les participants maintenant\
                1.Oui/2.Non:")
                if add == "1":
                    for i in range(Tournament.NUMBER_OF_PLAYERS):
                        self.add_a_new_player(self.player_list)
                    self.back_to_main_page()
                elif add == "2":
                    self.back_to_main_page()

            else:
                self.new_tournament(self.tournament_dic)
                sleep(2)
                for i in range(Tournament.NUMBER_OF_PLAYERS):
                    self.choose_a_player(self.player_list, self.tournament_player_list)
                    print("Ajout d'un nouveau joueur {} sur {}".format(len(self.tournament_player_list),
                                                                       Tournament.NUMBER_OF_PLAYERS))

            self.show_players(self.player_list)
            self.tournament_dic["Joueurs"] = str(self.tournament_player_list)
            sleep(2)
            print("Nous allons commencer le tirage au sort...")
            sleep(2)
            self.rank_player(self.tournament_player_list, self.ranks_dic)
            for i in range(Tournament.NUMBER_OF_ROUNDS):
                self.tournament_round(self.tournament_player_list, self.ranks_dic, self.round_dic, self.match_list)
                self.continuer()

            self.tournament_dic['Vainqueur'] = self.ranks_dic['1']
            self.tournament_dic['Rounds'] = str(self.round_dic)
            print("Le gagnant du Tournoi {} est: '{}'".format(self.tournament_dic['Nom'],
                                                              self.tournament_dic['Vainqueur']))

            resume = input("Quelles sont les remarques générales de ce Tournoi:")
            self.tournament_dic['Déscription'] = resume
            self.tournament_list.append(self.tournament_dic)

        # Liste des Tournois
        elif choice == "4":
            if len(self.tournament_list) == 0:
                print("Aucun Tournoi enregistrer")
                self.back_to_main_page()
            else:
                print(self.tournament_list)
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










