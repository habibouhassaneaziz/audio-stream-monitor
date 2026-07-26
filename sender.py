import socket
import wave
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
CHUNK = 1024
sent_packets = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with wave.open("audio.wav", "rb") as wf:
    data = wf.readframes(CHUNK)
    while data:
        sock.sendto(data, (UDP_IP, UDP_PORT))
        sent_packets += 1
        print(f"Paquet envoyé : {sent_packets}")
        time.sleep(0.02)
        data = wf.readframes(CHUNK)

print(f"Total paquets envoyés : {sent_packets}")
sock.close()