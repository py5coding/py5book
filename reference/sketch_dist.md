# dist()

Calculates the distance between two points.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
# Sets the background gray value based on the distance 
# of the mouse from the center of the screen
def draw():
  py5.no_stroke()
  d = py5.dist(py5.width/2, py5.height/2, py5.mouse_x, py5.mouse_y)
  max_dist = py5.dist(0, 0, py5.width/2, py5.height/2)
  gray = py5.remap(d, 0, max_dist, 0, 255)
  py5.fill(gray)
  py5.rect(0, 0, py5.width, py5.height)
```

</div></div>

</div>

## Description

Calculates the distance between two points.

## Signatures

```python
dist(
    x1: Union[float, npt.NDArray],  # x-coordinate of the first point
    y1: Union[float, npt.NDArray],  # y-coordinate of the first point
    x2: Union[float, npt.NDArray],  # x-coordinate of the second point
    y2: Union[float, npt.NDArray],  # y-coordinate of the second point
    /,
) -> Union[float, npt.NDArray]

dist(
    x1: Union[float, npt.NDArray],  # x-coordinate of the first point
    y1: Union[float, npt.NDArray],  # y-coordinate of the first point
    z1: Union[float, npt.NDArray],  # z-coordinate of the first point
    x2: Union[float, npt.NDArray],  # x-coordinate of the second point
    y2: Union[float, npt.NDArray],  # y-coordinate of the second point
    z2: Union[float, npt.NDArray],  # z-coordinate of the second point
    /,
) -> Union[float, npt.NDArray]
```

Updated on March 06, 2023 02:49:26am UTC
