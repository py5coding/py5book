# screen_x()

Takes a three-dimensional X, Y, Z position and returns the X value for where it will appear on a (two-dimensional) screen.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)


def draw():
    py5.background(204)

    x = py5.mouse_x
    y = py5.mouse_y
    z = -100

    # draw "X" at z = -100
    py5.stroke(255)
    py5.line(x-10, y-10, z, x+10, y+10, z)
    py5.line(x+10, y-10, z, x-10, y+10, z)

    # draw gray line at z = 0 and same
    # x value. notice the parallax
    py5.stroke(102)
    py5.line(x, 0, 0, x, py5.height, 0)

    # draw black line at z = 0 to match
    # the x value element drawn at z = -100
    py5.stroke(0)
    the_x = py5.screen_x(x, y, z)
    py5.line(the_x, 0, 0, the_x, py5.height, 0)
```

</div></div>

</div>

## Description

Takes a three-dimensional X, Y, Z position and returns the X value for where it will appear on a (two-dimensional) screen.

Underlying Processing method: [screenX](https://processing.org/reference/screenX_.html)

## Signatures

```python
screen_x(
    x: float,  # 3D x-coordinate to be mapped
    y: float,  # 3D y-coordinate to be mapped
    /,
) -> float

screen_x(
    x: float,  # 3D x-coordinate to be mapped
    y: float,  # 3D y-coordinate to be mapped
    z: float,  # 3D z-coordinate to be mapped
    /,
) -> float
```

Updated on March 06, 2023 02:49:26am UTC
