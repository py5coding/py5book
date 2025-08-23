# exp()

Returns Euler's number e (2.71828...) raised to the power of the `n` parameter.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    v1 = py5.exp(1.0)
    py5.println(v1)  # Prints "2.718281828459045"
```

</div></div>

</div>

## Description

Returns Euler's number e (2.71828...) raised to the power of the `n` parameter. This function is the compliment to [](sketch_log).

This function makes a call to the numpy `exp()` function.

## Signatures

```python
exp(
    value: Union[float, npt.ArrayLike],  # exponent to raise
) -> Union[float, npt.NDArray]
```

Updated on August 23, 2025 19:59:53pm UTC
