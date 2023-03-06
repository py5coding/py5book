# random_seed()

Sets the seed value for py5's random functions.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.random_seed(42)
    a = py5.random()
    py5.random_seed(42)
    b = py5.random()
    # the values a and b will be the same
    py5.println(a, b)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.random_seed(0)
    for i in range(100):
        r = py5.random(255)
        py5.stroke(r)
        py5.line(i, 0, i, 100)
```

</div></div>

</div>

## Description

Sets the seed value for py5's random functions. This includes [](sketch_random), [](sketch_random_int), [](sketch_random_choice), and [](sketch_random_gaussian). By default, all of these functions would produce different results each time a program is run. Set the seed parameter to a constant value to return the same pseudo-random numbers each time the software is run.

## Signatures

```python
random_seed(
    seed: int,  # seed value
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
