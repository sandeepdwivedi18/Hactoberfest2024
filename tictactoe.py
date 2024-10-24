print (" tic tac toe Python program");

 
def tictactoe_grid(value):  
    print("\n")  
    print("\t      |      |")  
    print("\t    {} |  {}   |  {}".format(value[0], value[1], value[2]))  
    print('\t______|______|______')  
# printing the first three boxes of the 3X3 game board   
    print("\t      |      |") 
    print("\t   {}  |  {}   |  {}".format(value[3], value[4], value[5]))  
    print('\t______|______|______')  
    print("\t      |      |")  
# printing the second three boxes of the 3X3 game board   
    print("\t  {}   |  {}   |  {}".format(value[6], value[7], value[8]))  
    print("\t      |      |")  
    print("\n") 
# printing the last three boxes of the 3X3 game board   
 
####To Design the Scoreboard
# Use the user-defined function Python to create a scoreboard to capture the scores made during the game and display this when the game ends.
def my_scoreboard(score_board):  
    print("\t--------------------------------")  
    print("\t         The SCOREBOARD for TIC TAC TOE PYTHON GAME       ")  
    print("\t--------------------------------")  
   
    list_of_the_two_players = list(score_board.keys())  
    print("\t   ", list_of_the_two_players[0], "\t    ", score_board[list_of_the_two_players[0]])  
    print("\t   ", list_of_the_two_players[1], "\t    ", score_board[list_of_the_two_players[1]])  
   
    print("\t--------------------------------\n")
 
###To validate the Win or Tie situation of tic tac toe Python
# User-defined function Python for validating the win combinations in the entire tic tac toe Python game  
def win_validate(position_player, player_current):  
   
 # Below are all the possible winning combinations that were analyzed to win the tic tac toe Python game  
    win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]  
   
# using the for loop in Python to validate if any winning combination is getting validated as TRUE or not  
    for i in win_combinations:  
        if all(j in position_player[player_current] for j in i):  
   
# If any winning combination is getting validated as TRUE then the function shall return TRUE  
            return True  
# If any winning combination is not getting validated as TRUE then the function shall return FALSE   
    return False         
   
# User-defined function Python for validating is the tic ta toe Python game is a tie   
def tie_validate(position_player):  
    if len(position_player['X']) + len(position_player['O']) == 9:  
        return True  
    return False     
        

###Using the Data Structure to Store Data for a single game of tic tac toe Python

def game_single(player_current):  
# function to highlight the tic tac toe Python game  
    value = [' ' for i in range(9)]  
       
    print("using the data structure to store the filled positions denoted by X and O ")
    position_player = {'X' : [], 'O' : []} 

###To Understand the design of Game-Loop of tic tac toe Python
    while True:  
        tictactoe_grid(value)
#using the while loop to call the  tictactoe_grid function whenever it remains TRUE.
        print(" To handle the input from the player using the Try-Exception block for 'CHANCE' input ")

        try:  
            print("The player ", player_current, " turn. Now you need to choose your block : ", end="")  
            chance = int(input())  
        except ValueError:  
            print("This is an Invalid Input!!! Please try again!")  
            continue
  
        print("Below is the sanity check for 'CHANCE' input")  
        if chance < 1 or chance > 9:  
            print("This is an Invalid Input!!! Please try again!")  
            continue  
   
        print(" To check if the block in the grid is not filled up already ") 
        if value[chance - 1] != ' ':  
            print("Oops! The position is already filled. Please try again!")  
            continue  


###To update the inputs from a player into the game information of tic tac toe Python

        value[chance - 1] = player_current  
# By adding the above code, we update the status of the gameboard  
 
        position_player[player_current].append(chance)  
# By adding the above code, we update the player's position on the grid.
 
# calling the UDF to check for Win  
        if win_validate(position_player, player_current):  
            tictactoe_grid(value)  
            print("Hurray! You nailed it! ", player_current, " has won the tic tac toe Python game!")       
            print("\n")  
            return player_current  
      
# calling the UDF to check for Tie  
        if tie_validate(position_player):  
            tictactoe_grid(value)  
            print("It was close! Game is Tied")  
            print("\n")  
            return 'D'  
 
###To validate switching between the player once the chance of one player is executed
# using the if-else loop in Python to make the switch between the player  
        if player_current == 'X':  
            player_current = 'O'  
        else:  
            player_current = 'X'
    
    
###To Record the Player's names to observe on the scoreboard

if __name__ == "__main__":  
   
    print("The First Player's name")  
    player_first = input("Please mention your name: ")  
    print("\n")  
# implmenting the input function in Python to allow the user of the game to input its name.

    print("The Second Player's name")  
    player_second = input("Please mention your name:  ")  
    print("\n")
     
###To capture the game information
# Capturing the player who chooses the  X and O  
    player_current = player_first  
   
# Capturing the players' choice  
    player_choice = {'X' : "", 'O' : ""}  
   
# Storing the two possible options available for the tic tac toe Python game 
    option = ['X', 'O']  
   
# Storing the information that needs to be captured in the scoreboard  
    score_board = {player_first: 0, player_second: 0}  
    my_scoreboard(score_board)  
 
###For creating an Outer loop to make our game flexible and allow multiple games of tic tac toe Python to be played

# Using the while function in Python for adding multiple series of games until the players call it an exit.
    while True:  
# Menu displayed to the players
        print(player_current, ", you get the chance to make the choice for the series of the Tic tac toe Python game:")  
        print("Please press 1 for X")  
        print("Please press 2 for O")  
        print("Please press 3 for Exit") 
 
###To Handle Exception and Allot the selection of the symbol for the current player for each iteration of the game

# The try-except block for the_choice input from the player  
        try:  
            the_choice = int(input())     
        except ValueError:  
            print("This input is Invalid!!! Please Try Again\n")  
            continue  
   
# if Elif else loop in Python to define the condition for the selection made.   
        if the_choice == 1:  
            player_choice['X'] = player_current  
            if player_current == player_first:  
                player_choice['O'] = player_second  
            else:  
                player_choice['O'] = player_first  
   
        elif the_choice == 2:  
            player_choice['O'] = player_current  
            if player_current == player_first:  
                player_choice['X'] = player_second  
            else:  
                player_choice['X'] = player_first  
           
        elif the_choice == 3:
            print("Thanks for playing the game!!!")
            print("The final scores are")  
            my_scoreboard(score_board)  
            break    
   
        else:  
            print("This is an Invalid choice!! Please try again\n") 
 
###Execution of the tic tac toe Python game and updating the scoreboard simultaneously
# Capturing the winner of the single game of Tic-Tac-Toe Python
        winner = game_single(option[the_choice - 1]) 

# As per the scores obtained the winner is getting updated on the scoreboard  
        if winner != 'D' :  
            player_won = player_choice[winner]  
            score_board[player_won] = score_board[player_won] + 1 
 
            my_scoreboard(score_board)

###Swapping the chance given to choose the symbol between the selecting player
# Swapping between the players after each game for who will choose X or O  
        if player_current == player_first:  
            player_current = player_second  
        else:  
            player_current = player_first 
