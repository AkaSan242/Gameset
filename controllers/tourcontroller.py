"""Base tour controller"""

from operator import attrgetter
from views.tourview import *


def first_match(player_list, match_list, tournament_match, match_list_tuple):
    """define the matchs of the first round only:
    -Player 1 vs 5
    -Player 2 VS 6
    -Player 3 VS 7
    -Player 4 VS 8"""

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


def tournament_match_set(player_list, match_list, tournament_match, match_list_tuple):
    """Same as first round but for all round of a Tournament:
    -Player 1 vs 2
    -Player 3 vs 4
    -Player 5 vs 6
    -Player 7 vs 8"""

    new_ranking = sorted(player_list, key=attrgetter("rank"))

    # Fisrt macth
    match_one = ([new_ranking[0]], [new_ranking[1]])
    match_one_reverse = ([new_ranking[1]], [new_ranking[0]])
    match_one_tuple = (
        [new_ranking[0], new_ranking[0].score],
        [new_ranking[1], new_ranking[1].score],
    )

    # Second match
    match_two = ([new_ranking[2]], [new_ranking[3]])
    match_two_reverse = ([new_ranking[3]], [new_ranking[2]])
    match_two_tuple = (
        [new_ranking[2], new_ranking[2].score],
        [new_ranking[3], new_ranking[3].score],
    )

    # Third match
    match_three = ([new_ranking[4]], [new_ranking[5]])
    match_three_reverse = ([new_ranking[5]], [new_ranking[4]])
    match_three_tuple = (
        [new_ranking[4], new_ranking[4].score],
        [new_ranking[5], new_ranking[5].score],
    )

    # Fourth match
    match_four = ([new_ranking[6]], [new_ranking[7]])
    match_four_reverse = ([new_ranking[7]], [new_ranking[6]])
    match_four_tuple = (
        [new_ranking[6], new_ranking[6].score],
        [new_ranking[7], new_ranking[7].score],
    )

    match_list.append(match_one)
    match_list.append(match_two)
    match_list.append(match_three)
    match_list.append(match_four)

    # Check if a match was already played
    if match_one in tournament_match:
        print("Cette paire '{}' a déja jouer".format(match_one))
        print("On refait le tirage")
        check_match(player_list, match_list, tournament_match, match_list_tuple)

    elif match_two in tournament_match:
        print("Cette paire '{}' a déja jouer".format(match_two))
        print("On refait le tirage")
        check_match(player_list, match_list, tournament_match, match_list_tuple)

    elif match_three in tournament_match:
        print("Cette paire '{}' a déja jouer".format(match_three))
        print("On refait le tirage")
        check_match(player_list, match_list, tournament_match, match_list_tuple)

    elif match_four in tournament_match:
        print("Cette paire '{}' a déja jouer".format(match_four))
        print("On refait le tirage")
        check_match(player_list, match_list, tournament_match, match_list_tuple)

    else:
        tournament_match.append(match_one)
        tournament_match.append(match_one_reverse)

        tournament_match.append(match_two)
        tournament_match.append(match_two_reverse)

        tournament_match.append(match_three)
        tournament_match.append(match_three_reverse)

        tournament_match.append(match_four)
        tournament_match.append(match_four_reverse)

        match_list_tuple.append(match_one_tuple)
        match_list_tuple.append(match_two_tuple)
        match_list_tuple.append(match_three_tuple)
        match_list_tuple.append(match_four_tuple)


