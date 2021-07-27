"""Define the main controller"""

import sys
from time import sleep
from tournament import Tournament
from playerview import PlayerView
from tournamentview import TournamentView

game = PlayerView()
tour = TournamentView()

gameset_player = []
gameset_match = []
players_list = []
tournament_list = []
round_one_list = []
round_two_list = []
round_three_list = []
round_four_list = []
score = []


def choice():
    choice = input()
    if choice == "1":
        game.add_a_new_player(gameset_player)
        back_to_main_page()
    elif choice == "2":
        game.show_list_players(gameset_player)
        back_to_main_page()
    elif choice == "3":
        tour.create_new_tournament(tournament_list)
        while len(players_list) < Tournament.NUMBER_OF_PLAYERS:
            game.add_a_new_player(players_list)
            print("Ajout d'un nouveau joueur {} sur {}".format(len(players_list), Tournament.NUMBER_OF_PLAYERS))

        game.show_players(players_list)
        sleep(2)
        print("Nous allons commencer le tirage au sort...")
        sleep(2)
        for i in range(Tournament.NUMBER_OF_ROUNDS):
            tour.tournament_match(players_list, round_one_list)
        tour.show_tournament_match(round_one_list)
        sleep(5)
        tour.tournament_player_score(players_list, score)
        tour.tournament_show_player_score(score)
        sleep(5)
        continuer()
        for i in range(Tournament.NUMBER_OF_ROUNDS):
            tour.tournament_match(players_list, round_two_list)
        tour.show_tournament_match(round_two_list)
        sleep(2)
        for i in range(Tournament.NUMBER_OF_ROUNDS):
            tour.tournament_match(players_list, round_three_list)
        tour.show_tournament_match(round_three_list)
        sleep(2)
        for i in range(Tournament.NUMBER_OF_ROUNDS):
            tour.tournament_match(players_list, round_four_list)
        tour.show_tournament_match(round_four_list)
        sleep(2)

    elif choice == "4":
        tour.tournament_match(gameset_player, gameset_match)
        tour.show_tournament_match(gameset_match)
    elif choice == "5":
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







