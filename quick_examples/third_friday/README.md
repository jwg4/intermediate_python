# Third Friday of the month

The goal here is to write a piece of code which calculates the third Friday of a given month. For example, 6th April 2018 was a Friday, the first one of the month, Friday April 13th was the second Friday of the month, and Friday April 20th was the third Friday of that month.

Inputs:
 - `year` (an integer)
 - `month` (an integer).

Outputs:
 - A `datetime.date` object, which represents the third Friday of that month. It would also be acceptable to return just an integer, eg 17 to mean the 17th day of that month. However, we are probably going to want to use the `datetime.date` class and its functions for manipulating dates in this exercise, so probably we are happy to return an instance of this class.

Resources:
 - https://docs.python.org/3.5/library/datetime.html#datetime.date shows how you construct an element of the `date` class.
 - https://docs.python.org/3.5/library/datetime.html#datetime.date.weekday Find what day of the week a date is.
