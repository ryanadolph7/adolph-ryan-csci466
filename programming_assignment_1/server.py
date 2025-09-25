import socket 
import random
import copy
import sys 



initial_port = 0
if sys.argv[1].isdigit():
    initial_port = int(sys.argv[1])
port = initial_port

print("Starting server on port " + str(port) + " ...")
host = socket.gethostname()

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # create TCP socket

serverSocket.bind( (host, port) )       # bind to port and host
serverSocket.listen(1)             # listen for connections

connection, adrr = serverSocket.accept()    # accept connection from client, waits for connection

#data = connection.recv(1024).decode()        

#print(data)

#connection.send("Got it!!!!".encode())
grid = [[0 for _ in range(6)] for _ in range(6)]

#grid = [[0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0,], [1, 0, 0, 1, 1, 1], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]


#for row in grid:
#    print(" ".join(str(num) for num in row))
#print("\n")
#print(grid)
ship_size = 4

def fill_grid(grid, ship_size):
    #always place the 4 ship first
    row_or_col = random.choice([True, False])

    if row_or_col == True: 
        if(ship_size == 4):
            random_row = random.randint(0, 2)
            random_col = random.randint(0, 5)
            for i in range(ship_size):
                grid[random_row + i][random_col] = 1 
        elif(ship_size == 3):
            random_row = random.randint(0, 3)
            random_col = random.randint(0, 5)
            check = valid(grid, random_row, random_col, ship_size, row_or_col)
            if check == True: 
                for i in range(ship_size):
                    grid[random_row + i][random_col] = 1
            while not check: 
                random_row = random.randint(0, 3)
                random_col=  random.randint(0, 5)
                check = valid(grid, random_row, random_col, ship_size, row_or_col)
            for i in range(ship_size):
                grid[random_row + i][random_col] = 1
        elif(ship_size == 2):
            random_row = random.randint(0, 4)
            random_col = random.randint(0, 5)
            check = valid(grid, random_row, random_col, ship_size, row_or_col)
            if check == True: 
                for i in range(ship_size):
                    grid[random_row + i][random_col] = 1
            while not check: 
                random_row = random.randint(0, 3)
                random_col=  random.randint(0, 5)
                check = valid(grid, random_row, random_col, ship_size, row_or_col)
            for i in range(ship_size):
                grid[random_row + i][random_col] = 1
    if row_or_col == False: 
        if(ship_size == 4):
            random_row = random.randint(0, 5)
            random_col = random.randint(0, 2)
            for i in range(ship_size):
                grid[random_row][random_col + i] = 1 
        elif(ship_size == 3):
            random_row = random.randint(0, 5)
            random_col = random.randint(0, 3)
            check = valid(grid, random_row, random_col, ship_size, row_or_col)
            if check == True: 
                for i in range(ship_size):
                    grid[random_row][random_col + i] = 1
            while not check: 
                random_row = random.randint(0, 5)
                random_col=  random.randint(0, 3)
                check = valid(grid, random_row, random_col, ship_size, row_or_col)
            for i in range(ship_size):
                grid[random_row][random_col + i] = 1
        elif(ship_size == 2):
            random_row = random.randint(0, 5)
            random_col = random.randint(0, 4)
            check = valid(grid, random_row, random_col, ship_size, row_or_col)
            if check == True: 
                for i in range(ship_size):
                    grid[random_row][random_col + i] = 1
            while not check: 
                random_row = random.randint(0, 5)
                random_col=  random.randint(0, 4)
                check = valid(grid, random_row, random_col, ship_size, row_or_col)
            for i in range(ship_size):
                grid[random_row][random_col + i] = 1

    return grid

def valid(grid, random_row, random_col, ship_size, row_or_col):
    is_good = 0
    if row_or_col == True:
        for i in range(ship_size):
            if(grid[random_row + i][random_col] == 0):
                is_good += 1
        if (is_good == ship_size):
            return True
    elif row_or_col == False:
        for i in range(ship_size):
            if(grid[random_row][random_col + i] == 0):
                is_good += 1
        if (is_good == ship_size):
            return True 
    return False

#connection.send("Got it!!!!".encode())
games_on = True
total_hits = 0

fill_grid(grid, 4)
# for row in grid:
#     print(" ".join(str(num) for num in row))
# print("\n")
fill_grid(grid, 3)
# for row in grid:
#     print(" ".join(str(num) for num in row))
# print("\n")
fill_grid(grid,2)
for row in grid:
    print(" ".join(str(num) for num in row))
print("\n")


guessed_grid = [[0 for _ in range(6)] for _ in range(6)]

while(True):
    if total_hits == 9:
        games_on = False
        print("Game Over!")
        break

    data = connection.recv(1024).decode()            

    row = int(data[0])
    col = int(data[2])
    
    if(guessed_grid[row][col] == 'X'):
        connection.send("You alreay guessed that spot".encode())
    elif(grid[row][col] == 1): 
        connection.send("Hit".encode())
        guessed_grid[row][col] = 'X'
        total_hits += 1
    elif(grid[row][col] == 0):
        connection.send("Miss".encode())
        guessed_grid[row][col] = 'X'
    #print(grid[row][col]) 

    #for row in grid:
    #    print(" ".join(str(num) for num in row))
    #print("\n")

