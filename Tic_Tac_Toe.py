import random

game_input = ["Null" , 'X' , 'O' , 'X' , 'O' , 'X' , 'O' , 'X' , 'O' , 'X']

def board(game_input):
    print(game_input[7] + '|' + game_input[8] + '|' + game_input[9])
    print(game_input[4] + '|' + game_input[5] + '|' + game_input[6])
    print(game_input[1] + '|' + game_input[2] + '|' + game_input[3])
    
#board(input_game)

def player_input():
    marker =''
    while marker != 'X' and marker != 'O':
    marker = input('Player1: Please choose your marker: ')
   if marker == 'X': 
      return ('X' , 'O')
   else:
      return('O' , 'X')
      
#player_1, player_2 = player_input()
#print(player_1 + 'is Player 1 symbol')
#print(player_2 + 'is player 2 symbol')

def put_marker(game_input, marker,position,):
    game_input[position] = marker
    
def win(game_input, marker):
     return ((game_input[1] == game_input[2] == game_input[3] == marker)or
             (game_input[4] == game_input[5] == game_input[6] == marker)or
             (game_input[7] == game_input[8] == game_input[9] == marker)or
             (game_input[7] == game_input[5] == game_input[3] == marker)or
             (game_input[1] == game_input[5] == game_input[9] == marker)or
             (game_input[1] == game_input[4] == game_input[4] == marker)or
             (game_input[2] == game_input[5] == game_input[8] == marker)or
             (game_input[3] == game_input[6] == game_input[9] == marker))or
             
def choose_player():
    player =  random.randint(1,2)
    if player == 1:
       return 'player 1'
    else:
       return 'player 2'
       
       
def space(game_input,position):
    return game_input[position] == ''
    

def full_board_check(game_input):
    for i in range(1,10):
    if spcae(game_input,i):
       return False
    return True
    
 
def player_choice(game_input)
     position = 0
     while position not in [1,2,3,4,5,6,7,8,9] or not space(game_input,position):
          position = int(input('Please choose your positon(1-9) On NumPad: '))
     return position
     
     

def play_again():
    choice = input('Would you like to play again[Y/N]: ')
    return choice == 'Y'
    

while

the_board =[' ']*10
player_1, player_2 = player_input()
print(player_1 + 'is player_1 sign')
print(player_2 + 'is player_2 sign')

turn = choose_player()
print(turn + 'will play first')

play_game = input('Ready to Play[Y/N]:')

  if play_game == 'y':
     game_on = True
  else:
     game_on = False
     
  while game_on:
  
  if turn == 'player_1':
      board(the_board)
      position = player_choice(the_board)
      
  put_marker(the_board,player_1,position)
  
  if win(the_board, player_1):
    board(the_board)
    print('Player 1 has Won, Yipeeeeee!!!!!!!')
    game_on = False
    
    
   else: 
        turn ='player_2'
        
else:
   board(the_board)
   position = player_choice(the_board)
   
   put_marker(the_board, player_2, position)
   
   put_marker(the_board,player_1,position)
  
  if win(the_board, player_2):
    board(the_board)
    print('Player 2 has Won, Yipeeeeee!!!!!!!')
    game_on = False
 else:
      if full_board_check(the_board):
         board(the_board):
         print("Game Tie")
         game_on = False
         
  else:
      turn = "player_1"
      
      
 not play_again():
 break
         
