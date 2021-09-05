"""Define the main controller"""
import datetime
import sys
from operator import attrgetter
from tinydb import TinyDB, Query
from time import sleep

# Controllers
from .tournamentcontroller import *
from .playercontroller import *

# Models
from models.tournament import Tournament
from models.player import Player
from models.tour import Tour

# Views
from views.playerview import *
from views.tournamentview import *
from views.tourview import *

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
            self.player_list.append(Player(name, last_name, birth_date, gender, rank))

        # Get tournament from database
        serialized_tournament = tournament_table.all()
        for i in range(len(serialized_tournament)):
            name = serialized_tournament[i]["name"]
            place = serialized_tournament[i]["place"]
            date = serialized_tournament[i]["date"]
            new_date = datetime.datetime.fromtimestamp(int(date))
            number_of_players = serialized_tournament[i]["number of players"]
            number_of_rounds = serialized_tournament[i]["number of rounds"]
            time_control = serialized_tournament[i]["time controle"]
            description = serialized_tournament[i]["description"]

            json_tournament = Tournament(
                name,
                place,
                time_control,
                tour_list=[],
                player_list=[],
                date=new_date,
                player_numbers=number_of_players,
                number_of_rounds=number_of_rounds,
                description=description

            )
            for l in range(number_of_players):
                player_name = serialized_tournament[i]["player {}".format(l + 1)]["name"]
                player_last_name = serialized_tournament[i]["player {}".format(l + 1)]["last name"]
                player_birth_date = serialized_tournament[i]["player {}".format(l + 1)]["birth date"]
                player_gender = serialized_tournament[i]["player {}".format(l + 1)]["gender"]
                player_rank = serialized_tournament[i]["player {}".format(l + 1)]["rank"]
                player_score = serialized_tournament[i]["player {}".format(l + 1)]["score"]

                player = Player(player_name,
                                player_last_name,
                                player_birth_date,
                                player_gender,
                                player_rank,
                                player_score)
                json_tournament.player_list.append(player)

            for h in range(number_of_rounds):
                round_name = serialized_tournament[i]["Round {}".format(h + 1)]["name"]
                round_match = serialized_tournament[i]["Round {}".format(h + 1)]["match list"]
                round_start = serialized_tournament[i]["Round {}".format(h + 1)]["start"]
                round_end = serialized_tournament[i]["Round {}".format(h + 1)]["end"]

                round = Tour(match_list=round_match,
                             name=round_name,
                             beginning_time=round_start,
                             ending_time=round_end)
                json_tournament.tour_list.append(round)

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
        number = input("Combien de Joueurs voulez vous ajouter ? (entrez un numéro):")
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
                "Vous voulez la liste des Joueurs par 1.Ordre Alphabétique/2.Classement:"
            )

            if search_by == "1":
                search_player_by_name(self.player_list)
                update = input(
                    "Voulez-vous modifier les informations d'un joueur ? 1.Oui/2.Non:"
                )
                if update == "1":
                    update_delete_player(self.player_list)
                    self.back_to_main_page()

                elif update == "2":
                    self.back_to_main_page()

            elif search_by == "2":
                search_player_by_rank(self.player_list)
                update = input(
                    "Voulez-vous modifier les informations d'un joueur ? 1.Oui/2.Non:"
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
                    "Il n'y a pas assez de joueurs disponible pour un tournoi (Requis:'{}' Disponible:'{}')".format(
                        Tournament.NUMBER_OF_PLAYERS, len(self.player_list)
                    )
                )

                add = input(
                    "Voulez-vous ajouter les participants maintenant ? 1.Oui/2.Non:"
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
                while len(self.tournament_player_list) < Tournament.NUMBER_OF_PLAYERS:
                    choose_a_player(self.player_list, self.tournament_player_list)
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
                        "Vu que vous n'avez rien choisi par défaut le tournoi sera contrôler en Bullet"
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
                new_tournament.serialized_tournament['name'] = new_tournament.name
                new_tournament.serialized_tournament['place'] = new_tournament.place
                new_tournament.serialized_tournament['date'] = new_tournament.date
                new_tournament.serialized_tournament['time controle'] = new_tournament.time_control
                new_tournament.serialized_tournament['number of players'] = new_tournament.NUMBER_OF_PLAYERS
                new_tournament.serialized_tournament['number of rounds'] = new_tournament.NUMBER_OF_ROUNDS
                for i in range(new_tournament.NUMBER_OF_ROUNDS):
                    new_tournament.serialized_tournament["Round {}".format(i + 1)] = {"name": "",
                                                                                      "match list": "",
                                                                                      "start": "",
                                                                                      "end": ""}

                for elt in self.tournament_player_list:
                    new_tournament.player_list.append(elt)
                for i in range(len(new_tournament.player_list)):
                    serialized_player = {
                        "name": new_tournament.player_list[i].name,
                        "last name": new_tournament.player_list[i].last_name,
                        "birth date": new_tournament.player_list[i].birth_date,
                        "gender": new_tournament.player_list[i].gender,
                        "rank": new_tournament.player_list[i].rank,
                        "score": new_tournament.player_list[i].score
                    }
                    new_tournament.serialized_tournament['player {}'.format(i + 1)] = serialized_player

                print("Nous allons commencer le tirage au sort...")
                sleep(2)

                rank_player(self.tournament_player_list)
                for i in range(new_tournament.NUMBER_OF_ROUNDS):
                    tournament_round(
                        new_tournament,
                        self.tournament_player_list,
                        self.match_list,
                        self.tour_list,
                        self.tournament_match,
                        self.match_list_tuple,
                    )
                    self.continuer(new_tournament)
                    self.change_ranking()

                ranking = sorted(self.tournament_player_list, key=attrgetter("rank"))
                print("Le vainqueur du tournoi est {}".format(ranking[0]))
                resume = input(
                    "Quelles sont vos remarques sur ce Tournoi {}: ".format(
                        new_tournament.name
                    )
                )
                new_tournament.description = resume
                self.tournament_list.append(new_tournament)
                new_tournament.serialized_tournament['description'] = new_tournament.description
                new_tournament.save_tournament()

                for elt in self.tournament_player_list:
                    elt.score = 0

                self.tournament_player_list.clear()
                self.tournament_match.clear()
                self.tour_list.clear()
                self.back_to_main_page()

        elif tournament_choice == "2":
            if len(self.tournament_list) == 0:
                print("Il n'y a pas de Tournoi enregister")
                self.back_to_main_page()
            else:
                for tournament in self.tournament_list:
                    index = self.tournament_list.index(tournament)
                    if len(tournament.tour_list) < Tournament.NUMBER_OF_ROUNDS:
                        print("{}.{}".format(index, tournament.name))

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
                for i in range(tournament.NUMBER_OF_ROUNDS - len(tournament.tour_list)):
                    tournament_round(
                        tournament,
                        tournament.player_list,
                        self.match_list,
                        tournament.tour_list,
                        self.tournament_match,
                        self.match_list_tuple,
                    )
                    self.continuer(tournament)
                    self.change_ranking()

                ranking = sorted(tournament.player_list, key=attrgetter("rank"))
                print("Le vainqueur du tournoi est {}".format(ranking[0]))
                resume = input(
                    "Quelles sont vos remarques sur ce Tournoi {}: ".format(
                        tournament.name
                    )
                )
                tournament.description = resume
                tournament.serialized_tournament['description'] = tournament.description
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
            "Voulez changer le classement général d'un ou plusieurs joueurs  ? 1.Oui/2.Non:"
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
