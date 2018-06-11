# Parallel/Async/Multithreading in Python 3

---
We are going to talk about doing lots of things on one machine. NOT about doing lots of things on lots of machines (or one thing on lots of machines).

---
## Multiprocessing
This is a good approach if it works for you and you don't want to get embroiled in complexity.

We can just run lots of different processes. For example several different Python scripts,
or several copies of the same one. They can run on different CPU cores, at the same time. If one
process is waiting for something, the others will continue as normal.

They don't share any RAM and have to co-ordinate using the filesystem. If waiting for the filesystem
takes too long, this won't work.

The Global Interpreter Lock is not a problem for separate Python processes.

---
## Multithreading
You start different threads in one Python script. These are processes from the CPU's point of view,
but all the same process from the RAM's point of view. So different threads can run at the same time
on different cores, but can all access the same piece of memory.

Unlike having multiple processes, multiple threads can all access the same Python object. This means
you have to use objects which are thread-safe. Threads can't choose when they are going to be pre-empted.
So an object has to work ok if half of a method is run on it, then another method or the same method starts
to run on it. Or they can have critical blocks, where they can't be interrupted. Putting critical blocks
around all your methods would be annoying.

The Global Interpreter Lock means that two threads can't run Python code on different cores at the same
time. Why not? Because Python has a global namespace which both processes can edit.

This is ok if:
1. Most of your time is spent in C or C++ code.
2. Most of your time is spent waiting for I/O.

In the second case, you might not need threads. An asynchronous approach could be enough.

(In the first case, you maybe don't need Python threads.)

---
## Thread-safe objects

Lots of built-in Python code uses C code. Functions are not designed to be pre-emptive, especially modifying objects.

Need special versions of everything - or to isolate objects on threads.

---
## Locking and queuing

- Some shared data is necessary for control (otherwise use processes).
- Locks restrict access to something by more than one thread.
- Queues guarantee that items will only be retrieved once.

---?title=Basic Lock example
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

---?code=topics/parallel/primes/basic_block.py&lang=python

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
 - When the call does return, how do you pause the thing you're now doing?

---
## 'Green' threads
The OS only sees one thread. But on that thread we do one thing, then clear the stack
and start doing something else. We save the context we were doing the first thing in,
so that we can switch back to it.

Blocking I/O means that the process will block while waiting for I/O. If we have green
threads and only one OS-level process, all activity on that process will pause (but other
processes, at the OS level, will run). So we have to use nonblocking IO.

We can combine nonblocking I/O with an event loop to have async I/O.

---
## Structuring async code
 - Coroutines - explicitly switch to another 'fake thread'
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
@[12-16]

---
## Twisted uses yield to pass control around

---?code=topics/parallel/pubsub.py&lang=python
@[6-9]
@[15-22]
@[25-38]
@[41-44]

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
