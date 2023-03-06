# norm()

Normalizes a number from another range into a value between 0 and 1.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    value = 20
    n = py5.norm(value, 0, 50)
    py5.println(n)  # Prints "0.4"
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    value = -10
    n = py5.norm(value, 0, 100)
    py5.println(n)  # Prints "-0.1"
```

</div></div>

</div>

## Description

Normalizes a number from another range into a value between 0 and 1. Identical to `remap(value, low, high, 0, 1)`.

Numbers outside of the range are not clamped to 0 and 1, because out-of-range values are often intentional and useful. (See the second example.) If that isn't what you want, try pairing this function with [](sketch_constrain).

## Signatures

```python
norm(
    value: Union[float, npt.NDArray],  # the incoming value to be converted
    start: Union[float, npt.NDArray],  # lower bound of the value's current range
    stop: Union[float, npt.NDArray],  # upper bound of the value's current range
) -> Union[float, npt.NDArray]
```

Updated on March 06, 2023 02:49:26am UTC
