# atan()

The inverse of [](sketch_tan), returns the arc tangent of a value.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    a = py5.PI/3
    t = py5.tan(a)
    a_t = py5.atan(t)
    # prints "1.04719757 : 1.73205087 : 1.04719757"
    py5.println(round(a, 8), ':', round(t, 8), ':', round(a_t, 8))
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    a = py5.PI + py5.PI/3
    t = py5.tan(a)
    a_t = py5.atan(t)
    # prints "4.18879027 : 1.73205106 : 1.04719761"
    py5.println(round(a, 8), ':', round(t, 8), ':', round(a_t, 8))
```

</div></div>

</div>

## Description

The inverse of [](sketch_tan), returns the arc tangent of a value. This function expects the values in the range of -Infinity to Infinity and values are returned in the range `-HALF_PI` to `HALF_PI`.

This function makes a call to the numpy `atan()` function.

## Signatures

```python
atan(
    value: Union[float, npt.ArrayLike],  # value whose arc tangent is to be returned
) -> Union[float, npt.NDArray]
```

Updated on August 23, 2025 19:59:53pm UTC
