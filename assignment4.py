import sys
#reading input part and creating new variables.
board=[]
file=open(sys.argv[1],"r") 
for i in file.readlines():
    board.append(i.split())

row_size=len(board)-1
coulumn_size=len(board[0])-1
total_p=0
row_check=True
coulumn_check=True

#This is my main function.I can mark the letters to 0 by using main function.
def main(row,coulumn):
    if coulumn!=coulumn_size:
        if board[row][coulumn+1]!=color:
            pass
        
        else:
            board[row][coulumn]=0
            board[row][coulumn+1]=0
            main(row,coulumn+1)
            
            
    if row!=row_size:
        if board[row+1][coulumn]!=color:
            pass
        else:
            board[row][coulumn]=0
            board[row+1][coulumn]=0
            main(row+1,coulumn)
    if row!=0:
        if board[row-1][coulumn]!=color:
            pass
        else:
            board[row][coulumn]=0
            board[row-1][coulumn]=0
            main(row-1,coulumn)
            
    if coulumn!=0:
        if board[row][coulumn-1]!=color:
            pass
        else:
            board[row][coulumn]=0
            board[row][coulumn-1]=0
            main(row,coulumn-1)
    return board

#This is my move function.After marking  the letters,i make their movements with this function and there are three parts of move function.
def move():
#Part 1: 0'ları üste atma
    for c in range(len(board[0])):
        index=len(board)-1
        for r in range(len(board)-1,-1,-1):
            if board[r][c]!=0:
                board[index][c]=board[r][c]
                index-=1  
        for r in range(index,-1,-1):
            board[r][c]=0
#part 2:eğer bütün kolonlar 0 ise o kolonu en sağa atma
    count=0
    while count <row_size:
        for i in range(coulumn_size+1):
            x=[]
            for j in range(row_size+1):
                if board[j][i]==0:
                    x.append(board[j][i])
            if x.count(0)==row_size+1:
                for t in range(row_size+1):
                    try:
                        board[t][i]=board[t][i+1]
                        board[t][i+1]=0
                    except:
                        pass
        count+=1
#part 3: eğer bütün satır 0 ise o satırı en alta atma
    count=0
    while count<row_size:
        for i in range(row_size):
            x=[]
            for j in range(coulumn_size):
                if board[i][j]==0:
                    x.append(board[i][j])
            if x.count(0)==coulumn_size:
                board[i]=board[i+1]
                board[i+1]=[]
                for t in range(coulumn_size+1):
                    board[i+1].append(0)
        count+=1
    return board
#I create a new function for bomb.
def bomb(row,coulumn):
    board[row][coulumn]=0
    for i in range(row_size+1):
        if board[i][coulumn]=="X":
            bomb(i,coulumn)
        else:
            board[i][coulumn]=0
    for j in range(coulumn_size+1):
        if board[row][j]=="X":
                    bomb(row,j)
        else:
            board[row][j]=0
#This is my print function.After all the process,I print the board.
def print_board():

    print()
    for i in range(row_size+1):
        if board[i].count(0)==coulumn_size+1:
            pass
        else:
            for j in range(coulumn_size+1):
                if board[i][j]==0:
                    print(" ",end=" ")
                    
                else:
                    print(board[i][j],end=" ")

            print()
            
    print()
#This is my point function.I initially calculated the scores of all the letters on the board then I recalculated the board after selecting the letters and converting them to 0
def point():
    total_p=0
    for i in range(row_size+1):
        for j in range(coulumn_size+1):
            if board[i][j]=="B":
                total_p+=9
            elif board[i][j]=="G":
                total_p+=8
            elif board[i][j]=="W":
                total_p+=7
            elif board[i][j]=="Y":
                total_p+=6
            elif board[i][j]=="R":
                total_p+=5
            elif board[i][j]=="P":
                total_p+=4
            elif board[i][j]=="O":
                total_p+=3
            elif board[i][j]=="D":
                total_p+=2
            elif board[i][j]=="F":
                total_p+=1
    return total_p
#As i said before,this is the total score of the board.I called the function before the calculations because i wanted to calculate all points on the board.
all_points=point()
#And before the start i wanted to print full board and point 
print_board()
print("Your score is:",all_points-point(),"\n")

#in this part,i take input from user .if row_check and coulumn_check is False (If 2 letters are not the same next to each other or on top of each other),loop is ending 
while row_check==True or coulumn_check==True:
    for i in range(row_size):
        for j in range(coulumn_size):
            if board[i][j]==board[i][j+1]!=0 or board[i][j]=="X":
                row_check=True
                break
            else:
                row_check=False
        if row_check==True:
            break
    for i in range(coulumn_size):
        for j in range(row_size):
            if board[j][i]==board[j+1][i]!=0 or board[j][i]=="X":
                coulumn_check=True
                break
            else:
                coulumn_check=False
        if coulumn_check==True:
            break
    if row_check==False and coulumn_check==False :
        print("GAME OVER!")
        break
    else:
        #I am taking input and calling functions for calculations.
    
        try:
            pick=input("Please enter a row and coulumn number:")
            deneme=pick.split()
            row=int(deneme[0])
            coulumn=int(deneme[1])
            color=board[row][coulumn]
            if color==0:
                print("please enter a valid size!")
            elif color=="X":
                bomb(row,coulumn)
                move()
                print_board()
                print("Your score is:",all_points-point(),"\n")
        

            else:
                main(row,coulumn)
                move()
                print_board()
                print("Your score is:",all_points-point(),"\n")
        except IndexError :
            print("Please enter a valid size!")
    

    
    



            

         


        
       








                
        

