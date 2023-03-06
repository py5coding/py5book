# tan()

Calculates the ratio of the sine and cosine of an angle.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for tan()](/images/reference/Sketch_tan_0.png)

</div><div class="example-cell-code">

```python
def setup():
    a = 0
    for i in range(50):
        py5.line(2*i, 50, 2*i, 50+2*py5.tan(a))
        a += py5.TWO_PI/50
```

</div></div>

</div>

## Description

Calculates the ratio of the sine and cosine of an angle. This function expects the values of the angle parameter to be provided in radians (values from `0` to `TWO_PI`). Values are returned in the range infinity to -infinity.

This function makes a call to the numpy `tan()` function.

## Signatures

```python
tan(
    angle: Union[float, npt.ArrayLike]  # angle in radians
) -> Union[float, npt.NDArray]
```

Updated on March 06, 2023 02:49:26am UTC
