"""Main script of gameset test"""

from controllers.controller import Controller
from views.tournamentview import tournament_main_page

game = Controller()

print("BIENVENUE DANS GAMESET !")
tournament_main_page()
game.choose()
