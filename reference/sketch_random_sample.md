# random_sample()

Select random items from a list.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    words = ["apple", "bear", "cat", "dog"]
    word = py5.random_sample(words)
    py5.println(word)  # Prints one of the four words
```

</div></div>

</div>

## Description

Select random items from a list. The list items can be of any type. If multiple items are selected, this function will by default allow the same item to be selected multiple times. Set the `replace` parameter to `False` to prevent the same item from being selected multiple times.

The returned value will always be a sequence such as a list or numpy array, even if only one item is sampled. If you only want to sample one item, consider using [](sketch_random_choice) instead. If the list of objects is empty, an empty list will be returned.

This function's randomness can be influenced by [](sketch_random_seed), and makes calls to numpy to select the random items.

## Signatures

```python
random_sample(
    objects: list[Any],  # list of objects to choose from
    size: int = 1,  # number of random items to select
    replace: bool = True,  # whether to select random items with or without replacement
) -> list[Any]
```

Updated on April 15, 2023 22:56:12pm UTC
