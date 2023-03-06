# constrain()

Constrains a value to not exceed a maximum and minimum value.

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

Constrains a value to not exceed a maximum and minimum value.

## Signatures

```python
constrain(
    amt: Union[float, npt.NDArray],  # the value to constrain
    low: Union[float, npt.NDArray],  # maximum limit
    high: Union[float, npt.NDArray],  # minimum limit
) -> Union[float, npt.NDArray]
```

Updated on March 06, 2023 02:49:26am UTC
