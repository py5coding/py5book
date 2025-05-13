# random_permutation()

Generates a random permutation for the given sequence.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    words = ["apple", "bear", "cat", "dog"]
    perm = py5.random_permutation(words)
    py5.println(perm)  # Prints one of the permutation of words.
```

</div></div>

</div>

## Description

Generates a random permutation for the given sequence. Each time the `random_permutation()` method is called, it generates and return a random permuted sequence of the given sequence.

The returned value will always be a sequence such as a list. If the provided sequence is empty, an empty list will be returned.

This function's randomness can be influenced by [](sketch_random_seed), and makes calls to numpy to select the random permutation.

## Signatures

```python
random_permutation(
    seq: Sequence[Any],  # sequence of objects for which random permutation is required
) -> Sequence[Any]
```

Updated on January 28, 2025 16:45:48pm UTC
