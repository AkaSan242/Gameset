"""Base Tournament view"""

from tournament import Tournament
from time import  sleep

class TournamentView:
    """Gameset Tournament view"""

    def new_tournament(self, tournament_dic):
        """Start a new tournament"""
        name = input("Quel est le nom du Tournoi:")
        place = input("lieu du Tournoi:")
        time_control = input("Controle du temps (Bullet, Blitz ou coup rapide):")

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

    def choose_a_player(self, player_list, players):
        """Select a player for the tournament"""
        i = 0
        for elt in player_list:
            print("{}.{}".format(i, elt))
            i += 1

        choose_player = input("Choisissez un joueur(entrez son numéro):")
        player = player_list[int(choose_player)]
        print("Vous avez choisi:{}".format(player))
        sleep(2)
        players.append(player)

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
        """Choose 2 player for a match"""
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
        """define tournament match for a round"""
        match_one = "{} vs {}".format(rank_sup["1"], rank_sup["2"])
        match_two = "{} vs {}".format(rank_sup["3"], rank_sup["4"])
        match_three = "{} vs {}".format(rank_inf["5"], rank_inf["6"])
        match_four = "{} vs {}".format(rank_inf["7"], rank_inf["8"])

        match_list.append(match_one)
        match_list.append(match_two)
        match_list.append(match_three)
        match_list.append(match_four)

    def show_tournament_match(self, match_list):
        """Show all the match of the round"""
        print("Voici tout les matchs du prochain round:")
        for elt in match_list:
            print(elt)

    def update_player_score(self, player_list, score_list):
        """Add score for player after match"""
        print("C'est l'heure d'ajouter les résultats:")
        for i in range(len(player_list)):
            player = player_list[i]
            add_score = input("Quel est le score de {}:".format(player))
            score = add_score
            player.score += int(score)
            player_score = "{}:{} points".format(player, player.score)
            score_list.append(player_score)

    def update_player_rank(self, players, rank_sup, rank_inf):
        """Update player rank after match"""
        print("Mise à jour du classement:")
        for i in range(len(players)):
            player = players[i]
            new_rank = input("Quel est le nouveau classement de {}:".format(player))
            player.rank = new_rank

            if player.rank == "1":
                rank_sup["1"] = player
            elif player.rank == "2":
                rank_sup["2"] = player
            elif player.rank == "3":
                rank_sup["3"] = player
            elif player.rank == "4":
                rank_sup["4"] = player
            elif player.rank == "5":
                rank_inf["5"] = player
            elif player.rank == "6":
                rank_inf["6"] = player
            elif player.rank == "7":
                rank_inf["7"] = player
            elif player.rank == "8":
                rank_inf["8"] = player

    def show_players_status(self, players):
        """Show all Players status after round"""
        print("Voici le nouveau classement et résultats des joueurs après ce round:")
        for player in players:
            print("Joueur:'{}' Classement:'{}' Score:'{}'".format(player, player.rank, player.score))

    def tournament_main_page(self):
        """Print Main menu"""
        print("Menu Principal")
        print("1.Ajouter un Joueur")
        print("2.Liste des joueurs")
        print("3.Nouveau Tournoi")
        print("4.Description")
        print("5.Quitter")
