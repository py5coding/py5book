# floor()

Calculates the closest int value that is less than or equal to the value of the parameter.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    x = 2.88
    a = py5.floor(x)  # Sets 'a' to 2
```

</div></div>

</div>

## Description

Calculates the closest int value that is less than or equal to the value of the parameter.

This function makes a call to the numpy `floor()` function.

## Signatures

```python
floor(
    value: Union[float, npt.ArrayLike]  # number to round down
) -> Union[int, npt.NDArray]
```

Updated on March 06, 2023 02:49:26am UTC
