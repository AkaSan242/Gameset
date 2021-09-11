"""Base tour controller"""

from time import sleep, strftime
from operator import attrgetter

from .playercontroller import update_player_score
from models.tour import Tour
from views.tournamentview import show_tournament_match, player_ranking
from views.playerview import show_players_status


def first_match(player_list, match_list, tournament_match, match_list_tuple):
    """define the matchs of the first round only:
    -Player 1 vs 5
    -Player 2 VS 6
    -Player 3 VS 7
    -Player 4 VS 8

    -All match are 'Tuples' we create a tuple of a match between two players and add it in the match list.

    -Once all matchs are define we add them on the tournament match list.

    -'Tuples' are unique so for all matchs in match list we create a reverse 'Tuple' version of the match and add it in
    the tournament match list we'll use to check if there is a match 'A vs B' in the list,
    we can't have a match 'A vs B' or 'B vs A' on the next rounds because two players can't play together twice.

    -match list tuple is the list of the final version of each match use to save the tuple of the two players
    name and score
    """

    new_ranking = sorted(player_list, key=attrgetter("rank"))

    # Fisrt macth
    match_one = ([new_ranking[0]], [new_ranking[4]])
    match_one_reverse = ([new_ranking[4]], [new_ranking[0]])
    match_one_tuple = (
        [new_ranking[0], new_ranking[0].score],
        [new_ranking[4], new_ranking[4].score],
    )

    # Second match
    match_two = ([new_ranking[1]], [new_ranking[5]])
    match_two_reverse = ([new_ranking[5]], [new_ranking[1]])
    match_two_tuple = (
        [new_ranking[1], new_ranking[1].score],
        [new_ranking[5], new_ranking[5].score],
    )

    # Third match
    match_three = ([new_ranking[2]], [new_ranking[6]])
    match_three_reverse = ([new_ranking[6]], [new_ranking[2]])
    match_three_tuple = (
        [new_ranking[2], new_ranking[2].score],
        [new_ranking[6], new_ranking[6].score],
    )

    # Fourth match
    match_four = ([new_ranking[3]], [new_ranking[7]])
    match_four_reverse = ([new_ranking[7]], [new_ranking[3]])
    match_four_tuple = (
        [new_ranking[3], new_ranking[3].score],
        [new_ranking[7], new_ranking[7].score],
    )

    match_list.append(match_one)
    match_list.append(match_two)
    match_list.append(match_three)
    match_list.append(match_four)

    match_list_tuple.append(match_one_tuple)
    match_list_tuple.append(match_two_tuple)
    match_list_tuple.append(match_three_tuple)
    match_list_tuple.append(match_four_tuple)

    tournament_match.append(match_one)
    tournament_match.append(match_one_reverse)

    tournament_match.append(match_two)
    tournament_match.append(match_two_reverse)

    tournament_match.append(match_three)
    tournament_match.append(match_three_reverse)

    tournament_match.append(match_four)
    tournament_match.append(match_four_reverse)


def match_set(player_list, match_list, tournament_match, match_list_tuple):
    """Same as first match but for all other around:
    Player 1 vs 2
    Player 3 vs 4
    Player 5 vs 6
    Player 7 vs 8
    """
    generated_match = []
    inverse = 1
    j = 1
    while len(generated_match) == 0:
        new_ranking = sorted(
            player_list, key=attrgetter("rank"), reverse=not inverse % 2
        )
        generated_match = algo(
            j, new_ranking, len(player_list), tournament_match, match_list_tuple
        )
        if inverse % 2:
            j += 1
        inverse += 1
    for elt in generated_match:
        match_list.append(elt)


def algo(j, new_ranking, number_of_players, tournament_match, match_list_tuple):
    """Algo function is use to check all the match and redefine them if needed.
    for example:
    if player 1 and 2 have already played together then we try with player 3, 4 etc
     until we find a match never played in the tournament"""

    generated_match = []

    while len(generated_match) < number_of_players / 2:
        if j == len(new_ranking):
            return []
        # Define a match
        new_tuple = ([new_ranking[0]], [new_ranking[j]])
        new_tuple_reverse = ([new_ranking[j]], [new_ranking[0]])
        match_tuple = (
            [new_ranking[0], new_ranking[0].score],
            [new_ranking[j], new_ranking[j].score],
        )
        # If the match already played
        if new_tuple in tournament_match:
            print("Cette paire '{}' a déja jouer".format(new_tuple))
            j += 1
            continue
        else:
            tournament_match.append(new_tuple)
            tournament_match.append(new_tuple_reverse)
            match_list_tuple.append(match_tuple)

        generated_match.append(new_tuple)
        # Delete the players to be sure to not create another match with them
        del new_ranking[j]
        del new_ranking[0]
        j = 1

    return generated_match


def tournament_round(
    tournament, player_list, match_list, tournament_match, match_list_tuple
):
    """Define tournament round"""
    if len(tournament.tour_list) == 0:
        round_number = 1
        round_name = "Round {}".format(round_number)

        first_match(player_list, match_list, tournament_match, match_list_tuple)
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
        tournament.tour_list.append(tour)

        show_players_status(player_list)
        sleep(2)

        print("Classement:")
        player_ranking(player_list)
        sleep(1)
        match_list.clear()
        match_list_tuple.clear()

    elif len(tournament.tour_list) > 0:
        round_number = len(tournament.tour_list) + 1
        round_name = "Round {}".format(round_number)

        match_set(player_list, match_list, tournament_match, match_list_tuple)
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
        tournament.tour_list.append(tour)
        show_players_status(player_list)
        sleep(2)

        print("Classement:")
        player_ranking(player_list)
        sleep(1)
        match_list.clear()
        match_list_tuple.clear()
