"""Main script of gameset test"""

from controllers.controller import Controller

gameset_players = []
gameset_tournament = []
tournament_players = []
match_list = []

tournament_dic = {}
round_dic = {}
ranks_dic = {}

game = Controller(gameset_players, gameset_tournament,
                  tournament_players, tournament_dic,
                  match_list, round_dic, ranks_dic)

print("BIENVENUE DANS GAMESET !")
game.tournament_main_page()
game.choose()