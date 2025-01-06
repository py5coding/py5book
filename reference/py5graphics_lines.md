# Py5Graphics.lines()

Draw a collection of lines to the Py5Graphics drawing surface.

## Description

Draw a collection of lines to the Py5Graphics drawing surface. The purpose of this method is to provide an alternative to repeatedly calling [](py5graphics_line) in a loop. For a large number of lines, the performance of `lines()` will be much faster.

The `coordinates` parameter should be a numpy array with one row for each line. The first few columns are for the first point of each line and the next few columns are for the second point of each line. There will be four or six columns for 2D or 3D points, respectively.

This method is the same as [](sketch_lines) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_lines).

## Signatures

```python
lines(
    coordinates: Iterator[Iterator[float]],  # 2D array of line coordinates with 4 or 6 columns for 2D or 3D points, respectively
    /,
) -> None
```

Updated on January 06, 2025 22:21:18pm UTC