def tournament_rematch(player_list, match_list, tournament_match, match_list_tuple):
    """Redefine all match for a round:
    -Player 1 vs 3
    -Player 2 vs 4
    -Player 5 vs 7
    -Player 6 vs 8"""

    match_list.clear()

    new_ranking = sorted(player_list, key=attrgetter("rank"))

    # Fisrt macth
    match_one = ([new_ranking[0]], [new_ranking[2]])
    match_one_reverse = ([new_ranking[2]], [new_ranking[0]])
    match_one_tuple = (
        [new_ranking[0], new_ranking[0].score],
        [new_ranking[2], new_ranking[2].score],
    )

    # Second match
    match_two = ([new_ranking[1]], [new_ranking[3]])
    match_two_reverse = ([new_ranking[3]], [new_ranking[1]])
    match_two_tuple = (
        [new_ranking[1], new_ranking[1].score],
        [new_ranking[3], new_ranking[3].score],
    )

    # Third match
    match_three = ([new_ranking[4]], [new_ranking[6]])
    match_three_reverse = ([new_ranking[6]], [new_ranking[4]])
    match_three_tuple = (
        [new_ranking[4], new_ranking[4].score],
        [new_ranking[6], new_ranking[6].score],
    )

    # Fourth match
    match_four = ([new_ranking[5]], [new_ranking[7]])
    match_four_reverse = ([new_ranking[7]], [new_ranking[5]])
    match_four_tuple = (
        [new_ranking[5], new_ranking[5].score],
        [new_ranking[7], new_ranking[7].score],
    )

    match_list.append(match_one)
    match_list.append(match_two)
    match_list.append(match_three)
    match_list.append(match_four)

    # Check if a match was already played
    if match_one in tournament_match:
        print("Cette paire '{}' a déja jouer".format(match_one))
        print("On refait le tirage")
        match_list.clear()
        recheck_match_again(player_list, match_list, tournament_match, match_list_tuple)

    elif match_two in tournament_match:
        print("Cette paire '{}' a déja jouer".format(match_two))
        print("On refait le tirage")
        match_list.clear()
        recheck_match_again(player_list, match_list, tournament_match, match_list_tuple)

    elif match_three in tournament_match:
        print("Cette paire '{}' a déja jouer".format(match_three))
        print("On refait le tirage")
        match_list.clear()
        recheck_match_again(player_list, match_list, tournament_match, match_list_tuple)

    elif match_four in tournament_match:
        print("Cette paire '{}' a déja jouer".format(match_four))
        print("On refait le tirage")
        match_list.clear()
        recheck_match_again(player_list, match_list, tournament_match, match_list_tuple)

    else:
        tournament_match.append(match_one)
        tournament_match.append(match_one_reverse)

        tournament_match.append(match_two)
        tournament_match.append(match_two_reverse)

        tournament_match.append(match_three)
        tournament_match.append(match_three_reverse)

        tournament_match.append(match_four)
        tournament_match.append(match_four_reverse)

        match_list_tuple.append(match_one_tuple)
        match_list_tuple.append(match_two_tuple)
        match_list_tuple.append(match_three_tuple)
        match_list_tuple.append(match_four_tuple)


def tournament_rematch_more(
    player_list, match_list, tournament_match, match_list_tuple
):
    """Redefine all match for a round:
    -Player 1 vs 4
    -Player 2 vs 5
    -Player 3 vs 6
    -Player 7 vs 8"""

    match_list.clear()

    new_ranking = sorted(player_list, key=attrgetter("rank"))

    # Fisrt macth
    match_one = ([new_ranking[0]], [new_ranking[3]])
    match_one_reverse = ([new_ranking[3]], [new_ranking[0]])
    match_one_tuple = (
        [new_ranking[0], new_ranking[0].score],
        [new_ranking[3], new_ranking[3].score],
    )

    # Second match
    match_two = ([new_ranking[1]], [new_ranking[4]])
    match_two_reverse = ([new_ranking[4]], [new_ranking[1]])
    match_two_tuple = (
        [new_ranking[1], new_ranking[1].score],
        [new_ranking[4], new_ranking[4].score],
    )

    # Third match
    match_three = ([new_ranking[2]], [new_ranking[5]])
    match_three_reverse = ([new_ranking[5]], [new_ranking[2]])
    match_three_tuple = (
        [new_ranking[2], new_ranking[2].score],
        [new_ranking[5], new_ranking[5].score],
    )

    # Fourth match
    match_four = ([new_ranking[6]], [new_ranking[7]])
    match_four_reverse = ([new_ranking[7]], [new_ranking[6]])
    match_four_tuple = (
        [new_ranking[6], new_ranking[6].score],
        [new_ranking[7], new_ranking[7].score],
    )

    match_list.append(match_one)
    match_list.append(match_two)
    match_list.append(match_three)
    match_list.append(match_four)

    # Check if a match was already played
    if match_one in tournament_match:
        print("Cette paire '{}' a déja jouer".format(match_one))
        print("On refait le tirage")
        match_list.clear()
        recheck_match_more(player_list, match_list, tournament_match, match_list_tuple)

    elif match_two in tournament_match:
        print("Cette paire '{}' a déja jouer".format(match_two))
        print("On refait le tirage")
        match_list.clear()
        recheck_match_more(player_list, match_list, tournament_match, match_list_tuple)

    elif match_three in tournament_match:
        print("Cette paire '{}' a déja jouer".format(match_three))
        print("On refait le tirage")
        match_list.clear()
        recheck_match_more(player_list, match_list, tournament_match, match_list_tuple)

    elif match_four in tournament_match:
        print("Cette paire '{}' a déja jouer".format(match_four))
        print("On refait le tirage")
        match_list.clear()
        recheck_match_more(player_list, match_list, tournament_match, match_list_tuple)

    else:
        tournament_match.append(match_one)
        tournament_match.append(match_one_reverse)

        tournament_match.append(match_two)
        tournament_match.append(match_two_reverse)

        tournament_match.append(match_three)
        tournament_match.append(match_three_reverse)

        tournament_match.append(match_four)
        tournament_match.append(match_four_reverse)

        match_list_tuple.append(match_one_tuple)
        match_list_tuple.append(match_two_tuple)
        match_list_tuple.append(match_three_tuple)
        match_list_tuple.append(match_four_tuple)


