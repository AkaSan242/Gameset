"""Base Player view."""


from models.tournament import Tournament


def show_players(player_list):
    """Present all players of tournament"""
    print("Voici les {} participants du Tournoi:".format(Tournament.NUMBER_OF_PLAYERS))
    for players in player_list:
        print(
            "{} Classement:'{}' Score:'{}'".format(players, players.rank, players.score)
        )


def show_list_players(player_list):
    """Present all players of the list"""
    print("Voici les {} Joueurs disponible:".format(len(player_list)))
    for players in player_list:
        print(
            "Prénom: {} Nom: {} Classement: {}".format(
                players.name, players.last_name, players.rank
            )
        )
    if len(player_list) == 0:
        print("Il n'y a aucun joueurs disponible")


def show_player(name, last_name, birth_date, gender, rank):
    """Show player informations"""
    print(
        "Prénom:'{}' Nom:'{}' Date de naissance:'{}' Genre:'{}' Classement: '{}'".format(
            name, last_name, birth_date, gender, rank
        )
    )


def show_players_status(player_list):
    """Show all Players status after round"""
    print("Voici le nouveau classement et score des joueurs après ce round:")
    for player in player_list:
        print("Joueur: {} Score: {} Points".format(player, player.score))


def update_delete_player_main_page():
    """Main menu of update/delete player"""
    print("Voulez-vous:")
    print("1.Modifier un joueur")
    print("2.Supprimer un joueur")


def update_player_page():
    """Main page of choice update player"""
    print("Que voulez-vous modifier")
    print("1.Nom")
    print("2.Prénom")
    print("3.Date de Naissance")
    print("4.Genre")
    print("5.Classement")
