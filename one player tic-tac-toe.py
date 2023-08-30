import random
import os
import sys
game=[" "," "," ", " ", " "," "," ", " "," "]
def print_game():
    #os.system('cls')
    print(game[0]+" | "+game[1]+"| "+game[2])
    print("__|__|__")
    print(game[3]+" | "+game[4]+"| "+game[5])
    print("__|__|__")
    print(game[6]+" | "+game[7]+"| "+game[8])
    print("  |  |  ")
def begin():
    n=2
    print("press 1) user ='x'and computer='0'\n 2)user='0' and computer='x'")
    tr=int(input())
    if tr==1:
        user='X'
        computer='O'
    else:
        user='O'
        computer='X'
    while (True):
        print("User's turn ")
        user_chance(user)
        n=check_result(user,computer)
        if n==1:
            sys.exit()
        elif n==2:
            sys.exit()
        print("Computer's turn")
        computer_chance(computer)
        n=check_result(user,computer)
        if n==1:
            sys.exit()
        elif n==2:
            sys.exit()
def user_chance(user):    
    print("choose an empty space from 1-9")
    t=int(input())
    if game[t-1] !=' ' :
        print("space not empty")
        user_chance(user)
    else:
        game[t-1]=user
        print_game()
def computer_chance(computer):
    list1=[1,2,3,4,5,6,7,8,9]
    t=random.choice(list1)
    if(game[t-1]!=' '):        
        computer_chance(computer)
    else:
        game[t-1]=computer
        print_game()
def check_result(user,computer):
    value=6
    ti=8
    for i in range(8):
        if game[i]==" ":
            game[i]=6            
    solution1=list(set((game[0],game[4],game[8]))) #values cant be repeated in a set by default
    solution2=list(set((game[0],game[3],game[6])))
    solution3=list(set((game[1],game[4],game[7])))
    solution4=list(set((game[3],game[4],game[5])))
    solution5=list(set((game[2],game[5],game[8])))
    solution6=list(set((game[2],game[4],game[6])))
    solution7=list(set((game[6],game[7],game[8])))
    solution8=list(set((game[0],game[1],game[2])))
    result=[solution1,solution2,solution3,solution4,solution5,solution6,solution7,solution8]    
    for i in range(8):
        if len(result[i])==1 and result[i][0] != 6:
                if result[i][0]==user:
                   print("User wins")
                else:
                   print("Computer wins")
                value=5
    for i in range(8):
	     if game[i]==6:
                game[i]=" "
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
