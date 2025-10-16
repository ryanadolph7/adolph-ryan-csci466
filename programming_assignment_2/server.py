import socket 
import sys
import pickle



class Packet:
    # Sequence number
    # checksum
    # length
    # message 
    def __init__(self, seq_num, check, length, msg): 
        self.seq_num = seq_num
        self.check = check
        self.length = length
        self.msg = msg
    
    def get_check(self):
        return self.check

    def get_sequence(self):
        return self.seq_num
        
    def get_msg(self): 
        return self.msg

    def get_length(self):
        return self.length

def main():
    
    initial_port = 0
    prob = 0.0
    mss = 0
    # command line args
    if sys.argv[2].isdigit():
        prob = float(sys.argv[2])
    corrupt_prob = prob 
    if sys.argv[3].isdigit():
        mss = int(sys.argv[3])
    MSS = mss
    if sys.argv[1].isdigit():
        initial_port = int(sys.argv[1])
    port = initial_port

    print("Starting server on port " + str(port) + " ...")
    host = socket.gethostname()
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # create TCP socket
    serverSocket.bind( (host, port) )       # bind to port and host
    serverSocket.listen(1)             # listen for connections
    connection, adrr = serverSocket.accept()    # accept connection from client, waits for connection

    capybara = bytearray()                  # output capybara received from client 


    while True:
        data = connection.recv(60000)         # huge buffer for the receiver just in case 
        
        packet = pickle.loads(data)               # load the data   
        
        if len(packet.get_msg()) != packet.get_length():        # some half assed "check sum" thing i thought
            print("Packet corrupted")                           # i thought worked 
            continue
        else: 
            print("Packet received")
            print(packet.get_sequence())
            print(packet.get_length()) 
            print(len(packet.get_msg()))
            capybara.extend(packet.get_msg())
            
            if packet.get_msg() == b"FIN":
                print("Final packet received")
                break
        print("\n")

    with open("output_capybara.jpg", "wb") as f:
        f.write(capybara)


if __name__ == "__main__": 
    main()