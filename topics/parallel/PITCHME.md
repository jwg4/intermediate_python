# Parallel/Async/Multithreading in Python 3

---
We are going to talk about doing lots of things on one machine. NOT about doing lots of things on lots of machines (or one thing on lots of machines).

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
