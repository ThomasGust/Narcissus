import os
import threading
import argparse
import sys


if __name__ == "__main__":

    argumentList = sys.argv[1:]

    options = "hmo:"
    long_options = ["Help", "My_file", "Output="]

    parser = argparse.ArgumentParser()
 
    
    parser.add_argument("-u", "--Username", help = "GitHub Profile Username")
    parser.add_argument("-t", "--Threads", help="Number of windows or threads to be used")
    parser.add_argument("-w", "--Wait-Time", help="Average length of delay in between page reloads")
    parser.add_argument("-v", "--Views", help="The number of views to be added, 0 means run until interrupted")
    

    args = parser.parse_args()
    username = args.Username
    threads = args.Threads
    wt = args.Wait_Time
    views = args.Views

    
    def start_thread():
        os.system(f"python viewer.py {username} {wt} {int(int(views)/int(threads))} 0")

    t= []

    for i in range(int(threads)):
        t.append(threading.Thread(target=start_thread))
        t[i].start()

