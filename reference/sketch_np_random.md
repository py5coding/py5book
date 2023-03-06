# np_random

Access the numpy random number generator that py5 uses to provide random number functionality.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    words = ["apple", "bear", "cat", "dog"]
    py5.np_random.shuffle(words)
    # Prints the words in a random order
    for word in words:
        py5.println(word)
```

</div></div>

</div>

## Description

Access the numpy random number generator that py5 uses to provide random number functionality. Py5 uses a numpy random number generator to provide a breadth of random number functions such as [](sketch_random_choice), [](sketch_random_gaussian), and [](sketch_random_int). The functions py5 provides are the ones you are most likely to need, but numpy is capable of much more than what py5 makes available. Access this property to access all of numpy's random number functions.

All of the random numbers generated through this property can be influenced by [](sketch_random_seed).

Updated on March 06, 2023 02:49:26am UTC
