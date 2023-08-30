import sys
game=[" "," "," ", " ", " "," "," ", " "," "]
move=0
def print_game():
    print(game[0]+" | "+game[1]+"| "+game[2])
    print("__|__|__")
    print(game[3]+" | "+game[4]+"| "+game[5])
    print("__|__|__")
    print(game[6]+" | "+game[7]+"| "+game[8])
    print("  |  |  ")    
def begin():
    n=2
    print("press 1) Player1 ='x'and player2='0'\n 2)Player1='0' and player2='x'")
    tr=int(input())
    if tr==1:
        p1='X'
        p2='O'
    else:
        p1='O'
        p2='X'
    while True:
        print("Player 1's turn ")
        player(p1)
        n=check_result(p1,p2)
        if n==1:
            sys.exit()
        elif n==2:
            sys.exit()
        print("Player 2's turn")
        player(p2)
        n=check_result(p1,p2)
        if n==1:
            sys.exit()
        if n==2:
            sys.exit()
def player(p):    
    print("choose an empty space from 1-9")
    t=int(input())
    if game[t-1] !=' ' :
        print("space not empty")
        player(p)
    else:
        game[t-1]=p
        print_game()
def check_result(p1, p2):
    ti=8
    value = 6
    for i in range(8):
        if game[i] == " ":
            game[i] = 6
    solution1 = list(set((game[0], game[4], game[8])))  # values can't be repeated in a set by default
    solution2 = list(set((game[0], game[3], game[6])))
    solution3 = list(set((game[1], game[4], game[7])))
    solution4 = list(set((game[3], game[4], game[5])))
    solution5 = list(set((game[2], game[5], game[8])))
    solution6 = list(set((game[2], game[4], game[6])))
    solution7 = list(set((game[6], game[7], game[8])))
    solution8 = list(set((game[0], game[1], game[2])))
    result = [solution1, solution2, solution3, solution4, solution5, solution6, solution7, solution8]   
    for i in range(8):
        if len(result[i]) == 1 and result[i][0] != 6:
            if result[i][0] == p1:
                print("Player 1 wins")
            else:
                print("Player 2 wins")
            value = 5               
    for i in range(8):
        if game[i] == 6:
            game[i] = " "
    if ' ' not in game and value!=5:
        print("It's a draw")
        ti=9
    if value == 5:
        return 1
    elif ti==9:
        return 2
    else:
        return 3
print("The pattern of tic tac toe board is as follows")
print("1 |2 |3")
print("__|__|__")
print("4 |5 |6")
print("__|__|__")
print("7 |8 |9")
begin()
