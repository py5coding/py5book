# ceil()

Calculates the closest int value that is greater than or equal to the value of the parameter.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    x = 2.88
    a = py5.ceil(x)  # Sets 'a' to 3
```

</div></div>

</div>

## Description

Calculates the closest int value that is greater than or equal to the value of the parameter.

This function makes a call to the numpy `ceil()` function.

## Signatures

```python
ceil(
    value: Union[float, npt.ArrayLike],  # number to round up
) -> Union[int, npt.NDArray]
```

Updated on August 23, 2025 19:59:53pm UTC
