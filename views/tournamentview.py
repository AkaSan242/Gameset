"""Base Tournament view"""

from operator import attrgetter


class TournamentView:
    """Gameset Tournament view"""

    def rank_player(self, players, ranks):
        """ranking players for match"""
        i = 1
        for player in players:
            ranks["{}".format(i)] = player
            i += 1

    def player_ranking(self, player_list, ranks):
        """Ranking player by score"""
        new_ranking = sorted(player_list, key=attrgetter('score'), reverse=True)
        i = 1
        for elt in new_ranking:
            print("{}.{}".format(i, elt))
            i += 1
        self.rank_player(new_ranking, ranks)

    def show_tournament_informations(self, name, place, time_control, date, player_numbers, number_of_rounds):
        """Show tournament information"""
        print("Tournoi:'{}' Lieu:'{}' Date:'{}' Participants:'{}' Rounds:'{}' Contrôle du temps:'{}' ".format
              (name,
               place,
               date,
               player_numbers,
               number_of_rounds,
               time_control))

    def first_match(self, ranks, match_list):
        """define the match of the first round only"""
        print("C'est l'heure de définir les premiers matchs du tournoi:")
        match_one = "{} vs {}".format(ranks["1"], ranks["5"])
        match_two = "{} vs {}".format(ranks["2"], ranks["6"])
        match_three = "{} vs {}".format(ranks["3"], ranks["7"])
        match_four = "{} vs {}".format(ranks["4"], ranks["8"])

        match_list.append(match_one)
        match_list.append(match_two)
        match_list.append(match_three)
        match_list.append(match_four)

    def tournament_match(self, ranks, match_list):
        """define all matchs for a round"""
        match_one = "{} vs {}".format(ranks["1"], ranks["2"])
        match_two = "{} vs {}".format(ranks["3"], ranks["4"])
        match_three = "{} vs {}".format(ranks["5"], ranks["6"])
        match_four = "{} vs {}".format(ranks["7"], ranks["8"])

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
        print("4.Liste des Tournois")
        print("5.Quitter")

    def tournament_list_main_page(self, tournament_dict):
        """Print Tournament list Main menu"""
        print("Tournoi:'{}' Vainqueur:'{}' Date:'{}' Lieu:'{}'".format(tournament_dict['Nom'],
                                                                       tournament_dict['Vainqueur'],
                                                                       tournament_dict['Date'],
                                                                       tournament_dict['Lieu']))
        print("1.Liste des Participants")
        print("2.Listes des Rounds et Matchs")

