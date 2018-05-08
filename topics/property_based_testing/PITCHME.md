# Property based testing

---

Sometimes specific examples are very powerful.

Sometimes to fully check function behavior with property-based testing would mean re-implementing the function in the test definition.

---

A good strategy is to combine a few explicit examples, where you exactly specify the inputs and outputs, with property-based testing over the whole domain of the function, where you just check that
 - the function does not throw an exception
 - the return values is valid (eg not null or None)
 - some basic condition (like the output is greater than the input)