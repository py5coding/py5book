# Py5Shape.vertices()

Create a collection of vertices.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for vertices()](/images/reference/Py5Shape_vertices_0.png)

</div><div class="example-cell-code">

```python
import numpy as np

def setup():
    random_triangle_vertices = 100 * np.random.rand(25, 2)
    s = py5.create_shape()
    with s.begin_shape(s.TRIANGLES):
        s.vertices(random_triangle_vertices)
    py5.shape(s)
```

</div></div>

</div>

## Description

Create a collection of vertices. The purpose of this method is to provide an alternative to repeatedly calling [](py5shape_vertex) in a loop. For a large number of vertices, the performance of `vertices()` will be much faster.

The `coordinates` parameter should be a numpy array with one row for each vertex. There should be two or three columns for 2D or 3D points, respectively. There may also be an additional two columns for UV texture mapping values.

## Signatures

```python
vertices(
    coordinates: Sequence[Sequence[float]],  # 2D array of vertex coordinates and optional UV texture mapping values
    /,
) -> None
```

Updated on January 08, 2025 05:55:58am UTC
