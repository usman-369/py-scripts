import threading
import time
import random

def cpu_intensive_task():
    while True:
        sum(i * i for i in range(10000))

def memory_intensive_task():
    memory_hog = []
    while True:
        memory_hog.append([0] * 1000000)

threads = []

# CPU-intensive threads
for i in range(4):  # Adjust based on your CPU cores
    thread = threading.Thread(target=cpu_intensive_task)
    thread.start()
    threads.append(thread)

# Memory-intensive threads
for i in range(4):
    thread = threading.Thread(target=memory_intensive_task)
    thread.start()
    threads.append(thread)

# Let the threads run for a while
time.sleep(10)

# Optionally join threads (unreachable in this example since the loops are infinite)
for thread in threads:
    thread.join()

while True:
    print(random.randint(0, 1), end=' ')