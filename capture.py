from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
import time
import pandas as pd
packets = []

def process_packet(packet):
    if IP in packet:
        info = {
            'time': time.time(),
            'src': packet[IP].src,
            'dst': packet[IP].dst,
            'protocol': packet[IP].proto,
            'length': len(packet)
        }
        packets.append(info)
        print(info)

sniff(prn=process_packet, store=False)



# After collecting packets
df = pd.DataFrame(packets)
df.to_csv('traffic.csv', index=False)