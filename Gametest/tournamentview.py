"""Base Tournament view"""

from tournament import Tournament


class TournamentView:
    """Gameset Tournament view"""

    def create_new_tournament(self, list):
        """Start a new tournament"""
        tournament_name = input("Quel est le nom du Tournoi:")
        tournament_place = input("Où aura lieu le Tournoi:")
        tournament_time_control = input("Controle du temps (Bullet, Blitz ou coup rapide):")

        new_tournament = Tournament(tournament_name, tournament_place, tournament_time_control)
        list.append(new_tournament)

        print("Création du nouveau Tournoi '{}'".format(tournament_name))
        return new_tournament.show_tournament_informations()

    def tournament_match(self, player_list, match_list):
        """Choose 2 player for a match"""
        print("C'est l'heure de définir les prochains matchs")
        print("Voici les joueurs disponibles:")
        i = 0
        for elt in player_list:
            print("{}.{}".format(i, elt))
            i += 1

        choose_player_one = input("Séléctionner un joueur (entrez son numéro):")
        player_one = player_list[int(choose_player_one)]
        print("Vous avez choisi: '{}'".format(player_one))

        choose_player_two = input("Séléctionner un jouuer (entrez son numéro):")
        player_two = player_list[int(choose_player_two)]
        print("Vous avez choisi: '{}'".format(player_two))

        match = "Match: {} vs {}".format(player_one, player_two)
        match_list.append(match)

    def show_tournament_match(self, match_list):
        """Show all the match of the round"""
        print("Voici tout les matchs du prochain round:")
        for elt in match_list:
            print(elt)

    def tournament_player_score(self, player_list, score_list):
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
            player_score = "{}:{} points".format(player, score)
            score_list.append(player_score)

    def tournament_show_player_score(self, score_list):
        """Show all Players score after round"""
        print("voici les points des participants:")
        for elt in score_list:
            print(elt)

    def tournament_main_page(self):
        """Print Main menu"""
        print("Menu Principal")
        print("1.Ajouter un Joueur")
        print("2.Liste des joueurs")
        print("3.Nouveau Tournoi")
        print("4.Faire un Match")
        print("5.Description")
        print("6.Quitter")
