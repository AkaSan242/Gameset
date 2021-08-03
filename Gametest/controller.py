"""Define the main controller"""

import sys
from time import sleep
from tournament import Tournament
from playerview import PlayerView
from tournamentview import TournamentView

game = PlayerView()
tour = TournamentView()

game_players = []

tournament_players = []
tournament_list = []
tournament = {'Nom': '', 'Lieu': '', 'Date': '', 'Nombres de tours': '', 'Rounds': '', 'Joueurs': '',
              'Contrôle du temps': '', 'Déscription': '', 'Vainqueur': ''}
match = []
round = {'1': '', '2': '', '3': '', '4': ''}
score = []

rank_sup = {'1': '', '2': '', '3': '', '4': ''}
rank_inf = {'5': '', '6': '', '7': '', '8': ''}
ranking = rank_sup, rank_inf


def choice():

    choice = input()
    if choice == "1":
        game.add_a_new_player(game_players)
        back_to_main_page()
    elif choice == "2":
        game.show_list_players(game_players)
        update = input("Voulez-vous modifier le classement d'un joueur\
        1.Oui/2.Non:")
        if update == 1 or "1":
            game.update_player_rank(game_players)
            back_to_main_page()
        else:
            back_to_main_page()
    elif choice == "3":
        tour.new_tournament(tournament)
        if len(game_players) < Tournament.NUMBER_OF_PLAYERS:
            print("Il n'y a pas assez de joueurs disponible pour un tournoi dans la liste\
             ( Joueurs requis:'{}' Disponible:'{}' )".format(Tournament.NUMBER_OF_PLAYERS, len(game_players)))
            add = input("Voulez-vous ajouter les participants maintenant\
            1.Oui/2.Non:")
            if add == "1" or 1:
                for i in range(Tournament.NUMBER_OF_PLAYERS):
                    game.add_a_new_player(game_players)
                back_to_main_page()
        else:
            for i in range(Tournament.NUMBER_OF_PLAYERS):
                tour.choose_a_player(game_players, tournament_players)
                print("Ajout d'un nouveau joueur {} sur {}".format(len(tournament_players),
                                                                   Tournament.NUMBER_OF_PLAYERS))

        game.show_players(game_players)
        tournament["Joueurs"] = str(tournament_players)
        sleep(2)
        print("Nous allons commencer le tirage au sort...")
        sleep(2)
        tour.rank_player_sup(tournament_players, rank_sup)
        tour.rank_player_inf(tournament_players, rank_inf)
        tour.first_match(rank_sup, rank_inf, match)
        tour.show_tournament_match(match)
        sleep(5)
        round["1"] = str(match)
        game.update_player_score(tournament_players)
        game.show_players_status(tournament_players)
        sleep(3)
        print("Classement:")
        game.player_ranking(tournament_players)
        sleep(5)
        match.clear()
        tour.tournament_match(rank_sup, rank_inf, match)
        tour.show_tournament_match(match)
        sleep(5)
        round["2"] = str(match)
        game.update_player_score(tournament_players)
        game.show_players_status(tournament_players)
        sleep(3)
        print("Classement:")
        print(ranking)
        sleep(5)
        match.clear()
    elif choice == "4":
        print(Tournament.__doc__)
        back_to_main_page()
    else:
        sys.exit()


def continuer():
    continuer = input("Voulez-vous continuer ?\
    1.Oui/2.Non:")
    if continuer == "2" or 2:
        tour.tournament_main_page()
        choice()
    else:
        pass


def back_to_main_page():
    retour = input("voulez-vous revenir à la page principal ?\
    1.Oui/2.Non:")
    if retour == "1" or 1:
        tour.tournament_main_page()
        choice()
    else:
        sys.exit()



print("BIENVENUE DANS GAMESET !")
tour.tournament_main_page()
choice()







