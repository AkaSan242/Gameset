# Gameset
Gameset is an application to... set a game (for real no joke). let me explain before you leave please !!!
With Gameset you can create players and make a tournament with them for anygame.

you can save/load the players and the tournaments everytime you run the application and the most of the most..
Gameset is an off_line application so even if you don't have internet or a good coonexion it doesn't matter it works
interesting no ?

(yes i know is not but act like it is ok ? thank you next)

## INSTALLATION
To use this wonderful appliaction (yes wonderful) please:

 -Clone the url of the repository
 
 -Run `git clone url_of_repository`
 
 -Create a virtual environment by run `python -m venv env`
 
 -Activate your environment by run `source env/bin/activate`
 
 -Run `pip install -r requirements.txt`
 
 -Start enjoy Gameset by run `python gameset.py`
  
 you can create your self flake8 report directory if you want just run`flake8 --format=html --htmldir=flake-report` 
 
 
 
## HOW TO USE

i said "for anygame" but in this case the script of Gameset is make for a chess game (why not?)
let me tell you what's happening when you run the application
first of all you got the 'Main Menu':
                                    
                                    -1.Add a player
                                    -2.Player list
                                    -3.Start a new tournament
                                    -4.Tournament list
                                    -5.Leave (yes i know you want to but please stay)
                                    
#### 1.Add a Player
-Choose the number of players you want to add

-Add the player, a player is define like that:
                
                                    -1.Name
                                    -2.Last name
                                    -3.Birth date
                                    -4.Gender
                                    -5.Rank
                                    -6.Score(deafult=0) 
                                    the score change only during a tournament so you don't have to define him
                                    
 -When you finish to create a player he/she will automaticaly be save on database and guess what ? 
 
 you don't have to create her the application will do it for you yeah !! don't thank me.
 
 -Now everytime you run the applcation your players will be available.
 
 #### 2.Player list
 -Print the list of players (obviously what else ?)
 
 -Choose if you want the list by:
    
                                  -Name
                                  or
                                  -Rank
                                  
 #### 3.Start a new tournament
 -Two options:
              
              -Start a new tournament
              -Continue a tournament
 
 When you start a Tournament you have two things to do:
 
              -Choose the players of the Tournament(default=8) in the player list
              -Define the info of the tournament (Name, Place, choose the time control)
              the datetime will be define automaticaly
              
 after that the tournament start.
 
 The tournament:
    
 A tournament has 8 players and 4 rounds by default you can change that in the script 'tournament.py'.
 for the first round only the match/fight or whatever you call it between two players is define like this:
   
    -Player 1 vs 5
    -Player 2 vs 6
    -Player 3 vs 7
    -Player 4 vs 8
    
  And the next rounds like that:
    
    -Player 1 vs 2
    -Player 3 vs 4
    -Player 5 vs 6
    -Player 7 vs 8
    
   there is an algorithm make to be sure than two players have a match only once so if player 1 and 2 already have a match on a previous round the algorithm change the oppeners until he find a match never happen.
   
 By the end of each round you have to add point for each player and the application will ranking the players by score.
 After that you will have two questions:
 
    -Continue ? 1.yes/2.no ?
    -Change the general ranking of a player ? 1.yes/2.no ?
    
 General ranking ? what are you talking about ? ok let me teach you young jedi. you have a list of player in the application ok? you choose player on this list for your tournament ok ? when you create a player you have to give him a rank right ?(are you still there ? lol) ok then the rank of a player in the application and the ranking during a tournament are not the same ranking (you got it !) so the question is for change the ranking of a player in general not in the current tournament.
 understood ? cool now next.
 
 If you choose yes at the continue question of course the tournament will goes on but if you choose no the tournament will be save on the database (players, round, score, etc) so you can finish it whenever you want when you run the application another time.
 
 by the end of the tournament you can wright your remarks about it and it will be save too on database so you have a record of all tournament played in the application.
 
#### 4.List of tournaments
the list of all tournaments played

You choose a tournament and you can check:

    -list of players(by name and rank)
    -list of rounds(match list, datetime of beginning and ending)
    -list of matchs(all matchs of the tournament)  
    
#### 5.Leave
NOT YET !!

 
 ## CONTRIBUTIONS
 ME MYSELF AND I
 and my mentor (just a little^^ but i'm still thankful)
