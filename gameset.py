"""Main script of gameset test"""

from controllers.controller import Controller

gameset_players = []
gameset_tournament = []
gameset_match_list = []
tournament_players = []
match_list = []
tour_list = []
tournament_match = [] 


game = Controller(gameset_players, gameset_tournament,
                  tournament_players, match_list,
                  tour_list, tournament_match_list=tournament_match, gameset_match_list=gameset_match_list)

print("BIENVENUE DANS GAMESET !")
game.tournament_main_page()
game.choose()