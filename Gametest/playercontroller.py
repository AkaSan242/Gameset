"""Base Player controller"""

from time import sleep
from player import Player
from playerview import PlayerView
from operator import attrgetter


class PlayerController(PlayerView):
    """Gameset Player Controller"""

    def add_a_new_player(self, player_list):
        """Add a new player in the game"""
        player_name = input("Quel est le prénom du joueur:")
        player_last_name = input("Quel est le nom du Joueur:")
        player_birth_date = input("Date de Naissance:")
        player_gender = input("Sexe (Homme, Femme, Personnel):")
        player_rank = input("Classement:")

        player_list.append(Player(player_name,
                                  player_last_name,
                                  player_birth_date,
                                  player_gender,
                                  player_rank))

        print("Ajout du nouveau joueur '{}' terminé".format(player_name))
        sleep(2)
        self.show_player(player_name, player_last_name, player_birth_date,
                         player_gender, player_rank)

    def update_player_rank(self, player_list):
        """Update player rank"""
        print("Mise à jour du classement:")
        for i in range(len(player_list)):
            print("{}.{}".format(i, player_list[i]))

        choose_player = input("Choisissez un joueur (entrez son numéro):")
        player = player_list[int(choose_player)]
        new_rank = input("Quel est le nouveau classement de {}:".format(player))
        player.rank = new_rank
        print("Nouveau classement de {} confirmé".format(player))

    def update_player_score(self, player_list):
        """Add score for player after round"""
        print("C'est l'heure d'ajouter les résultats:")
        for i in range(len(player_list)):
            player = player_list[i]
            add_score = input("Quel est le score de {}:".format(player))
            score = add_score
            player.score += int(score)


    def search_player_by_name(self, player_list):
        """Print Player_list by Name"""
        new_ranking = sorted(player_list, key=attrgetter('name'))
        i = 1
        for elt in new_ranking:
            print("{}.{}".format(i, elt))
            i += 1

    def search_player_by_rank(self, player_list):
        """Print Player_list by Rank"""
        new_ranking = sorted(player_list, key=attrgetter('rank'))
        i = 1
        for elt in new_ranking:
            print("{}.{}".format(i, elt))
            i += 1