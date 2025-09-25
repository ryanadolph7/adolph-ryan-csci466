import socket
import sys 

initial_port = 0
if sys.argv[1].isdigit():
    initial_port = int(sys.argv[1])
#print(initial_port)
port = initial_port
host = socket.gethostname()

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect( (host, port) )
print("Connected on port " + str(port) + "\n")

#clientSocket.send("hello!!!".encode())

#response = clientSocket.recv(1024).decode()
#print(response)
grid = [[0 for i in range(6)] for j in range(6)]
game_over = False
total_hits = 0
total_guess = 0
for row in grid:
    print(" ".join(str(num) for num in row))
print("\n")
while(not game_over):
    message = input("Enter a coordinate in row col format: ")
    if(int(message[0]) > 5 or int(message[2]) > 5 or int(message[0]) < 0 or int(message[2]) < 0):
        print("Invalid input, try again")
        continue    
    clientSocket.send(message.encode())
    response = clientSocket.recv(1024).decode()
    
    #print(response)

    
    if(grid[int(message[0])][int(message[2])] == 1):
        print("You already hit that spot")
        total_guess += 1
        continue
    elif(grid[int(message[0])][int(message[2])] == 'X'):
        print("You already missed that spot")
        total_guess += 1
        continue
    elif(response == "Hit"):
        grid[int(message[0])][int(message[2])] = 1
        total_hits += 1
        print("It's a hit!")
        total_guess += 1
    elif(response == "Miss"):
        print("Its a miss!")
        grid[int(message[0])][int(message[2])] = 'X'
        total_guess += 1
    
    for row in grid:
        print(" ".join(str(num) for num in row))
    print("\n")

    if(total_hits == 9):
        game_over = True

print("Game over! You took " + str(total_guess) + " guesses to sink all the ships.")

