# Py5Graphics.vertices()

Create a collection of vertices.

## Description

Create a collection of vertices. The purpose of this method is to provide an alternative to repeatedly calling [](py5graphics_vertex) in a loop. For a large number of vertices, the performance of `vertices()` will be much faster.

The `coordinates` parameter should be a numpy array with one row for each vertex. There should be two or three columns for 2D or 3D points, respectively. There may also be an additional two columns for UV texture mapping values.

This method is the same as [](sketch_vertices) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_vertices).

## Signatures

```python
vertices(
    coordinates: Iterator[Iterator[float]],  # 2D array of vertex coordinates and optional UV texture mapping values
    /,
) -> None
```

Updated on January 06, 2025 22:21:18pm UTC
