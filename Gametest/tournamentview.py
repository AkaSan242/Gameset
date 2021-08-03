"""Base Tournament view"""

from tournament import Tournament
from time import  sleep

class TournamentView:
    """Gameset Tournament view"""

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
        i = 0
        for elt in player_list:
            print("{}.{}".format(i, elt))
            i += 1

        choose_player = input("Choisissez un joueur (entrez son numéro):")
        player = player_list[int(choose_player)]
        print("Vous avez choisi:{}".format(player))
        sleep(2)
        tournament_players_list.append(player)

    def rank_player_sup(self, players, rank_sup):
        """Seperate players for match"""
        rank_sup["1"] = players[0]
        rank_sup["2"] = players[1]
        rank_sup["3"] = players[2]
        rank_sup["4"] = players[3]

    def rank_player_inf(self, players, rank_inf):
        """Seperate players for match"""
        rank_inf["5"] = players[4]
        rank_inf["6"] = players[5]
        rank_inf["7"] = players[6]
        rank_inf["8"] = players[7]

    def show_tournament_informations(self, name, place, time_control, date, player_numbers, number_of_rounds):
        """Show tournament information"""
        print("Tournoi:'{}' Lieu:'{}' Date:'{}' Participants:'{}' Rounds:'{}' Contrôle du temps:'{}' ".format(name,
                                                                                                              place,
                                                                                                              date,
                                                                                                    player_numbers,
                                                                                                  number_of_rounds,
                                                                                                    time_control))

    def first_match(self, rank_sup, rank_inf, match_list):
        """define the match of the first round only"""
        print("C'est l'heure de définir les premiers matchs du tournoi:")
        match_one = "{} vs {}".format(rank_sup["1"], rank_inf["5"])
        match_two = "{} vs {}".format(rank_sup["2"], rank_inf["6"])
        match_three = "{} vs {}".format(rank_sup["3"], rank_inf["7"])
        match_four = "{} vs {}".format(rank_sup["4"], rank_inf["8"])

        match_list.append(match_one)
        match_list.append(match_two)
        match_list.append(match_three)
        match_list.append(match_four)

    def tournament_match(self, rank_sup, rank_inf, match_list):
        """define all matchs for a round"""
        match_one = "{} vs {}".format(rank_sup["1"], rank_sup["2"])
        match_two = "{} vs {}".format(rank_sup["3"], rank_sup["4"])
        match_three = "{} vs {}".format(rank_inf["5"], rank_inf["6"])
        match_four = "{} vs {}".format(rank_inf["7"], rank_inf["8"])

        match_list.append(match_one)
        match_list.append(match_two)
        match_list.append(match_three)
        match_list.append(match_four)

    def show_tournament_match(self, match_list):
        """Show all matchs of the round"""
        print("Voici tout les matchs du prochain round:")
        for elt in match_list:
            print(elt)

    def tournament_main_page(self):
        """Print Main menu"""
        print("Menu Principal")
        print("1.Ajouter un Joueur")
        print("2.Liste des joueurs")
        print("3.Tournoi")
        print("4.Description")
        print("5.Quitter")
