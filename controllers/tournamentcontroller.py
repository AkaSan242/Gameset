"""Base Tournament Controller"""


from operator import attrgetter
from time import sleep
from views.tournamentview import tournament_list_main_page


def choose_a_player(player_list, tournament_players_list):
    """Select a player for the tournament"""
    for elt in player_list:
        if elt not in tournament_players_list:
            index = player_list.index(elt)
            print("{}.{}".format(index, elt))

    print("Participants:{}".format(tournament_players_list))

    choose_player = input("Choisissez un joueur (entrez son numéro):")
    player = player_list[int(choose_player)]

    if player in tournament_players_list:
        print("{} est déja pris".format(player))
        sleep(1)
    else:
        print("Vous avez choisi:{}".format(player))
        sleep(1)
        tournament_players_list.append(player)


def check_tournament_list(tournament_list):
    """Use to check informations about all tournaments"""
    for elt in tournament_list:
        index = tournament_list.index(elt)
        print("{}.{}".format(index, elt.name))

    tournament_choice = input(
        "Choisissez le Tournoi à consulter (Entrez son numéro):"
    )
    tournament = tournament_list[int(tournament_choice)]

    tournament_list_main_page(tournament)
    choose_tournament_info(tournament)


def choose_tournament_info(tournament):
    """use to choose the informations to show"""
    choice = input()
    if choice == "1":
        print("Vous souhaitez la liste par:")
        print("1.Nom")
        print("2.Classeement")

        list_by = input()
        if list_by == "1":
            name_ranking = sorted(tournament.player_list,
                                  key=attrgetter("name"))
            for elt in name_ranking:
                print(elt, elt.last_name)
            sleep(2)

        elif list_by == "2":
            ranking = sorted(tournament.player_list,
                             key=attrgetter("rank"))
            i = 1
            for elt in ranking:
                print("{}  Classement:{}  Score:{}".format(elt, i, elt.score))
                i += 1
            sleep(2)

    elif choice == "2":
        print("Vous voulez voir:")
        print("1.Liste des Rounds")
        print("2.Liste des matchs")

        list_of = input()
        if list_of == "1":
            for elt in tournament.tour_list:
                print(elt)

        elif list_of == "2":
            for elt in tournament.tour_list:
                print(elt.show_match())
