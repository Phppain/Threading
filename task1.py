"""task1.py"""

import threading
from time import sleep, time

def create_file(i):
    sleep(1)
    with open(f"file_{i}.txt", 'w') as f:
        f.write(f"file_{i} created")

if __name__ == "__main__":
    start_time = time()
    for i in range(100):
        create_file(i)
    end_time = time()
    start2_time = time()
    for i in range(100):
        thread = threading.Thread(target=create_file, args=(i, ))
        thread.start()
    end2_time = time()
    print("Classic way:", end_time - start_time)
    print("Threading way:", end2_time - start2_time)