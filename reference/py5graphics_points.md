# Py5Graphics.points()

Draw a collection of points, each a coordinate in space at the dimension of one pixel.

## Description

Draw a collection of points, each a coordinate in space at the dimension of one pixel. The purpose of this method is to provide an alternative to repeatedly calling [](py5graphics_point) in a loop. For a large number of points, the performance of `points()` will be much faster.

The `coordinates` parameter should be a numpy array with one row for each point. There should be two or three columns for 2D or 3D points, respectively.

This method is the same as [](sketch_points) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_points).

Underlying Processing method: PGraphics.points

## Signatures

```python
points(
    coordinates: npt.NDArray[np.floating],  # 2D array of point coordinates with 2 or 3 columns for 2D or 3D points, respectively
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
