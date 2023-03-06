# Py5Shape.get_vertex_z()

Get the value of the z coordinate for the vertex `index`.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_vertex_z()](/images/reference/Py5Shape_get_vertex_z_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.sphere_detail(8)
    s1 = py5.create_shape(py5.SPHERE, 40)
    z_values = [s1.get_vertex_z(i) for i in range(s1.get_vertex_count())]
    py5.shape(s1, 50, 50)
    py5.println(s1.get_depth(), min(z_values), max(z_values))  # 80, -40, 40
```

</div></div>

</div>

## Description

Get the value of the z coordinate for the vertex `index`.

Underlying Processing method: PShape.getVertexZ

## Signatures

```python
get_vertex_z(
    index: int,  # vertex index
    /,
) -> float
```

Updated on March 06, 2023 02:49:26am UTC
