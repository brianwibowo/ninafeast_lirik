from time import sleep
import time
import sys

def print_lirik():
    line = [
        ("Ini sumpahku padamu 'tuk biarkanmu",0.09),
        ("Tumbuh lebih baik, cari panggilanmu",0.14),
        ("Jadi lebih baik dibanding diriku",0.13),
        ("'Tuk sementara, kita tertawakan",0.15),
        ("Berbagai hal yang lucu dan lara",0.15),
        ("Selepas-lepasnya",0.12),
        ("Saat dewasa kau 'kan mengerti",0.13),
        ]
    delays=[0, 0, 1.8, 0, 0.2, 0.4, 5] 
    
    for i, (line, char_delay) in enumerate(line):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')
print_lirik()      