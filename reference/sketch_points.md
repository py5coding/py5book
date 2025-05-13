# points()

Draw a collection of points, each a coordinate in space at the dimension of one pixel.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for points()](/images/reference/Sketch_points_0.png)

</div><div class="example-cell-code">

```python
import numpy as np

def setup():
    random_points = 100 * np.random.rand(500, 2)
    py5.points(random_points)
```

</div></div>

</div>

## Description

Draw a collection of points, each a coordinate in space at the dimension of one pixel. The purpose of this method is to provide an alternative to repeatedly calling [](sketch_point) in a loop. For a large number of points, the performance of `points()` will be much faster.

The `coordinates` parameter should be a numpy array with one row for each point. There should be two or three columns for 2D or 3D points, respectively.

## Signatures

```python
points(
    coordinates: Sequence[Sequence[float]],  # 2D array of point coordinates with 2 or 3 columns for 2D or 3D points, respectively
    /,
) -> None
```

Updated on January 08, 2025 05:55:58am UTC
