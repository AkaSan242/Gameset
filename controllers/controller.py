"""Define the main controller"""
import sys
from operator import attrgetter
from tinydb import TinyDB, Query
db = TinyDB('db.json')
players_table = db.table('players')
tournament_table = db.table('tournament')
match_table = db.table('Match list')

from models.tournament import Tournament
from models.player import Player
from time import sleep
from .tournamentcontroller import TournamentController


class Controller(TournamentController):
    """Gameset Main Controller"""
    def __init__(self,
                 player_list, tournament_list,
                 tournament_player_list, match_list,
                 tour_list, tournament_match_list,
                 gameset_match_list):

        self.player_list = player_list
        self.tournament_list = tournament_list
        self.tournament_player_list = tournament_player_list
        self.tour_list = tour_list
        self.match_list = match_list
        self.tournament_match = tournament_match_list
        self.gameset_match_list = gameset_match_list

        # Get players from database
        serialized_players = players_table.all()
        for i in range(len(serialized_players)):
            name = serialized_players[i]['name']
            last_name = serialized_players[i]['last name']
            birth_date = serialized_players[i]['birth date']
            gender = serialized_players[i]['gender']
            rank = serialized_players[i]['rank']
            self.player_list.append(Player(name, last_name, birth_date, gender, rank))

        # Get tournament from database
        serialized_tournament = tournament_table.all()
        for i in range(len(serialized_tournament)):
            name = serialized_tournament[i]['name']
            place = serialized_tournament[i]['place']
            date = serialized_tournament[i]['date']
            number_of_players = serialized_tournament[i]['player number']
            number_of_rounds = serialized_tournament[i]['number of rounds']
            time_control = serialized_tournament[i]['time control']
            description = serialized_tournament[i]['description']
            tour_list = serialized_tournament[i]['rounds']
            tournament_players = serialized_tournament[i]['participants']
            self.tournament_list.append(Tournament(name, place, time_control,
                                                   tour_list, tournament_players,
                                                   date, number_of_players,
                                                   number_of_rounds, description))

        # Get all match played in gameset from database
        serialized_match = match_table.all()
        for elt in serialized_match:
            self.gameset_match_list.append(elt)

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
                search_by = input("Vous voulez la liste des Joueurs par 1.Ordre Alphabétique/2.Classement:")

                if search_by == "1":
                    self.search_player_by_name(self.player_list)
                    update = input("Voulez-vous modifier les informations d'un joueur ? 1.Oui/2.Non:")
                    if update == "1":
                        self.update_delete_player(self.player_list)
                        self.back_to_main_page()
                    elif update == "2":
                        self.back_to_main_page()

                elif search_by == "2":
                    self.search_player_by_rank(self.player_list)
                    update = input("Voulez-vous modifier les informations d'un joueur ? 1.Oui/2.Non:")
                    if update == "1":
                        self.update_delete_player(self.player_list)
                        self.back_to_main_page()
                    elif update == "2":
                        self.back_to_main_page()
        # Commencer un Tournoi
        elif choice == "3":
            self.start_continue_tournament()
            tournament_choice = input()
            if tournament_choice == "1":

                if len(self.player_list) < Tournament.NUMBER_OF_PLAYERS:
                    print("Il n'y a pas assez de joueurs disponible pour un tournoi (Requis:'{}' Disponible:'{}')".format
                      (Tournament.NUMBER_OF_PLAYERS, len(self.player_list)))

                    add = input("Voulez-vous ajouter les participants maintenant ? 1.Oui/2.Non:")
                    if add == "1":
                        for i in range(Tournament.NUMBER_OF_PLAYERS):
                            self.add_a_new_player(self.player_list)
                        self.back_to_main_page()
                    elif add == "2":
                        self.back_to_main_page()

                else:
                    while len(self.tournament_player_list) < Tournament.NUMBER_OF_PLAYERS:
                        self.choose_a_player(self.player_list, self.tournament_player_list)
                        print("Ajout d'un nouveau joueur {} sur {}".format(len(self.tournament_player_list),
                                                                           Tournament.NUMBER_OF_PLAYERS))

                sleep(2)
                self.show_players(self.tournament_player_list)
                sleep(2)

                name = input("Quel est le Nom du Tournoi:")
                while len(name) <= 0:
                    name = input("Quel est le Nom Tournoi (obligatoire): ")

                place = input("lieu du Tournoi:")
                while len(place) <= 0:
                    place = input("Lieu du Tournoi (Obligatoire): ")

                time_control = input("Controle du temps (Bullet, Blitz ou Coup Rapide):")
                while len(time_control) <= 0:
                    time_control = input("Contrôle du temps (Obligatoire):")

                new_tournament = Tournament(name, place, time_control, player_list=[], tour_list=[])
                print("Création du nouveau Tournoi '{}'".format(name))
                self.show_tournament_informations(
                    new_tournament.name,
                    new_tournament.place,
                    new_tournament.time_control,
                    new_tournament.date,
                    new_tournament.NUMBER_OF_PLAYERS,
                    new_tournament.NUMBER_OF_ROUNDS)

                print("Nous allons commencer le tirage au sort...")
                sleep(2)

                self.rank_player(self.tournament_player_list)
                for i in range(new_tournament.NUMBER_OF_ROUNDS):
                    self.tournament_round(self.tournament_player_list,
                                          self.match_list, self.tour_list,
                                          self.tournament_match, self.gameset_match_list)
                    self.continuer(new_tournament)
                    self.change_ranking()

                for elt in self.tournament_player_list:
                    new_tournament.player_list.append(elt)

                for elt in self.tour_list:
                    new_tournament.tour_list.append(elt)

                ranking = sorted(self.tournament_player_list, key=attrgetter('rank'))
                print("Le vainqueur du tournoi est {}".format(ranking[0]))
                resume = input("Quelles sont vos remarques sur ce Tournoi {}: ".format(new_tournament.name))
                new_tournament.description = resume
                new_tournament.serialized_tournament()

                self.tournament_list.append(new_tournament)
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
                        if len(tournament.tour_list) < Tournament.number_of_rounds:
                            print("{}.{}".format(index, tournament.name))

                    choose_tournament = input("Quel tournoi voulez-vous continuer ? (entrez son numéro):")
                    tournament = self.tournament_list[int(choose_tournament)]
                    print("Nous reprenons le tournoi {} à partir du round {}".format(tournament.name,
                          len(tournament.tour_list) + 1))

                    self.rank_player(tournament.player_list)
                    for i in range(tournament.NUMBER_OF_ROUNDS - len(tournament.tour_list)):
                        self.tournament_round(tournament.player_list,
                                              self.match_list, tournament.tour_list,
                                              self.tournament_match, self.gameset_match_list)
                        self.continuer(tournament)
                        self.change_ranking()

                    for elt in self.tour_list:
                        tournament.tour_list.append(elt)

                    ranking = sorted(tournament.player_list, key=attrgetter('rank'))
                    print("Le vainqueur du tournoi est {}".format(ranking[0]))
                    resume = input("Quelles sont vos remarques sur ce Tournoi {}: ".format(tournament.name))
                    tournament.description = resume
                    tournament.serialized_tournament()

                    self.tournament_list.append(tournament)
                    self.tournament_match.clear()
                    self.back_to_main_page()

        # Liste des Tournois
        elif choice == "4":
            if len(self.tournament_list) == 0:
                print("Aucun Tournoi enregistrer")
                self.back_to_main_page()
            else:
                print("Voici la liste des Tournois:")
                self.check_tournament_list(self.tournament_list)
                self.back_to_main_page()

        # Liste des Matchs
        elif choice == "5":
            if len(self.gameset_match_list) == 0:
                print("Aucun match n'a été jouer")
                self.back_to_main_page()
            else:
                print("Voici la liste des matchs jouer dans gameset")
                for elt in self.gameset_match_list:
                    print(elt)
                self.back_to_main_page()

        # Quitter
        elif choice == "6":
            print("GAMESET ET MAT ! CIAO")
            sys.exit()

    def continuer(self, tournament):
        """Use to check if you want to continue the tournament or save"""
        continuer = input("Voulez-vous continuer ?\
    1.Oui/2.Non:")

        if continuer == "2":
            tournament.serialized_tournament()
            print("Sauvegarde du tournoi {} effectué".format(tournament.name))
            self.tournament_main_page()
            self.choose()

        elif continuer == "1":
            print("THE SHOW GOES ON ! ")

    def change_ranking(self):
        """Use if you want to change a player rank during a tournament"""
        change = input("Voulez changer le classement général d'un ou plusieurs joueurs  ? 1.Oui/2.Non:")

        if change == "1":
            number = input("Combien de classement voulez vous changer (Entrez un numéro):")
            for i in range(int(number)):
                self.update_player_rank(self.player_list)

        elif change == "2":
            pass

    def back_to_main_page(self):
        """Print Main menu"""
        self.tournament_main_page()
        self.choose()










