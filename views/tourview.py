"""Base tour view"""


from time import sleep, strftime
from models.tour import Tour
from views.tournamentview import TournamentView


class TourView(Tour):
    """Tour View"""

    def tournament_round(self, player_list, match_list, tour_list, tournament_match, gameset_match_list):
        """Define tournament round"""
        if len(tour_list) == 0:
            round_number = 1
            round_name = "Round {}".format(round_number)

            self.first_match(player_list, match_list, tournament_match, gameset_match_list)
            print(round_name)
            tour = Tour(match_list=[], name=round_name)
            for i in range(len(match_list)):
                tour.match_list.append(match_list[i])

            self.show_tournament_match(match_list)
            start = strftime("%Y %m %d %H:%M")
            tour.beginning_time = start
            sleep(5)

            self.update_player_score(player_list)
            end = strftime("%Y %m %d %H:%M")
            tour.ending_time = end
            tour_list.append(tour)

            self.show_players_status(player_list)
            sleep(3)

            print("Classement:")
            self.player_ranking(player_list)
            sleep(3)
            match_list.clear()

        elif len(tour_list) > 0:
            round_number = len(tour_list) + 1
            round_name = "Round {}".format(round_number)

            self.tournament_match_set(player_list, match_list, tournament_match, gameset_match_list)
            print(round_name)
            tour = Tour(match_list=[], name=round_name)
            for i in range(len(match_list)):
                tour.match_list.append(match_list[i])

            self.show_tournament_match(match_list)
            start = strftime("%Y %m %d %H:%M")
            tour.beginning_time = start
            sleep(5)

            self.update_player_score(player_list)
            end = strftime("%Y %m %d %H:%M")
            tour.ending_time = end
            tour_list.append(tour)

            self.show_players_status(player_list)
            sleep(3)

            print("Classement:")
            self.player_ranking(player_list)
            sleep(3)
            match_list.clear()