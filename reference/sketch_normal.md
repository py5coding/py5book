# normal()

Sets the current normal vector.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for normal()](/images/reference/Sketch_normal_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.no_stroke()
    py5.background(0)
    py5.point_light(150, 250, 150, 10, 30, 50)
    py5.begin_shape()
    py5.normal(0, 0, 1)
    py5.vertex(20, 20, -10)
    py5.vertex(80, 20, 10)
    py5.vertex(80, 80, -10)
    py5.vertex(20, 80, 10)
    py5.end_shape(py5.CLOSE)
```

</div></div>

</div>

## Description

Sets the current normal vector. Used for drawing three dimensional shapes and surfaces, `normal()` specifies a vector perpendicular to a shape's surface which, in turn, determines how lighting affects it. Py5 attempts to automatically assign normals to shapes, but since that's imperfect, this is a better option when you want more control. This function is identical to `gl_normal3f()` in OpenGL.

Underlying Processing method: [normal](https://processing.org/reference/normal_.html)

## Signatures

```python
normal(
    nx: float,  # x direction
    ny: float,  # y direction
    nz: float,  # z direction
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
