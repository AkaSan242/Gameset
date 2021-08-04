"""Base Tournament view"""


class TournamentView:
    """Gameset Tournament view"""

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
        print("Tournoi:'{}' Lieu:'{}' Date:'{}' Participants:'{}' Rounds:'{}' Contrôle du temps:'{}' ".format
              (name,
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
