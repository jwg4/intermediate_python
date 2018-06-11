# Parallel/Async/Multithreading in Python 3

---
We are going to talk about doing lots of things on one machine. NOT about doing lots of things on lots of machines (or one thing on lots of machines).

---
## Three topics
(In ascending order of how confusing they are.)
 1. Multiprocessing
 2. Multithreading
 3. Async

---
## Multiprocessing
 - We can just run lots of different processes. 
 - several different Python scripts or several copies of the same one.
 - Run on different CPU cores, at the same time.
 - if one process is waiting for something, the others continue.

 - Don't share any RAM.
 - Have to co-ordinate eg. using the filesystem.

---
## Multiprocessing works if:
 - You don't want to deal with threads or async.
 - You manage coordination somewhere else.
 - Or hardly any coordination.
 - All the time is taken in Python code.
 - You don't max out filesystem or network resources.
 - (You want to scale to other machines.)

---
## Multithreading
 - You start different threads in one Python script.
 - Separate from the CPU's point of view,
 - All the same process from the RAM's point of view.
 - Different threads can run at the same time on different cores.
 - All access the same piece of memory.

---
## Multithreading vs. multiprocessing
 - All threads can access the same Python objects.
 - Objects have to be thread-safe.
 - Can't run Python code on two CPUs at once.
 
---
## Threading works if:
1. Most of your time is spent in C or C++ code.
2. Most of your time is spent waiting for I/O.

In the second case, you might not need threads. An asynchronous approach could be enough.

(In the first case, you maybe don't need Python threads.)

---
## The Global Interpreter Lock
 - Python interpretation is not thread-safe.
 - Lots of things have global state.
 - We can run Python with multiple threads.
 - Can't run Python code on both threads.

---
## Thread-safe objects

Lots of built-in Python code uses C code. Functions are not designed to be pre-emptive, especially modifying objects.

Need special versions of everything - or to isolate objects on threads. The special versions use locks or low-level control like critical sections.

---
## Locking and queuing

- Some shared data is necessary for control (otherwise use processes).
- Locks restrict access by more than one thread.
- Queues guarantee items are only retrieved once.

---
## Basic Lock example
```[python]
count = 0
lock = threading.Lock()

def incre():
    global count 
    lock.acquire()
    try:
        count += 1    
    finally:
        lock.release()
```

---?code=topics/parallel/primes/basic_block.py&lang=python&title=More complex Queue example

---?code=topics/parallel/primes/primes.py&lang=python
@[4-10]
@[13-19]

---?code=topics/parallel/primes/main.py&lang=python
@[7-12]
@[67-70]
@[45-49]
@[72-76]
@[52-59]
@[28-34]
@[36-42]
@[78-83]


---
## What is async?
 - When you make an IO call, you do something else while waiting for the call to return.
 - Ideal for database calls, HTTP requests.
 - Commonly used in JavaScript.
 - Important for application servers.
 - Typically using an event queue.
 
---
## Three elements
 - Give up execution instead of blocking
 - Choose what to run next.
 - Decide when to carry on executing the paused thing.

---
## Can't work with normal I/O
 - only one OS thread.
 - if blocking IO is used, the whole thread blocks.
 - need async-aware I/O libraries.

---
## Structuring async code
 - Coroutines - explicitly switch to another 'thread'
 - Event driven - events add something to the queue
 - Callbacks - pass the next function to the async one
 - Promises/futures - monadic

--- 
## Generators and yield
The first way Python did 'context switching' was with the 'yield' keyword.
This allows us to create 'lazy iterables'.
These are data structures where, whenever we try to retrieve some values, some will be available.
They could already by present in a list, or some could be generated each time.

---?code=topics/parallel/infinite.py&lang=python

---
## Yield and send
Generators became useful for switching in and out of functions. So 'send' keyword was added.
You can 'send' a value into a function, and have it 'yield' back a value, while the context is saved.

---?code=topics/parallel/send.py&lang=python
@[1-8]
@[10-16]

---
## Twisted uses yield to pass control around

---?code=topics/parallel/pubsub.py&lang=python
@[6-9]
@[15-22]
@[25-38]
@[41-44]


---
## 'Green' threads
 - The OS only sees one thread.
 - 'coroutines'
 - Save whole stack, and switch context.
 - When switching back, restore whole stack.
 - Still relies on giving up execution.
 - `gevent` and `eventlet` implementations include an event loop.
 
---
## Gevent - coroutines not generators
---?code=topics/parallel/gevent_basic.py&lang=python
@[2]
@[4-12]
@[14-17]

---?code=topics/parallel/gevent_select.py&lang=python
@[1-6]
@[8-18]
@[20-28]

---
## Futures - something you haven't done yet is a 'thing'
---?code=topics/parallel/futures.py&lang=python
@[2-9]
@[11-21]

---
## The modern approach
 - asyncio in Python 3.4
 - asyncio-compatible libraries such as aiohttp
 - `await` and `async` keywords in Python 3.5
 - Easy to wrap an async function with user code.

---
## Await, async, asyncio, aiohttp
---?code=topics/parallel/reddit.py&lang=python
@[4-9]
@[28-33]
@[11-14]
@[16-26]
@[35-38]

---
## Thanks
 - Jack Grahl
 - twitter.com/jackgrahl
 - github.com/jwg4
 - My job: PrismFP Analytics
 - Thanks to Robert for FSQ
