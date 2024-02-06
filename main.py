import os
import threading
print("HELLO")

def start_thread():
    os.system("python driver.py ThomasGust 1 0 0")

threads = []
for i in range(3):
    threads.append(threading.Thread(target=start_thread))
    threads[i].start()
