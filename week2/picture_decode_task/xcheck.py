import time
import psutil
import os

from picture_decode_costi import read_file, save_pict_to_file

def check():
    start_time = time.time()
    process = psutil.Process(os.getpid())
    start_memory = process.memory_info().rss

    #function here
    
    save_pict_to_file(read_file('hard\\example.txt'), 'hard\\result.txt')
    
    end_time = time.time()
    end_memory = process.memory_info().rss

    print(f"Execution time: {end_time - start_time} seconds")
    print(f"Memory used: {end_memory - start_memory} bytes")

    return True

if __name__ == '__main__':
    check()