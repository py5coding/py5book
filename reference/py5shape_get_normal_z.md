# Py5Shape.get_normal_z()

Get the normal vector's z value for one of a `Py5Shape` object's vertices.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_normal_z()](/images/reference/Py5Shape_get_normal_z_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.background(0)
    py5.directional_light(255, 255, 255, -1, -1, -1)

    py5.sphere_detail(5)
    s1 = py5.create_shape(py5.SPHERE, 30)

    for i in range(s1.get_vertex_count()):
        py5.println(s1.get_normal_x(i), s1.get_normal_y(i), s1.get_normal_z(i))

    py5.shape(s1, 50, 50)
```

</div></div>

</div>

## Description

Get the normal vector's z value for one of a `Py5Shape` object's vertices. A normal vector is used for drawing three dimensional shapes and surfaces, and specifies a vector perpendicular to a shape's surface which, in turn, determines how lighting affects it. Py5 attempts to automatically assign normals to shapes, and this method can be used to inspect that vector.

This method can only be used for a complete `Py5Shape` object, and never within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair.

Underlying Processing method: PShape.getNormalZ

## Signatures

```python
get_normal_z(
    index: int,  # vertex index
    /,
) -> float
```

Updated on March 06, 2023 02:49:26am UTC
