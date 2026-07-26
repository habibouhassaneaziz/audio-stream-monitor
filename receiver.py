import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 5005
CHUNK = 4096
received_packets = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("En écoute...")
while True:
    data, addr = sock.recvfrom(CHUNK)
    received_packets += 1
    print(f"Paquet reçu : {received_packets}")