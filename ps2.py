from os import system

size=3
winsum=15

# function to display all lines, if needed
def display(lines):
    for i in lines:
        for j in i:
            print(j,end=" ")
        print()

lines=[[]]
# adding all horizontal lines
for i in range(size):
    temp=[] 
    for j in range(size):
        temp.append(i*size+j)
    lines.append(temp)
# adding all verticalal lines
for i in range(size):
    temp=[] 
    for j in range(size):
        temp.append(i+size*j)
    lines.append(temp)
# adding diagonal lines
temp=[] 
for i in range(size):
    temp.append(i+size*i)
lines.append(temp)
temp=[] 
for i in range(size):
    temp.append(size*i+size-i-1)
lines.append(temp)
# display(lines)

# function to display board
def bdisplay(board):
    for i in range(size):
        print(end="\n\t")
        for j in range(size):
            if(board[i*size+j]==-1):
                print("_",end="\t")
            else:
                print(board[i*size+j],end="\t")
# board for playing the game
board=[]
for i in range(size*size):
    board.append(-1)
numbers=[]
for i in range(size*size):
    numbers.append(False)
# bdisplay(board)

# function to check whether game is over
def gameover(board,lines):
    for i in lines:
        sum=0
        for j in i:
            if(board[j]==-1):
                sum=0
                break
            else:
                sum+=board[j]
        if(sum==winsum):
            # for j in i:
            #     print(j,end=" ")
            # print()
            return True
    return False
# Starting the Game
player=0
while(1):
    # checking if a game is already over, then will show option to exit/continue
    if(player==size*size):
        system("clear")
        new=input("Do you want to start a new Game (y/n) : ")
        if(new=="y"):
            for i in range(size*size):
                board[i]=-1
                numbers[i]=False
            player=0
        elif(new=="n"):
            break
        else:
            continue
    # displaying game menus
    while(1):
        system("clear")
        print("\n\t Welcome to the Game!\n")
        # Displaying the board
        bdisplay(board)
        print("\n\n\n\tplayer",(player%2)+1,"'s chance")
        pos=input("Enter Position : ")
        val=input("Enter value : ")
        # checking whether inputs are valid
        if(pos.isnumeric() and val.isnumeric()):
            pos=int(pos)
            val=int(val)
        else:
            print("\n\tInvalid Input\n\nPress ENTER to continue")
            input()
            continue
        if(pos<1 or val<1 or pos>size*size or val>size*size or board[pos-1]!=-1 or numbers[val-1]):
            print("\n\tInvalid Input\n\nPress ENTER to continue")
            input()
            continue
        elif((player%2)==0 and val%2==0):
            print("\nERROR : Player 1 is only allowed to enter odd values")
            print("\nPress ENTER to continue")
            input()
            continue
        elif((player%2)==1 and val%2!=0):
            print("\nERROR : Player 2 is only allowed to enter even values")
            print("\nPress ENTER to continue")
            input()
            continue
        else:
            # updating the board with entered value
            board[pos-1]=val
            # checking if player has won the game
            if(gameover(board,lines)):
                print("\tPlayer",(player%2)+1,"wins the game")
                print("\nPress ENTER to continue")
                player=size*size
                input()
                break
            # checking if the board is completely filled
            elif(player==size*size-1):
                print("\tGame ends in a draw")
                print("\nPress ENTER to continue")
                input()
                player=size*size
                break
            # changing player
            else:
                numbers[val-1]=True
                player=player+1
    

