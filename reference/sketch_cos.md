# cos()

Calculates the cosine of an angle.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for cos()](/images/reference/Sketch_cos_0.png)

</div><div class="example-cell-code">

```python
def setup():
    a = 0
    for i in range(25):
        py5.line(4*i, 50, 4*i, 50+40*py5.cos(a))
        a += py5.TWO_PI/25
```

</div></div>

</div>

## Description

Calculates the cosine of an angle. This function expects the values of the angle parameter to be provided in radians (values from `0` to `TWO_PI`). Values are returned in the range -1 to 1.

This function makes a call to the numpy `cos()` function.

## Signatures

```python
cos(
    angle: Union[float, npt.ArrayLike],  # angle in radians
) -> Union[float, npt.NDArray]
```

Updated on August 23, 2025 19:59:53pm UTC
