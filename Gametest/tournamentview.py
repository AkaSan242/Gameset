"""Base Tournament view"""

from tournament import Tournament


class TournamentView:
    """Gameset Tournament view"""

    def new_tournament(self, tournament_list):
        """Start a new tournament"""
        name = input("Quel est le nom du Tournoi:")
        place = input("Où aura lieu le Tournoi:")
        time_control = input("Controle du temps (Bullet, Blitz ou coup rapide):")

        new_tournament = Tournament(name, place, time_control)
        tournament_list.append(new_tournament)

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

        choose_player = input("Séléctionner un joueur (entrez son numéro):")
        player = player_list[int(choose_player)]
        print("Vous avez choisi:'{}'".format(player))

        players.append(player)

    def show_tournament_informations(self, name, place, time_control, date, player_numbers, number_of_rounds):
        """Show tournament information"""
        print("Tournoi:'{}' Lieu:'{}' Date:'{}' Participants:'{}' Rounds:'{}' Contrôle du temps:'{}' ".format(name,
                                                                                                              place,
                                                                                                              date,
                                                                                                    player_numbers,
                                                                                                  number_of_rounds,
                                                                                                    time_control))

    def match(self, players, match_list):
        """Choose 2 player for a match"""
        print("C'est l'heure de définir les prochains matchs")
        print("Voici les joueurs disponibles:")
        i = 0
        for elt in players:
            print("{}.{}".format(i, elt))
            i += 1

        choose_player_one = input("Séléctionner un joueur (entrez son numéro):")
        player_one = players[int(choose_player_one)]
        print("Vous avez choisi: '{}'".format(player_one))

        choose_player_two = input("Séléctionner un jouuer (entrez son numéro):")
        player_two = players[int(choose_player_two)]
        print("Vous avez choisi: '{}'".format(player_two))

        match = "Match: {} vs {}".format(player_one, player_two)
        match_list.append(match)

    def show_tournament_match(self, match_list):
        """Show all the match of the round"""
        print("Voici tout les matchs du prochain round:")
        for elt in match_list:
            print(elt)

    def update_player_score(self, player_list, score_list):
        """Add score for player after match"""
        print("C'est l'heure d'ajouter les résultats:")
        i = 0
        for elt in player_list:
            print("{}.{}".format(i, elt))
            i += 1
        for i in range(len(player_list)):
            choose_player = input("Choisissez un joueur pour ajouter son score (Tapez son numéro): ")
            player = player_list[int(choose_player)]
            add_score = input("Quel est le score de {}:".format(player))
            score = add_score
            player.score += int(score)
            player_score = "{}:{} points".format(player, player.score)
            score_list.append(player_score)

    def update_player_rank(self, players):
        """Update player rank after match"""
        print("Mise à jour du classement:")
        i = 0
        for elt in players:
            print("{}.{}".format(i, elt))
            i += 1
        for i in range(len(players)):
            choose_player = input("Choisissez un joueur pour mettre son classement à jour (Tapez son numéro): ")
            player = players[int(choose_player)]
            new_rank = input("Quel est le nouveau classement de {}:".format(player))
            player.rank = new_rank

    def show_players_status(self, players):
        """Show all Players status after round"""
        print("Voici le nouveau classement et résultats des joueurs après ce round:")
        for elt in players:
            print("Joueur:'{}' Classement:'{}' Score:'{}'".format(elt, elt.rank, elt.score))

    def tournament_main_page(self):
        """Print Main menu"""
        print("Menu Principal")
        print("1.Ajouter un Joueur")
        print("2.Liste des joueurs")
        print("3.Nouveau Tournoi")
        print("4.Description")
        print("5.Quitter")
