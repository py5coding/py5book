# Py5Shape.depth

Get the `Py5Shape` object's depth.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for depth](/images/reference/Py5Shape_depth_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.sphere_detail(8)
    s1 = py5.create_shape(py5.SPHERE, 40)
    z_values = [s1.get_vertex_z(i) for i in range(s1.get_vertex_count())]
    py5.shape(s1, 50, 50)
    py5.println(s1.depth, min(z_values), max(z_values))  # 80, -40, 40
```

</div></div>

</div>

## Description

Get the `Py5Shape` object's depth. This property only makes sense when using the `P3D` renderer. The value will be equal to 0 when using default renderer.

Underlying Processing field: PShape.depth

Updated on October 06, 2023 14:17:50pm UTC
