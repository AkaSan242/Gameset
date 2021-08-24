"""Base tour controller"""
from tinydb import TinyDB, Query
db = TinyDB('db.json')
match_table = db.table('Match list')

from operator import attrgetter
from views.tourview import TourView


class TourController(TourView):
    """Tournament Tour controller
    Player_list:
    the player list is use to sorte player by rank to define all match of a round and add them in the match list

     Match_list:
     the match list is use to print all matchs of the current round

     Tournament match:
     this is a list of all the match played in the current tournament,
      we use it when a new round start to compare with the match list and check if two player had already made a match

     Gameset match list:
     this list is a record of the tuple of each match played in the gameset application """

    def first_match(self, player_list, match_list, tournament_match):
        """define the matchs of the first round only:
        -Player 1 vs 5
        -Player 2 VS 6
        -Player 3 VS 7
        -Player 4 VS 8"""

        new_ranking = sorted(player_list, key=attrgetter('rank'))

        # Fisrt macth
        player_one = ["{}, {}".format(new_ranking[0], new_ranking[0].score)]
        player_two = ["{}, {}".format(new_ranking[4], new_ranking[4].score)]
        match_one_tuple = ("{}{}".format(player_one, player_two))
        match_one = "{} vs {}".format(new_ranking[0].name, new_ranking[4].name)
        match_one_reverse = "{} vs {}".format(new_ranking[4].name, new_ranking[0].name)

        # Second match
        player_three = ["{}, {}".format(new_ranking[1], new_ranking[1].score)]
        player_four = ["{}, {}".format(new_ranking[5], new_ranking[5].score)]
        match_two_tuple = ("{}{}".format(player_three, player_four))
        match_two = "{} vs {}".format(new_ranking[1].name, new_ranking[5].name)
        match_two_reverse = "{} vs {}".format(new_ranking[5].name, new_ranking[1].name)

        # Third match
        player_five = ["{}, {}".format(new_ranking[2], new_ranking[2].score)]
        player_six = ["{}, {}".format(new_ranking[6], new_ranking[6].score)]
        match_three_tuple = ("{}{}".format(player_five, player_six))
        match_three = "{} vs {}".format(new_ranking[2].name, new_ranking[6].name)
        match_three_reverse = "{} vs {}".format(new_ranking[6].name, new_ranking[2].name)

        # Fourth match
        player_seven = ["{}, {}".format(new_ranking[3], new_ranking[3].score)]
        player_eight = ["{}, {}".format(new_ranking[7], new_ranking[7].score)]
        match_four_tuple = ("{}{}".format(player_seven, player_eight))
        match_four = "{} vs {}".format(new_ranking[3].name, new_ranking[7].name)
        match_four_reverse = "{} vs {}".format(new_ranking[7].name, new_ranking[3].name)

        match_list.append(match_one)
        match_list.append(match_two)
        match_list.append(match_three)
        match_list.append(match_four)

        tournament_match.append(match_one)
        tournament_match.append(match_one_reverse)
        match_table.insert(match_one_tuple)

        tournament_match.append(match_two)
        tournament_match.append(match_two_reverse)
        match_table.insert(match_two_tuple)

        tournament_match.append(match_three)
        tournament_match.append(match_three_reverse)
        match_table.insert(match_three_tuple)

        tournament_match.append(match_four)
        tournament_match.append(match_four_reverse)
        match_table.insert(match_four_tuple)

    def tournament_match_set(self, player_list, match_list, tournament_match):
        """Same as first round but for all round of a Tournament:
        -Player 1 vs 2
        -Player 3 vs 4
        -Player 5 vs 6
        -Player 7 vs 8"""

        new_ranking = sorted(player_list, key=attrgetter('rank'))

        # First match
        player_one = ["{}, {}".format(new_ranking[0], new_ranking[0].score)]
        player_two = ["{}, {}".format(new_ranking[1], new_ranking[1].score)]
        match_one_tuple = ("{}{}".format(player_one, player_two))
        match_one = "{} vs {}".format(new_ranking[0].name, new_ranking[1].name)
        match_one_reverse = "{} vs {}".format(new_ranking[1].name, new_ranking[0].name)

        # Second match
        player_three = ["{}, {}".format(new_ranking[2], new_ranking[2].score)]
        player_four = ["{}, {}".format(new_ranking[3], new_ranking[3].score)]
        match_two_tuple = ("{}{}".format(player_three, player_four))
        match_two = "{} vs {}".format(new_ranking[2].name, new_ranking[3].name)
        match_two_reverse = "{} vs {}".format(new_ranking[3].name, new_ranking[2].name)

        # Third match
        player_five = ["{}, {}".format(new_ranking[4], new_ranking[4].score)]
        player_six = ["{}, {}".format(new_ranking[5], new_ranking[5].score)]
        match_three_tuple = ("{}{}".format(player_five, player_six))
        match_three = "{} vs {}".format(new_ranking[4].name, new_ranking[5].name)
        match_three_reverse = "{} vs {}".format(new_ranking[5].name, new_ranking[4].name)

        # Fourth match
        player_seven = ["{}, {}".format(new_ranking[6], new_ranking[6].score)]
        player_eight = ["{}, {}".format(new_ranking[7], new_ranking[7].score)]
        match_four_tuple = ("{}{}".format(player_seven, player_eight))
        match_four = "{} vs {}".format(new_ranking[6].name, new_ranking[7].name)
        match_four_reverse = "{} vs {}".format(new_ranking[7].name, new_ranking[6].name)

        match_list.append(match_one)
        match_list.append(match_two)
        match_list.append(match_three)
        match_list.append(match_four)

        # Check if a match was already played
        if match_one in tournament_match:
            print("{} a déja été jouer".format(match_one))
            print("On refait le tirage")
            self.check_match(player_list, match_list, tournament_match)

        elif match_two in tournament_match:
            print("{} a déja été jouer".format(match_two))
            print("On refait le tirage")
            self.check_match(player_list, match_list, tournament_match)

        elif match_three in tournament_match:
            print("{} a déja été jouer".format(match_three))
            print("On refait le tirage")
            self.check_match(player_list, match_list, tournament_match)

        elif match_four in tournament_match:
            print("{} a déja été jouer".format(match_four))
            print("On refait le tirage")
            self.check_match(player_list, match_list, tournament_match)

        else:
            tournament_match.append(match_one)
            tournament_match.append(match_one_reverse)
            match_table.insert(match_one_tuple)

            tournament_match.append(match_two)
            tournament_match.append(match_two_reverse)
            match_table.insert(match_two_tuple)

            tournament_match.append(match_three)
            tournament_match.append(match_three_reverse)
            match_table.insert(match_three_tuple)

            tournament_match.append(match_four)
            tournament_match.append(match_four_reverse)
            match_table.insert(match_four_tuple)

    def tournament_rematch(self, player_list, match_list, tournament_match):
        """Redefine all match for a round:
        -Player 1 vs 3
        -Player 2 vs 4
        -Player 5 vs 7
        -Player 6 vs 8"""

        match_list.clear()

        new_ranking = sorted(player_list, key=attrgetter('rank'))

        player_one = ["{}, {}".format(new_ranking[0], new_ranking[0].score)]
        player_two = ["{}, {}".format(new_ranking[2], new_ranking[2].score)]
        match_one_tuple = ("{}{}".format(player_one, player_two))
        match_one = "{} vs {}".format(new_ranking[0].name, new_ranking[2].name)
        match_one_reverse = "{} vs {}".format(new_ranking[2].name, new_ranking[0].name)

        player_three = ["{}, {}".format(new_ranking[1], new_ranking[1].score)]
        player_four = ["{}, {}".format(new_ranking[3], new_ranking[3].score)]
        match_two_tuple = ("{}{}".format(player_three, player_four))
        match_two = "{} vs {}".format(new_ranking[1].name, new_ranking[3].name)
        match_two_reverse = "{} vs {}".format(new_ranking[3].name, new_ranking[1].name)

        player_five = ["{}, {}".format(new_ranking[4], new_ranking[4].score)]
        player_six = ["{}, {}".format(new_ranking[6], new_ranking[6].score)]
        match_three_tuple = ("{}{}".format(player_five, player_six))
        match_three = "{} vs {}".format(new_ranking[4].name, new_ranking[6].name)
        match_three_reverse = "{} vs {}".format(new_ranking[6].name, new_ranking[4].name)

        player_seven = ["{}, {}".format(new_ranking[5], new_ranking[5].score)]
        player_eight = ["{}, {}".format(new_ranking[7], new_ranking[7].score)]
        match_four_tuple = ("{}{}".format(player_seven, player_eight))
        match_four = "{} vs {}".format(new_ranking[5].name, new_ranking[7].name)
        match_four_reverse = "{} vs {}".format(new_ranking[7].name, new_ranking[5].name)

        match_list.append(match_one)
        match_list.append(match_two)
        match_list.append(match_three)
        match_list.append(match_four)

        # Check if a match was already played
        if match_one in tournament_match:
            print("{} a déja été jouer".format(match_one))
            print("On refait le tirage")
            match_list.clear()
            self.recheck_match(player_list, match_list, tournament_match)

        elif match_two in tournament_match:
            print("{} a déja été jouer".format(match_two))
            print("On refait le tirage")
            match_list.clear()
            self.recheck_match(player_list, match_list, tournament_match)

        elif match_three in tournament_match:
            print("{} a déja été jouer".format(match_three))
            print("On refait le tirage")
            match_list.clear()
            self.recheck_match(player_list, match_list, tournament_match)

        elif match_four in tournament_match:
            print("{} a déja été jouer".format(match_four))
            print("On refait le tirage")
            match_list.clear()
            self.recheck_match(player_list, match_list, tournament_match)

        else:
            tournament_match.append(match_one)
            tournament_match.append(match_one_reverse)
            match_table.insert(match_one_tuple)

            tournament_match.append(match_two)
            tournament_match.append(match_two_reverse)
            match_table.insert(match_two_tuple)

            tournament_match.append(match_three)
            tournament_match.append(match_three_reverse)
            match_table.insert(match_three_tuple)

            tournament_match.append(match_four)
            tournament_match.append(match_four_reverse)
            match_table.insert(match_four_tuple)

    def check_match(self, player_list, match_list, tournament_match):
        """check if a match alreday made"""
        print("Contrôle des matchs...")
        self.tournament_rematch(player_list, match_list, tournament_match)

    def recheck_match(self, player_list, match_list, tournament_match):
        """check if a match alreday made"""
        print("Contrôle des matchs...")
        self.first_match(player_list, match_list, tournament_match)




