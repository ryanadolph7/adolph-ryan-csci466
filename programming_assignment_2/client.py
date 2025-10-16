import socket
import sys
import time
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
    size = 0
    all_data = bytearray()
    packet_list = []
    with open("capybara.jpg", "rb") as f:
        size += 1 
        data = f.read()
        all_data.extend(data)

    # get all the data together from capybara.jpg image and split into serialized data of 2000 bytes
    serialized_data = [[0 for _ in range(2000)] for _ in range(len(all_data) // 2000 + 1)]
    index = 0
    data_index = 0
    for byte in all_data: 
        if data_index == 2000: 
            data_index = 0
            index += 1
        serialized_data[index][data_index] = byte
        data_index += 1
    seq_num = 0
    for seq_num in range(len(serialized_data)):
        packet = Packet(seq_num + 1, True, len(serialized_data[seq_num]), serialized_data[seq_num])
        packet_list.append(packet)

    packet_list.append(Packet(seq_num + 2, True, len(b"FIN"), b"FIN"))         # final packet
    
    # command line args
    if sys.argv[2].isdigit():
        prob = float(sys.argv[2])
    corrupt_prob = prob 
    #print(corrupt_prob)
    if sys.argv[3].isdigit():
        mss = int(sys.argv[3])
    MSS = mss
    #print(MSS)
    if sys.argv[1].isdigit():
       initial_port = int(sys.argv[1])
    port = initial_port

    host = socket.gethostname()
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect( (host, port) )
    print("Connected on port " + str(port) + "\n")
    # need to check that send buffer isnt full, once it is, send then wait for ack
    # then reload buffer and repeat until all data sent
    #print(len("capybara.jpg"))
    #print(len("capybara.jpg") % 2000 + 1)
    #time.sleep(1)

    for each_packet in packet_list: 
        print("Sending", each_packet.get_sequence())
        packet = pickle.dumps(each_packet)
        clientSocket.sendall(packet)
        time.sleep(1)       
    
    


if __name__ == "__main__": 
    main()