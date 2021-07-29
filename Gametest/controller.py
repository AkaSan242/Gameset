"""Define the main controller"""

import sys
from time import sleep
from tournament import Tournament
from playerview import PlayerView
from tournamentview import TournamentView

game = PlayerView()
tour = TournamentView()

match = []
players_list = []
players = []
tournament_list = []
round_one_list = []
round_two_list = []
round_three_list = []
round_four_list = []
score = []
score_two = []

def choice():
    choice = input()
    if choice == "1":
        game.add_a_new_player(players_list)
        back_to_main_page()
    elif choice == "2":
        game.show_list_players(players_list)
        back_to_main_page()
    elif choice == "3":
        tour.new_tournament(tournament_list)
        if len(players_list) < Tournament.NUMBER_OF_PLAYERS:
            print("Il n'y a pas assez de joueurs disponible pour un tournoi dans la liste\
             ( Joueurs requis:'{}' Disponible:'{}' )".format(Tournament.NUMBER_OF_PLAYERS, len(players_list)))
            back_to_main_page()
        else:
            for i in range(Tournament.NUMBER_OF_PLAYERS):
                tour.choose_a_player(players_list, players)
                print("Ajout d'un nouveau joueur {} sur {}".format(len(players), Tournament.NUMBER_OF_PLAYERS))

        game.show_players(players)
        sleep(2)
        print("Nous allons commencer le tirage au sort...")
        sleep(2)
        for i in range(Tournament.NUMBER_OF_ROUNDS):
            tour.match(players, round_one_list)
        tour.show_tournament_match(round_one_list)
        sleep(5)
        tour.update_player_score(players, score)
        tour.update_player_rank(players)
        tour.show_players_status(players)
        sleep(5)
        for i in range(Tournament.NUMBER_OF_ROUNDS):
            tour.match(players, round_two_list)
        tour.show_tournament_match(round_two_list)
        sleep(5)
        tour.update_player_score(players, score_two)
        tour.update_player_rank(players)
        tour.show_players_status(players)
        sleep(5)
        continuer()
        for i in range(Tournament.NUMBER_OF_ROUNDS):
            tour.match(players, round_three_list)
        tour.show_tournament_match(round_three_list)
        sleep(2)
        for i in range(Tournament.NUMBER_OF_ROUNDS):
            tour.match(players, round_four_list)
        tour.show_tournament_match(round_four_list)
        sleep(2)
    elif choice == "4":
        print(Tournament.__doc__)
        back_to_main_page()
    else:
        sys.exit()


def continuer():
    continuer = input("Voulez-vous continuer Y/N ?:")
    if continuer == "N" or "n":
        tour.tournament_main_page()
        choice()
    else:
        pass



def back_to_main_page():
    retour = input("voulez-vous revenir à la page principal Y/N:")
    if retour == "Y" or "y":
        tour.tournament_main_page()
        choice()
    else:
        sys.exit()



print("BIENVENUE DANS GAMESET !")
tour.tournament_main_page()
choice()







