from multiprocessing import Process, Queue

from primes import calculate_primes_less_than, calculate_primes_between
from primes import can_test_to, need_to_test
from basic_block import BasicBlock as block_counter

task_queue = Queue()
result_queue = Queue()

primes = {}
handled = 0
queued = 1

counter = block_counter(1000)
block_contains = counter.block_contains
top_number = counter.top_number


def queue_task(next_block):
    blocks = [
        primes[i] for i in
        range(1, block_contains(need_to_test(top_number(next_block))) + 1)
    ]
    task = (next_block, blocks)
    task_queue.put(task)


def handle_results(limit):
    global handled
    global queued

    while handled < limit:
        n, prime_list = result_queue.get()
        primes[n] = prime_list

        while (handled + 1) in primes:
            handled = handled + 1

        while (
                can_test_to(top_number(handled)) >=
                top_number(queued + 1)
                and queued < limit):
            next_block = queued + 1
            queue_task(next_block)
            queued = next_block


def put_first_block():
    m = top_number(1) + 1
    primes = calculate_primes_less_than(m)
    result = (1, primes)
    result_queue.put(result)


def task_worker():
    while True:
        n, blocks = task_queue.get()
        l = top_number(n-1) + 1
        m = top_number(n)
        primes = calculate_primes_between(l, m, blocks)
        result = (n, primes)
        result_queue.put(result)


def get_results(primes):
    return [ x for l in sorted(primes.keys()) for x in primes[l] ]


if __name__ == '__main__':
    BLOCK_COUNT = 100
    WORKER_COUNT = 10

    put_first_block()

    workers = [ Process(target=task_worker) for x in range(WORKER_COUNT) ]
    for w in workers:
        w.start()

    handle_results(BLOCK_COUNT)

    for w in workers:
        w.terminate()

    results = get_results(primes)
    print(len(results))
    print(results[-1])
