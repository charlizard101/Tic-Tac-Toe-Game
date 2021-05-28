
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

board2 = ["1","2","3",
         "4","5","6",
         "7","8","9"]

game_running = True

winner = None
player="X"
def display_board():

    print(board[0] + "|" + board[1] + "|" + board[2]+"         "+ board2[0] + "|" + board2[1] + "|" + board2[2])
    print(board[3] + "|" + board[4] + "|" + board[5]+"         "+ board2[3] + "|" + board2[4] + "|" + board2[5])
    print(board[6] + "|" + board[7] + "|" + board[8]+"         "+ board2[6] + "|" + board2[7] + "|" + board2[8])

def run_game():

   global game_running
   global player
   global winner
   display_board()



   while game_running==True:



      first_turn(player)


      game_finished()

      switch_turn()

      display_board()

      if winner=="X" or winner =="O" :

         print("The Winner is "+ winner)

         exit()

      elif winner == None:

         print("NEXT TURN")



def first_turn(player1):
  value=False
  position = input("Choose a position between 1 to 9:  ")

  while not value:

    while position not in ["1","2","3","4","5","6","7","8","9"]:

        position=input("Choose a position between 1 to 9:  ")

    position=int(position) - 1



    if board[position]=="-":
        value=True
    else:

        print("You can't go there,Try Again")

  board[position]=player1


def switch_turn():
    global player

    if player=="X":
        player="O"

    elif player=="O":
        player="X"


    return

def game_finished():

 check_win()
 check_tie()


def check_tie():
 global game_running
 global winner
 while "-" not in board and winner==None:

     game_running = False
     print("TIE GAME")

     break





def check_win():
    global winner
    global game_running
    check_row()

    check_column()

    check_diagnol()


def check_row():
    global game_running
    global winner
    if board[0]==board[1]==board[2]!="-" :
      print("WE HAVE A WINNER:")
      print("WINNER IS: "+ board[0])
      winner=board[0]
      game_running==False

    elif board[3]==board[4]==board[5]!="-" :
        print("WE HAVE A WINNER:")
        print("WINNER IS: " + board[4])
        winner=board[3]
        game_running == False


    elif board[7] == board[8] == board[6] != "-":
        print("WE HAVE A WINNER:")
        print("WINNER IS: " + board[6])
        winner=board[6]
        game_running == False


    else:
        game_running == True





def check_column():
 global winner
 global game_running
 if board[0] == board[3] == board[6] != "-":
    print("WE HAVE A WINNER:")
    print("WINNER IS: " + board[0])
    winner = board[0]
    game_running == False

 elif board[1] == board[4] == board[7] != "-":
    print("WE HAVE A WINNER:")
    print("WINNER IS: " + board[4])
    winner = board[1]
    game_running == False


 elif board[2] == board[5] == board[8] != "-":
    print("WE HAVE A WINNER:")
    print("WINNER IS: " + board[6])
    winner = board[2]
    game_running == False


 else:
    game_running == True



def check_diagnol():
 global winner
 if board[0] == board[4] == board[8] != "-":
     print("WE HAVE A WINNER:")
     print("WINNER IS: " + board[0])
     winner = board[0]
     game_running == False

 elif board[2] == board[4] == board[6] != "-":
     print("WE HAVE A WINNER:")
     print("WINNER IS: " + board[4])
     winner = board[2]
     game_running == False

 else:
     game_running == True;

run_game()






