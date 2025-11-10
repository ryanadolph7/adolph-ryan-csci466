import socket
import sys
import time
import random

class Node:
    def __init__(self, sender_port, receiving_port, packet_num, is_head, node_num, message):
        self.sender_port = sender_port
        self.receiving_port = receiving_port
        self.packet_num = packet_num
        self.is_head = is_head
        self.node_num = node_num        
        self.message = message


def main(): 

    # set up node from command line
    sender_port = 0
    if (sys.argv[1].isdigit()):
        sender_port = int(sys.argv[1])
    receiving_port = 0
    if (sys.argv[2].isdigit()):
        receiving_port = int(sys.argv[2])
    packet_num = 0
    if (sys.argv[3].isdigit()):
        packet_num = int(sys.argv[3])
    is_head = False
    if (sys.argv[4] == '1'):
        is_head = True
    node_num = 0
    if (sys.argv[5].isdigit()):
        node_num = int(sys.argv[5])
    
    message = "I am the message being sent .... hehehehehe"
    messages = []
    for i in range(packet_num):
        messages.append(message + " " + str(i))

    node = Node(sender_port, receiving_port, packet_num, is_head, node_num, messages)

    if(not is_head):
        print("Node {} is receiving on port {}".format(node_num, receiving_port))

    #print(sender_port, receiving_port, packet_num, is_head, node_num)
    # if we are the head, we are sending a message, otherwise were are receiving
    while True:
        if is_head:
            
            if not node.packet_num == 0:
                print("sending packet to the internet\n")
                print(node.message[0])
                node.packet_num -= 1
                random_num = random.random()
                node.message.pop()
                if(random_num <= .25):
                    node.message.append(message)
            elif node.packet_num == 0:
                print("I have no packets left to send\n")
                time.sleep(.25)
                random_num = random.random()
                if(random_num <= .25):
                    print("I have received a new token!\n")
                    node.message.append(message)
                    pass

            host = socket.gethostname()
            recv_port = receiving_port
            connection = (host, recv_port)
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            clientSocket.bind( connection )
            send_host = socket.gethostname()
            send_port = sender_port
            send = (send_host, send_port)
            clientSocket.sendto(message.encode(), send)
            clientSocket.close()
            time.sleep(.5)
            is_head = False
            print("\n")
        elif not is_head:
            print("Waiting for data")
            host = socket.gethostname()
            recv_port = receiving_port
            connection = (host, recv_port)
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            serverSocket.bind( connection )
            received = False
            message_received = ""
            while(not received):
                data = serverSocket.recvfrom(1024)
                message_received = data[0].decode()
                connection = data[1]
                print("Message Received " + message_received)
                received = True
                is_head = True
                # data[0] = message
                # data[1] = remote socket connection     
            serverSocket.close()
            time.sleep(.5)
            print("\n")
            
        
        time.sleep(.5)
    return 


if __name__ == '__main__':
    main()