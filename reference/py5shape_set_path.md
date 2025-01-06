# Py5Shape.set_path()

Set many vertex points at the same time, using a numpy array.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for set_path()](/images/reference/Py5Shape_set_path_0.png)

</div><div class="example-cell-code">

```python
import numpy as np

def setup():
    vertices = 100 * np.random.rand(25, 2)
    s = py5.create_shape()
    s.begin_shape()
    s.no_fill()
    s.vertices(vertices)
    s.end_shape()

    new_vertices = 100 * np.random.rand(25, 2)
    s.set_path(new_vertices.shape[0], new_vertices)

    py5.shape(s)
```

</div></div>

</div>

## Description

Set many vertex points at the same time, using a numpy array. This will be faster and more efficient than repeatedly calling [](py5shape_set_vertex) in a loop. Setting the vertex codes is not supported, so the vertices will be regular vertices and not bezier, quadratic or curve vertices.

The `vcount` parameter cannot be larger than the first dimension of the `verts` array.

Underlying Processing method: PShape.setPath

## Signatures

```python
set_path(
    vcount: int,  # number of vertices
    verts: Iterator[Iterator[float]],  # 2D array of vertex coordinates
    /,
) -> None
```

Updated on January 06, 2025 22:21:18pm UTC
