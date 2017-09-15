from multiprocessing import Process, Queue

from primes import calculate_primes_less_than, calculate_primes_between

task_queue = Queue()
result_queue = Queue()

primes = {}
handled = 0 
queued = 1

counter = BasicBlock(1000)
block_contains = counter.block_contains
top_number = counter.top_number


def queue_task(next_block):
    blocks = [ primes[i] for i in range(0, block_contains(need_to_test(top_number(next_block)))) ]
    task = (next_block, blocks)
    task_queue.put(task)
    queued = next_block


def handle_results():
    while True:
        n, prime_list = result_queue.get() 
        primes[n] == prime_list
        
        while (handled + 1) in primes:
            handled = handled + 1
        
        while can_test_to(top_number(handled)) >= top_number(queued + 1):
            queue_task(queued + 1)


def put_first_block():
    m = top_number(1) + 1
    primes = calculate_primes_less_than(m)
    result = (m, primes)
    result_queue.put(result)
