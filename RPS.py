# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
  if prev_play!='':
    opponent_history.append(prev_play)

   
  pattern=['R','P','S']
  if prev_play=="":
    import random
    guess=random.choice(pattern)
  else:

    last_move=pattern.index(opponent_history[-1])
    next_move=(last_move+1)%len(pattern)
    guess=pattern[next_move]
  return guess


# def player(prev_play,oppoent_history=[]):
#   if prev_play!="":
#     oppoent_history.append(prev_play)
#   pattern={"RR": "P",
#         "RP": "S",
#         "RS": "R",
#         "PP": "R",
#         "PS": "S",
#         "PR": "P",
#         "SS": "R",
#         "SR": "P",
#         "SP": "S"}
#   if len(oppoent_history)>=2:
#     last_two_moves=oppoent_history[-2]+oppoent_history[-1]
#     if last_two_moves in pattern:
#       guess=pattern[last_two_moves]
#     else:
#       import random
#       guess= random.choice(["R","P","S"])
#   else:
#     import random
#     guess=random.choice(["R","P","S"])


#   return guess


