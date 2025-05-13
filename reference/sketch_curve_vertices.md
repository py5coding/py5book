# curve_vertices()

Create a collection of curve vertices.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for curve_vertices()](/images/reference/Sketch_curve_vertices_0.png)

</div><div class="example-cell-code">

```python
import numpy as np

def setup():
    random_curve_vertices = 100 * np.random.rand(25, 2)
    with py5.begin_shape():
        py5.vertex(py5.width / 2, py5.height / 2)
        py5.curve_vertices(random_curve_vertices)
```

</div></div>

</div>

## Description

Create a collection of curve vertices. The purpose of this method is to provide an alternative to repeatedly calling [](sketch_curve_vertex) in a loop. For a large number of curve vertices, the performance of `curve_vertices()` will be much faster.

The `coordinates` parameter should be a numpy array with one row for each curve vertex.  There should be two or three columns for 2D or 3D points, respectively.

## Signatures

```python
curve_vertices(
    coordinates: Sequence[Sequence[float]],  # 2D array of curve vertex coordinates with 2 or 3 columns for 2D or 3D points, respectively
    /,
) -> None
```

Updated on January 08, 2025 05:55:58am UTC
