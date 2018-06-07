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
 - Promises - monadic
 
---?code=topics/parallel/primes/main.py&lang=python
