# degrees()

Converts a radian measurement to its corresponding value in degrees.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    rad = py5.PI/4
    deg = py5.degrees(rad)
    # prints "0.7854 radians is 45.0 degrees"
    py5.println(round(rad, 5), 'radians is', round(deg, 5), 'degrees')
```

</div></div>

</div>

## Description

Converts a radian measurement to its corresponding value in degrees. Radians and degrees are two ways of measuring the same thing. There are 360 degrees in a circle and `2*PI` radians in a circle. For example, `90° = PI/2 = 1.5707964`. All trigonometric functions in py5 require their parameters to be specified in radians.

This function makes a call to the numpy `degrees()` function.

## Signatures

```python
degrees(
    radians: Union[float, npt.ArrayLike]  # radian value to convert to degrees
) -> Union[float, npt.NDArray]
```

Updated on March 06, 2023 02:49:26am UTC
