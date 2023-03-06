# asin()

The inverse of [](sketch_sin), returns the arc sine of a value.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    a = py5.PI/3
    s = py5.sin(a)
    a_s = py5.asin(s)
    # prints "1.04719757 : 0.86602541 : 1.04719757"
    py5.println(round(a, 8), ':', round(s, 8), ':', round(a_s, 8))
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    a = py5.PI + py5.PI/3
    s = py5.sin(a)
    a_s = py5.asin(s)
    # prints "4.18879027 : -0.86602543 : -1.04719761"
    py5.println(round(a, 8), ':', round(s, 8), ':', round(a_s, 8))
```

</div></div>

</div>

## Description

The inverse of [](sketch_sin), returns the arc sine of a value. This function expects the values in the range of -1 to 1 and values are returned in the range `-HALF_PI` to `HALF_PI`.

This function makes a call to the numpy `asin()` function.

## Signatures

```python
asin(
    value: Union[float, npt.ArrayLike]  # value in the range of -1 to 1 whose arc sine is to be returned
) -> Union[float, npt.NDArray]
```

Updated on March 06, 2023 02:49:26am UTC
