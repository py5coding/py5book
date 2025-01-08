# Py5Shape.curve_vertices()

Create a collection of curve vertices.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for curve_vertices()](/images/reference/Py5Shape_curve_vertices_0.png)

</div><div class="example-cell-code">

```python
import numpy as np

def setup():
    py5.size(100, 100, py5.P2D)
    random_curve_vertices = 100 * np.random.rand(25, 2)
    s = py5.create_shape()
    with s.begin_shape():
        s.vertex(py5.width / 2, py5.height / 2)
        s.curve_vertices(random_curve_vertices)
    py5.shape(s)
```

</div></div>

</div>

## Description

Create a collection of curve vertices. The purpose of this method is to provide an alternative to repeatedly calling [](py5shape_curve_vertex) in a loop. For a large number of curve vertices, the performance of `curve_vertices()` will be much faster.

The `coordinates` parameter should be a numpy array with one row for each curve vertex.  There should be two or three columns for 2D or 3D points, respectively.

Drawing 2D curves requires using the `P2D` renderer and drawing 3D curves requires using the `P3D` renderer. When drawing directly with `Py5Shape` objects, curves do not work at all using the default renderer.

This method can only be used within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair.

## Signatures

```python
curve_vertices(
    coordinates: Sequence[Sequence[float]],  # 2D array of curve vertex coordinates with 2 or 3 columns for 2D or 3D points, respectively
    /,
) -> None
```

Updated on January 08, 2025 05:55:58am UTC
