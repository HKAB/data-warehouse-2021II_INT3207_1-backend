import sqlite3
import requests
from pprint import pprint
import threading
import queue
import sys

API_KEY = "GqfwrZUEfxbwbnQUhtBMFivEysYIxelQ"
URL = "https://apis.wemap.asia/geocode-1/search?text={}&key=" + API_KEY

con = sqlite3.connect('../db/JOB.db', check_same_thread=False)
cur = con.cursor()

nohope = 0
success = 0

q = queue.Queue()
workers = []
thread_lock = threading.Lock()
thread_stop = False

for row in cur.execute("SELECT rowid, officeLocation FROM job"):
    q.put(row)

def get_stuff(query):
    response = requests.get(URL.format(query)).json()
    features = response.get('features')
    if features:
        return features[0]['geometry']['coordinates']
    else:
        return []

def run():
    cur = con.cursor()
    print('Threading run')
    global q, nohope, success, thread_stop, thread_lock
    while not q.empty() and not thread_stop:
        try:
            rowid, query = q.get(block=False)
            coordinates = get_stuff(query)
            with thread_lock:
                if coordinates:
                    print(coordinates)
                    cur.execute("UPDATE job SET long=?, lat=? WHERE rowid=?", (coordinates[0], coordinates[1], rowid))
                    success += 1
                else:
                    nohope += 1
        except queue.Empty:
            print("Terminating thread")
            return
        except KeyboardInterrupt:
            thread_stop = True
            return

for i in range(10):
    worker = threading.Thread(target=run)
    worker.start()
    workers.append(worker)

try:
    [w.join() for w in workers]
except KeyboardInterrupt:
    thread_stop = True
    sys.exit()
con.commit()
if nohope and success:
    print("Sadgely, we have {}/{} with failure rate of {}%".format(success, success + nohope, nohope / (nohope + success) * 100))
