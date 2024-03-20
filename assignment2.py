print("""
1.BRUSH DOWN
2.BRUSH UP
3.VEHICLE ROTATES RIGHT
4.VEHICLE ROTATES LEFT
5.MOVE UP TO X
6.JUMP
7.REVERSE DIRECTION
8.VIEW THE MATRIX
0.EXIT
please enter the commands with a plus sign(+) between them
""")

b=True
while b==True:
    a=input(":").split("+")
    matrix_size = int(a[0])
    a.pop(0)
    for i in a:
        if i.startswith('5_'):
            b=False
        elif i=="1" or i=="2" or i=="3" or i=="4" or i=="6" or i=="7" or i=="8" or i=="0":
            b=False
        else:
            print("you entered an incorrect command.Please try again!")
            b=True



matrix = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
vehicle_position = [0, 0]


def print_matrix(matrix):
    # Prints the matrix with + signs around it
    for i in range(matrix_size + 2):
        print("+", end="")
    print("")
    for i in range(matrix_size):
        print("+", end="")
        for j in range(matrix_size):
            if matrix[i][j] == 0:
                print(" ", end="")
            else:
                print("*", end="")
        print("+")
    for i in range(matrix_size + 2):
        print("+", end="")
    print("")
l=[]

def game(vehicle_position):
    brush_status=False
    vehicle_rotation = 1
    count=1
    for i in a:
        if i=="0":
            break
        elif i=="1":
            brush_status=True
            vehicle_position[0]=vehicle_position[0]%matrix_size
            vehicle_position[1]=vehicle_position[1]%matrix_size
            matrix[vehicle_position[0]][vehicle_position[1]]=1
        elif i.startswith('5_'):
            l = [str(t) for t in i]
            del l[0:2]
            b = ''.join(l)
            t = int(b)
            if vehicle_rotation == 1:
                if brush_status==True:
                    count=0
                    while count<t:
                        vehicle_position[1]+=1
                        vehicle_position[1]=vehicle_position[1]%matrix_size
                        matrix[vehicle_position[0]][vehicle_position[1]] = 1
                        count+=1
                else:
                    vehicle_position[1] += t
            elif vehicle_rotation==2:
                if brush_status==True:
                    count=0
                    while count < t:
                        vehicle_position[0] -= 1
                        vehicle_position[0] = vehicle_position[0] % matrix_size
                        matrix[vehicle_position[0]][vehicle_position[1]] = 1
                        count += 1
                else:
                    vehicle_position[0] -= t
            elif vehicle_rotation==3:
                if brush_status==True:
                    count=0
                    while count < t:
                        vehicle_position[1] -= 1
                        vehicle_position[1] = vehicle_position[1] % matrix_size
                        matrix[vehicle_position[0]][vehicle_position[1]] = 1
                        count += 1
                else:
                    vehicle_position[1] -= t
            elif vehicle_rotation==4:
                count=0
                if brush_status==True:
                    while count < t:
                        vehicle_position[0] += 1
                        vehicle_position[0] = vehicle_position[0] % matrix_size
                        matrix[vehicle_position[0]][vehicle_position[1]] = 1
                        count += 1
                else:
                    vehicle_position[0] += t
        elif i=="2":
            brush_status=False
        elif i=="3":
            if vehicle_rotation==1 :
                vehicle_rotation=4
            elif vehicle_rotation==2 :
                vehicle_rotation=1
            elif vehicle_rotation==3 :
                vehicle_rotation=2
            elif vehicle_rotation==4 :
                vehicle_rotation=3
        elif i=="4":
            if vehicle_rotation==1 :
                vehicle_rotation = 2
            elif vehicle_rotation==2 :
                vehicle_rotation = 3
            elif vehicle_rotation==3:
                vehicle_rotation = 4
            elif vehicle_rotation==4 :
                vehicle_rotation = 1
        elif i=="7":
            if vehicle_rotation==1 :
                vehicle_rotation=3
            elif vehicle_rotation==2 :
                vehicle_rotation=4
            elif vehicle_rotation==3 :
                vehicle_rotation=1
            elif vehicle_rotation==4 :
                vehicle_rotation=2

        elif i=="6":
            if vehicle_rotation==1 :
                vehicle_position[1]+=3
                vehicle_position[1] = vehicle_position[1] % matrix_size
                brush_status=False
            elif vehicle_rotation==2 :
                vehicle_position[0]-=3%matrix_size
                vehicle_position[0] = vehicle_position[0] % matrix_size
                brush_status=False
            elif vehicle_rotation==3 :
                vehicle_position[1]-=3
                vehicle_position[1] = vehicle_position[1] % matrix_size
                brush_status=False
            elif vehicle_rotation==4 :
                vehicle_position[0]+=3
                vehicle_position[0] = vehicle_position[0] % matrix_size
                brush_status=False
        elif i=="8":
            print_matrix(matrix)

    return matrix
game(vehicle_position)