def tournament_rematch_more_one(
    player_list, match_list, tournament_match, match_list_tuple
):
    """Redefine all match for a round:
    -Player 1 vs 8
    -Player 2 vs 7
    -Player 3 vs 6
    -Player 4 vs 5"""

    match_list.clear()

    new_ranking = sorted(player_list, key=attrgetter("rank"))

    # Fisrt macth
    match_one = ([new_ranking[0]], [new_ranking[7]])
    match_one_reverse = ([new_ranking[7]], [new_ranking[0]])
    match_one_tuple = (
        [new_ranking[0], new_ranking[0].score],
        [new_ranking[7], new_ranking[7].score],
    )

    # Second match
    match_two = ([new_ranking[1]], [new_ranking[6]])
    match_two_reverse = ([new_ranking[6]], [new_ranking[1]])
    match_two_tuple = (
        [new_ranking[1], new_ranking[1].score],
        [new_ranking[6], new_ranking[6].score],
    )

    # Third match
    match_three = ([new_ranking[2]], [new_ranking[5]])
    match_three_reverse = ([new_ranking[5]], [new_ranking[2]])
    match_three_tuple = (
        [new_ranking[2], new_ranking[2].score],
        [new_ranking[5], new_ranking[5].score],
    )

    # Fourth match
    match_four = ([new_ranking[3]], [new_ranking[4]])
    match_four_reverse = ([new_ranking[4]], [new_ranking[3]])
    match_four_tuple = (
        [new_ranking[3], new_ranking[3].score],
        [new_ranking[4], new_ranking[4].score],
    )

    match_list.append(match_one)
    match_list.append(match_two)
    match_list.append(match_three)
    match_list.append(match_four)

    # Check if a match was already played
    if match_one in tournament_match:
        print("Cette paire '{}' a déja jouer".format(match_one))
        print("On refait le tirage")
        match_list.clear()
        recheck_match(player_list, match_list, tournament_match, match_list_tuple)

    elif match_two in tournament_match:
        print("Cette paire '{}' a déja jouer".format(match_two))
        print("On refait le tirage")
        match_list.clear()
        recheck_match(player_list, match_list, tournament_match, match_list_tuple)

    elif match_three in tournament_match:
        print("Cette paire '{}' a déja jouer".format(match_three))
        print("On refait le tirage")
        match_list.clear()
        recheck_match(player_list, match_list, tournament_match, match_list_tuple)

    elif match_four in tournament_match:
        print("Cette paire '{}' a déja jouer".format(match_four))
        print("On refait le tirage")
        match_list.clear()
        recheck_match(player_list, match_list, tournament_match, match_list_tuple)

    else:
        tournament_match.append(match_one)
        tournament_match.append(match_one_reverse)

        tournament_match.append(match_two)
        tournament_match.append(match_two_reverse)

        tournament_match.append(match_three)
        tournament_match.append(match_three_reverse)

        tournament_match.append(match_four)
        tournament_match.append(match_four_reverse)

        match_list_tuple.append(match_one_tuple)
        match_list_tuple.append(match_two_tuple)
        match_list_tuple.append(match_three_tuple)
        match_list_tuple.append(match_four_tuple)


def check_match(player_list, match_list, tournament_match, match_list_tuple):
    """check if a match alreday made"""
    print("Contrôle des matchs...")
    tournament_rematch(player_list, match_list, tournament_match, match_list_tuple)


def recheck_match(player_list, match_list, tournament_match, match_list_tuple):
    """check if a match alreday made"""
    print("Contrôle des matchs...")
    first_match(player_list, match_list, tournament_match, match_list_tuple)


def recheck_match_again(player_list, match_list, tournament_match, match_list_tuple):
    """check if a match alreday made"""
    print("Contrôle des matchs...")
    tournament_rematch_more(player_list, match_list, tournament_match, match_list_tuple)


def recheck_match_more(player_list, match_list, tournament_match, match_list_tuple):
    """check if a match alreday made"""
    print("Contrôle des matchs...")
    tournament_rematch_more_one(
        player_list, match_list, tournament_match, match_list_tuple
    )
