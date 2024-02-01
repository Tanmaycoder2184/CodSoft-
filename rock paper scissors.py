#!/usr/bin/python3

def take_user_input():
  while is_the_input_ok == False:
    user_in = input("Hey please give us your input out of Rock/Paper/ Scissor (R/P/S) - ")
    if user_in == 'R' or user_in == 'P' or user_in == 'S' :
      is_the_input_ok = True
  return user_in
  import random
def generate_computer_choice():
 lt = ('R','P','S')
 return random.choice(lt)
generate_computer_choice()
def check_winner(c,u):
 if c =='R' and u =='R':
  return 'D'
 elif c == 'P' and u == 'P':
  return 'D'
 elif c == 'S' and  u == 'S':
  return 'D'
 elif c == 'R' and u == 'P':
  return 'u'
 elif c == 'P' and u == 'R':
  return  'c'
 elif c == 'S' and  u == 'R':
  return 'u'
 elif c == 'R' and u == 'S':
  return 'c'
 elif c == 'P' and u =='S':
  return  'u'
 elif c == 'S' and u == 'P':
  return  'c'
  from IPython.display import clear_output
  def show_score_board(dt):
   print("----------------")
  print("|--Score Board--|")
  print("|User - ",dt.get("u_score"),"    |")
  print("|Comp - ",dt.get("c_score"),"    |")
  print("|Draw - ",dt.get("draw"),"    |")
  print("----------------")
  print("")
  play_again = 'y'
score_dt = {'u_score':0,'c_score':0,'draw':0}

while play_again == 'y':
  winner = check_winner(generate_computer_choice(),take_user_input())

  if winner == 'D':
    print("It was a Draw!!")
    score_dt['draw'] = score_dt['draw'] + 1
  elif winner == 'C':
    print("Computer Wins!!")
    score_dt['c_score'] = score_dt['c_score'] + 1
  else:
    print("User Wins!!")
    score_dt['u_score'] = score_dt['u_score'] + 1

  play_again = input("Do you wanna play again (y/n) - ")
  clear_output(wait=True)
  show_score_board(score_dt)