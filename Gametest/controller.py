"""Define the main controller"""

import sys
from time import sleep
from tournament import Tournament
from playerview import PlayerView
from tournamentview import TournamentView

game = PlayerView()
tour = TournamentView()

tournament = {'Nom': '', 'Lieu': '', 'Date': '', 'Nombres de tours': '', 'Rounds': '', 'Joueurs': '',
              'Contrôle du temps': '', 'Déscription': ''}
match = []
players_list = []
players = []
rank_sup = {'1': '', '2': '', '3': '', '4': ''}
rank_inf = {'5': '', '6': '', '7': '', '8': ''}
ranking = rank_sup, rank_inf
round = {'1': '', '2': '', '3': '', '4': ''}
round_match = []
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
        tour.new_tournament(tournament)
        if len(players_list) < Tournament.NUMBER_OF_PLAYERS:
            print("Il n'y a pas assez de joueurs disponible pour un tournoi dans la liste\
             ( Joueurs requis:'{}' Disponible:'{}' )".format(Tournament.NUMBER_OF_PLAYERS, len(players_list)))
            back_to_main_page()
        else:
            for i in range(Tournament.NUMBER_OF_PLAYERS):
                tour.choose_a_player(players_list, players)
                print("Ajout d'un nouveau joueur {} sur {}".format(len(players), Tournament.NUMBER_OF_PLAYERS))

        game.show_players(players)
        tournament["Joueurs"] = str(players)
        sleep(2)
        print("Nous allons commencer le tirage au sort...")
        sleep(2)
        tour.rank_player_sup(players, rank_sup)
        tour.rank_player_inf(players, rank_inf)
        tour.first_match(rank_sup, rank_inf, match)
        round_match.append(match)
        tour.show_tournament_match(round_match)
        sleep(5)
        round["1"] = str(round_match)
        tour.update_player_score(players, score)
        tour.update_player_rank(players, rank_sup, rank_inf)
        print("Classement:")
        print(ranking)
        sleep(5)
        round_match.clear()
        tour.tournament_match(rank_sup, rank_inf, match)
        round_match.append(match)
        tour.show_tournament_match(round_match)
        sleep(5)
        round["2"] = str(round_match)
        tour.update_player_score(players, score)
        tour.update_player_rank(players, rank_sup, rank_inf)
        tour.show_players_status(players)
        print("Classement:")
        print(ranking)
        sleep(5)
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







