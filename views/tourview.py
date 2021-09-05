"""Base tour view"""

from operator import attrgetter
from time import sleep, strftime
from models.tour import Tour
from models.tournament import Tournament
from .tournamentview import *
from .playerview import *
from controllers.tourcontroller import *
from controllers.playercontroller import *


def tournament_round(
        tournament, player_list, match_list, tour_list, tournament_match, match_list_tuple
    ):
    """Define tournament round"""
    if len(tour_list) == 0:
        round_number = 1
        round_name = "Round {}".format(round_number)

        first_match(
            player_list, match_list, tournament_match, match_list_tuple
        )
        print(round_name)
        tour = Tour(match_list=[], name=round_name)
        for i in range(len(match_list_tuple)):
            tour.match_list.append(match_list_tuple[i])

        show_tournament_match(match_list_tuple)
        start = strftime("%Y %m %d %H:%M")
        tour.beginning_time = start
        sleep(2)

        update_player_score(player_list)
        end = strftime("%Y %m %d %H:%M")
        tour.ending_time = end
        tour_list.append(tour)
        tournament.tour_list.append(tour)
        serialized_tour = {
            "name": tour.name,
            "match list": tour.match_list,
            "start": tour.beginning_time,
            "end": tour.ending_time,

        }

        show_players_status(player_list)
        sleep(2)

        print("Classement:")
        player_ranking(player_list)
        sleep(1)
        match_list.clear()
        match_list_tuple.clear()

        new_ranking = sorted(player_list, key=attrgetter("score"), reverse=True)
        for i in range(len(new_ranking)):
            serialized_player = {
                "name": new_ranking[i].name,
                "last name": new_ranking[i].last_name,
                "birth date": new_ranking[i].birth_date,
                "gender": new_ranking[i].gender,
                "rank":new_ranking[i].rank,
                "score": new_ranking[i].score
            }
            tournament.serialized_tournament['player {}'.format(i + 1)] = serialized_player

    elif len(tour_list) > 0:
        round_number = len(tour_list) + 1
        round_name = "Round {}".format(round_number)

        tournament_match_set(
            player_list, match_list, tournament_match, match_list_tuple
        )
        print(round_name)
        tour = Tour(match_list=[], name=round_name)
        for i in range(len(match_list_tuple)):
            tour.match_list.append(match_list_tuple[i])

        show_tournament_match(match_list_tuple)
        start = strftime("%Y %m %d %H:%M")
        tour.beginning_time = start
        sleep(2)

        update_player_score(player_list)
        end = strftime("%Y %m %d %H:%M")
        tour.ending_time = end
        tour_list.append(tour)
        tournamment.tour_list.append(tour)
        serialized_tour = {
            "name": tour.name,
            "match list": tour.match_list,
            "start": tour.beginning_time,
            "end": tour.ending_time,

        }
        tournament.serialized_tournament['{}'.format(round_name)] = serialized_tour

        show_players_status(player_list)
        sleep(2)

        print("Classement:")
        player_ranking(player_list)
        sleep(1)
        match_list.clear()
        match_list_tuple.clear()

        new_ranking = sorted(player_list, key=attrgetter("score"), reverse=True)
        for i in range(len(new_ranking)):
            serialized_player = {
                "name": new_ranking[i].name,
                "last name": new_ranking[i].last_name,
                "birth date": new_ranking[i].birth_date,
                "gender": new_ranking[i].gender,
                "rank": new_ranking[i].rank,
                "score": new_ranking[i].score
            }
            tournament.serialized_tournament['player {}'.format(i + 1)] = serialized_player