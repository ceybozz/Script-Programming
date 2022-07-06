# modules
import time, datetime # Import time functions
import concurrent.futures # Provides asynchronous execution on threads
import psutil # imports info on running processes
import multiprocessing # Imports functions from multiprocessing/__init__.py
import numpy # Import mathematical operations


# Constants, Variables
UI32 = numpy.iinfo(numpy.uint32)
# share variable between processes, notice large V in .Value
KEY_NOT_FOUND = multiprocessing.Value('i', True) # Key not found Constant
secret_key = numpy.random.randint(low=0, high=UI32.max, dtype='uint32')    # Secret key random
secret_key = numpy.uint32(911923)  # Secret key not a random
cpu_count = psutil.cpu_count(logical=True)  # True = show all CPU's

# init_globals functions for processes
def init_globals(key_not_found):   
    global KEY_NOT_FOUND
    KEY_NOT_FOUND = key_not_found

# crack_something method with funcitons to crack
# multiprocess function, notice small v in .value
def crack_something(cpu, cur_key, end_key):
    print(f'CPU: {cpu} keyspace start at {cur_key} and end at {end_key}')
    # While loop to count the CPU's on PC
    while KEY_NOT_FOUND.value and (cur_key <= end_key):
        if (cur_key == secret_key):
            KEY_NOT_FOUND.value = False
            return f'CPU: {cpu} found secret key at: {cur_key}'
        else:
            cur_key = cur_key + 1
        if (cur_key % 1000000 == 0):
            print(f'CPU: {cpu} is at key: {cur_key}') # Shows CPU at current key
    return f'CPU: {cpu} reached key at: {cur_key}' # Shows every CPU ends

# main funnciotns
def main(): 
    print(f'Random Secret key is at: {secret_key}') # Key value
    print(f'CPU (process) count is at: {cpu_count}') #CPU's
    start_keys = []
    end_keys = []
    cpus = []   
    cpu_key_space = numpy.uint32(UI32.max / cpu_count)
    for i in range(0, cpu_count):
        cpus.append(i)
        start_keys.append(i * cpu_key_space)
        end_keys.append((i+1) * cpu_key_space)
    end_keys[-1] = numpy.uint32(UI32.max)
    print(f'Start keyspace offsets at: {start_keys}')
    print(f'End keyspace offsets at: {end_keys}')
    key_not_found = multiprocessing.Value('i', True)
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count, initializer=init_globals, initargs=(key_not_found,)) as executor:
        for result in executor.map(crack_something, cpus, start_keys, end_keys):
            print(result)
    return

# Init
if __name__ == '__main__':
    start = time.perf_counter() # start time
    main()
    finish = time.perf_counter() # end time
    print(f'Finished in {round(finish-start, 2)} seconds') # Calc time
    keys_sec = int(secret_key / round(finish-start, 2) * cpu_count) # Calc keys per seconds
    print(f'Around {keys_sec} keys per second was tested')
    total_time = str(datetime.timedelta(seconds=int(numpy.uint32(UI32.max)/keys_sec))) # Calc brute force keyspace time
    print(f'To brute force the whole keyspace would take around {total_time} HH:MM:SS')