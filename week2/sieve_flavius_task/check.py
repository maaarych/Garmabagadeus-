import time
import psutil
import os

from sieve_flavius_copy import sieve_flavius

def check():
    start_time = time.time()
    process = psutil.Process(os.getpid())
    start_memory = process.memory_info().rss

    #function here
    sieve_flavius(1000)

    end_time = time.time()
    end_memory = process.memory_info().rss

    print(f"Execution time: {end_time - start_time} seconds")
    print(f"Memory used: {end_memory - start_memory} bytes")

    return True

if __name__ == '__main__':
    check()