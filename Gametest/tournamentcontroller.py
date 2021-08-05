"""Base Tournament Controller"""

from tournament import Tournament
from time import sleep
from tournamentview import TournamentView
from playercontroller import PlayerController


class TournamentController(TournamentView, PlayerController):
    """Gameset Tournament Controller"""

    def new_tournament(self, tournament_dic):
        """Start a new tournament"""
        name = input("Quel est le Nom du Tournoi:")
        place = input("lieu du Tournoi:")
        time_control = input("Controle du temps (Bullet, Blitz ou Coup Rapide):")

        new_tournament = Tournament(name, place, time_control)
        tournament_dic.update({"Nom": "{}".format(new_tournament.name),
                               "Lieu": "{}".format(new_tournament.place),
                               "Date": "{}".format(new_tournament.date),
                               "Contrôle du temps": "{}".format(new_tournament.time_control),
                               "Nombres de tours": "{}".format(new_tournament.NUMBER_OF_ROUNDS)})

        print("Création du nouveau Tournoi '{}'".format(name))
        TournamentView.show_tournament_informations(self,
                                                    name,
                                                    place,
                                                    time_control,
                                                    new_tournament.date,
                                                    new_tournament.NUMBER_OF_PLAYERS,
                                                    new_tournament.NUMBER_OF_ROUNDS)

    def choose_a_player(self, player_list, tournament_players_list):
        """Select a player for the tournament"""
        for elt in player_list:
            if elt not in tournament_players_list:
                index = player_list.index(elt)
                print("{}.{}".format(index, elt))

        print("Participants:{}".format(tournament_players_list))

        choose_player = input("Choisissez un joueur (entrez son numéro):")
        player = player_list[int(choose_player)]
        print("Vous avez choisi:{}".format(player))
        sleep(2)
        tournament_players_list.append(player)

    def tournament_round(self, player_list, ranks_dic, round_dic, match_list):
        """Define tournament round"""
        if len(round_dic) == 0:
            round_number = 1
            self.first_match(ranks_dic, match_list)
            self.show_tournament_match(match_list)
            sleep(5)
            round_dic["{}".format(round_number)] = str(match_list)
            self.update_player_score(player_list)
            self.show_players_status(player_list)
            sleep(3)
            print("Classement:")
            self.player_ranking(player_list, ranks_dic)
            sleep(5)
            match_list.clear()
        elif len(round_dic) > 0:
            round_number = len(ranks_dic) + 1
            self.tournament_match(ranks_dic, match_list)
            self.show_tournament_match(match_list)
            sleep(5)
            round_dic["{}".format(round_number)] = str(match_list)
            self.update_player_score(player_list)
            self.show_players_status(player_list)
            sleep(3)
            print("Classement:")
            self.player_ranking(player_list, ranks_dic)
            sleep(5)
            match_list.clear()