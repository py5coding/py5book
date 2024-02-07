# constrain()

Constrains a value between a minimum and maximum value.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def draw():
    py5.background(204)
    mx = py5.constrain(py5.mouse_x, 30, 70)
    py5.rect(mx-10, 40, 20, 20)
```

</div></div>

</div>

## Description

Constrains a value between a minimum and maximum value.

## Signatures

```python
constrain(
    amt: Union[float, npt.NDArray],  # the value to constrain
    low: Union[float, npt.NDArray],  # minimum limit
    high: Union[float, npt.NDArray],  # maximum limit
) -> Union[float, npt.NDArray]
```

Updated on February 07, 2024 03:43:17am UTC
