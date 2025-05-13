# random_choice()

Select a random item from a list.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    words = ["apple", "bear", "cat", "dog"]
    word = py5.random_choice(words)
    py5.println(word)  # Prints one of the four words
```

</div></div>

</div>

## Description

Select a random item from a list. The list items can be of any type. If the list of objects is empty, `None` will be returned.

This function's randomness can be influenced by [](sketch_random_seed), and makes calls to numpy to select the random items.

## Signatures

```python
random_choice(
    seq: Sequence[Any],  # list of objects to choose from
) -> Any
```

Updated on January 28, 2025 16:45:48pm UTC
