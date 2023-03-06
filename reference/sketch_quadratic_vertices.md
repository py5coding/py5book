# quadratic_vertices()

Create a collection of quadratic vertices.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for quadratic_vertices()](/images/reference/Sketch_quadratic_vertices_0.png)

</div><div class="example-cell-code">

```python
import numpy as np

def setup():
    random_quadratic_vertices = 100 * np.random.rand(25, 4)
    py5.begin_shape()
    py5.vertex(py5.width / 2, py5.height / 2)
    py5.quadratic_vertices(random_quadratic_vertices)
    py5.end_shape()
```

</div></div>

</div>

## Description

Create a collection of quadratic vertices. The purpose of this method is to provide an alternative to repeatedly calling [](sketch_quadratic_vertex) in a loop. For a large number of quadratic vertices, the performance of `quadratic_vertices()` will be much faster.

The `coordinates` parameter should be a numpy array with one row for each quadratic vertex. The first few columns are for the control point and the next few columns are for the anchor point. There should be four or six columns for 2D or 3D points, respectively.

Underlying Processing method: quadraticVertices

## Signatures

```python
quadratic_vertices(
    coordinates: npt.NDArray[np.floating],  # 2D array of quadratic vertex coordinates with 4 or 6 columns for 2D or 3D points, respectively
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
