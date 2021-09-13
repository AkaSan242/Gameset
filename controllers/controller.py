"""Define the main controller"""

import sys
from operator import attrgetter
from tinydb import TinyDB
from time import sleep

# Controllers
from .tournamentcontroller import choose_a_player, check_tournament_list
from .playercontroller import (
    add_a_new_player,
    search_player_by_name,
    search_player_by_rank,
    update_delete_player,
    update_player_rank,

)
from .tourcontroller import tournament_round

# Models
from models.tournament import Tournament
from models.player import Player
from models.tour import Tour

# Views
from views.playerview import show_players
from views.tournamentview import (
    start_continue_tournament,
    rank_player,
    tournament_main_page,
    show_tournament_informations,
)

db = TinyDB("db.json")
players_table = db.table("players")
tournament_table = db.table("tournament")


class Controller:
    """Gameset Main Controller"""

    def __init__(self):

        self.player_list = []
        self.tournament_list = []
        self.tournament_player_list = []
        self.tour_list = []
        self.match_list = []
        self.tournament_match = []
        self.match_list_tuple = []

        # Get players from database
        serialized_players = players_table.all()
        for i in range(len(serialized_players)):
            name = serialized_players[i]["name"]
            last_name = serialized_players[i]["last name"]
            birth_date = serialized_players[i]["birth date"]
            gender = serialized_players[i]["gender"]
            rank = serialized_players[i]["rank"]
            self.player_list.append(Player(name,
                                           last_name,
                                           birth_date,
                                           gender,
                                           rank))

        # Get tournament from database
        serialized_tournament = tournament_table.all()
        for i in range(len(serialized_tournament)):
            name = serialized_tournament[i]["name"]
            place = serialized_tournament[i]["place"]
            date = serialized_tournament[i]["date"]
            number_of_players = serialized_tournament[i]["number of players"]
            number_of_rounds = serialized_tournament[i]["number of rounds"]
            time_control = serialized_tournament[i]["time control"]
            description = serialized_tournament[i]["description"]
            tour_list = serialized_tournament[i]["tour list"]
            player_list = serialized_tournament[i]["player list"]

            json_tournament = Tournament(
                name,
                place,
                time_control,
                tour_list=[],
                player_list=[],
                date=date,
                player_numbers=number_of_players,
                number_of_rounds=number_of_rounds,
                description=description,
            )

            for t in range(len(tour_list)):
                name = tour_list[t]["name"]
                match_list = tour_list[t]["match list"]
                start = tour_list[t]["start"]
                end = tour_list[t]["end"]
                tour = Tour(match_list, name, start, end)
                json_tournament.tour_list.append(tour)

            for p in range(len(player_list)):
                name = player_list[p]["name"]
                last_name = player_list[p]["last name"]
                birth_date = player_list[p]["birth date"]
                gender = player_list[p]["gender"]
                rank = player_list[p]["rank"]
                score = player_list[p]["score"]
                player = Player(name,
                                last_name,
                                birth_date,
                                gender,
                                rank,
                                score)
                json_tournament.player_list.append(player)

            self.tournament_list.append(json_tournament)

    def choose(self):
        """Use to make a choice on the main page"""
        choice = input()
        if choice == "1":
            self.choose_one()
        elif choice == "2":
            self.choose_two()
        elif choice == "3":
            self.choose_three()
        elif choice == "4":
            self.choose_four()
        elif choice == "5":
            self.choose_five()

    def choose_one(self):
        # Ajouter un joueur
        number = input("Combien de joueurs ? (entrez un numéro):")
        for i in range(int(number)):
            add_a_new_player(self.player_list)
        self.back_to_main_page()

    def choose_two(self):
        # Liste des joueurs
        if len(self.player_list) == 0:
            print("Il n'y a aucun joueurs dans la liste")
            self.back_to_main_page()
        else:
            search_by = input(
                "Liste des Joueurs par 1.Ordre Alphabétique/2.Classement:"
            )

            if search_by == "1":
                search_player_by_name(self.player_list)
                update = input(
                    "Modifier les informations d'un joueur ? 1.Oui/2.Non:"
                )
                if update == "1":
                    update_delete_player(self.player_list)
                    self.back_to_main_page()

                elif update == "2":
                    self.back_to_main_page()

            elif search_by == "2":
                search_player_by_rank(self.player_list)
                update = input(
                    "Modifier les informations d'un joueur ? 1.Oui/2.Non:"
                )
                if update == "1":
                    update_delete_player(self.player_list)
                    self.back_to_main_page()
                elif update == "2":
                    self.back_to_main_page()

    def choose_three(self):
        # Commencer un Tournoi
        start_continue_tournament()
        tournament_choice = input()
        if tournament_choice == "1":
            if len(self.player_list) < Tournament.NUMBER_OF_PLAYERS:
                print(
                    "(Requis:'{}' Disponible:'{}')".format(
                        Tournament.NUMBER_OF_PLAYERS, len(self.player_list)
                    )
                )

                add = input(
                    "Ajouter les participants ? 1.Oui/2.Non:"
                )
                if add == "1":
                    for i in range(
                        Tournament.NUMBER_OF_PLAYERS - len(self.player_list)
                    ):
                        add_a_new_player(self.player_list)
                    self.back_to_main_page()
                elif add == "2":
                    self.back_to_main_page()

            else:
                while len(
                        self.tournament_player_list)\
                        < Tournament.NUMBER_OF_PLAYERS:
                    choose_a_player(self.player_list,
                                    self.tournament_player_list)
                    print(
                        "Ajout d'un nouveau joueur {} sur {}".format(
                            len(self.tournament_player_list),
                            Tournament.NUMBER_OF_PLAYERS,
                        )
                    )

                sleep(2)
                show_players(self.tournament_player_list)
                sleep(2)

                name = input("Quel est le Nom du Tournoi:")
                while len(name) <= 0:
                    name = input("Quel est le Nom Tournoi (obligatoire): ")

                place = input("lieu du Tournoi:")
                while len(place) <= 0:
                    place = input("Lieu du Tournoi (Obligatoire): ")

                print("Contrôle du temps:")
                print("1.Bullet")
                print("2.Blitz")
                print("3.Coup rapide")
                time_control = input(
                    "Choisissez le contrôle du temps (Entrez un numéro):"
                )
                while len(time_control) <= 0:
                    time_control = input("Contrôle du temps (Obligatoire):")
                if time_control == "1":
                    time_control = "Bullet"
                elif time_control == "2":
                    time_control = "Blitz"
                elif time_control == "3":
                    time_control = "Coup rapide"
                else:
                    print(
                        "Le tournoi sera contrôler en Bullet"
                    )
                    time_control = "Bullet"

                new_tournament = Tournament(
                    name, place, time_control, player_list=[], tour_list=[]
                )
                print("Création du nouveau Tournoi '{}'".format(name))
                show_tournament_informations(
                    new_tournament.name,
                    new_tournament.place,
                    new_tournament.time_control,
                    new_tournament.date,
                    new_tournament.NUMBER_OF_PLAYERS,
                    new_tournament.NUMBER_OF_ROUNDS,
                )

                for elt in self.tournament_player_list:
                    new_tournament.player_list.append(elt)
                self.tournament_player_list.clear()

                print("Nous allons commencer le tirage au sort...")
                sleep(2)

                rank_player(new_tournament.player_list)
                for i in range(new_tournament.NUMBER_OF_ROUNDS):
                    tournament_round(
                        new_tournament,
                        new_tournament.player_list,
                        self.match_list,
                        self.tournament_match,
                        self.match_list_tuple,
                    )
                    self.continuer(new_tournament)
                    self.change_ranking()

                ranking = sorted(new_tournament.player_list,
                                 key=attrgetter("rank"))
                print("Le vainqueur du tournoi est {}".format(ranking[0]))
                resume = input("Quelles sont vos remarques sur ce Tournoi: ")
                new_tournament.description = resume
                self.tournament_list.append(new_tournament)
                new_tournament.save_tournament()

                self.tournament_match.clear()
                self.back_to_main_page()

        elif tournament_choice == "2":
            self.choose_three_continue()

    def choose_three_continue(self):
        if len(self.tournament_list) == 0:
            print("Il n'y a pas de Tournoi enregister")
            self.back_to_main_page()
        else:
            for tournament in self.tournament_list:
                index = self.tournament_list.index(tournament)
                if len(tournament.tour_list) < Tournament.NUMBER_OF_ROUNDS:
                    print(index, tournament.name)

            choose_tournament = input(
                "Quel tournoi voulez-vous continuer ? (entrez son numéro):"
            )
            tournament = self.tournament_list[int(choose_tournament)]
            print(
                "Nous reprenons le tournoi {} à partir du round {}".format(
                    tournament.name, len(tournament.tour_list) + 1
                )
            )

            rank_player(tournament.player_list)
            for i in range(
                    tournament.NUMBER_OF_ROUNDS - len(tournament.tour_list)
            ):
                tournament_round(
                    tournament,
                    tournament.player_list,
                    self.match_list,
                    self.tournament_match,
                    self.match_list_tuple,
                )
                self.continuer(tournament)
                self.change_ranking()

            ranking = sorted(tournament.player_list, key=attrgetter("rank"))
            print("Le vainqueur du tournoi est {}".format(ranking[0]))
            resume = input("Quelles sont vos remarques sur ce Tournoi: ")
            tournament.description = resume
            tournament.save_tournament()

            self.tournament_list.append(tournament)
            self.tournament_match.clear()
            self.back_to_main_page()

    def choose_four(self):
        # Liste des Tournois
        if len(self.tournament_list) == 0:
            print("Aucun Tournoi enregistrer")
            self.back_to_main_page()
        else:
            print("Voici la liste des Tournois:")
            check_tournament_list(self.tournament_list)
            self.back_to_main_page()

    def choose_five(self):
        # Quitter
        print("GAMESET ET MAT ! CIAO")
        sys.exit()

    def continuer(self, tournament):
        """Use to check if you want to continue the tournament or save"""
        continuer = input(
            "Voulez-vous continuer ?\
    1.Oui/2.Non:"
        )

        if continuer == "2":
            tournament.save_tournament()
            print("Sauvegarde du tournoi {} effectué".format(tournament.name))
            tournament_main_page()
            self.choose()

        elif continuer == "1":
            print("THE SHOW GOES ON ! ")

    def change_ranking(self):
        """Use if you want to change a player rank during a tournament"""
        change = input(
            "Changer le classement général d'un joueur ? 1.Oui/2.Non:"
        )

        if change == "1":
            number = input(
                "Combien de classement voulez vous changer (Entrez un numéro):"
            )
            for i in range(int(number)):
                update_player_rank(self.player_list)

        elif change == "2":
            pass

    def back_to_main_page(self):
        """Print Main menu"""
        tournament_main_page()
        self.choose()
