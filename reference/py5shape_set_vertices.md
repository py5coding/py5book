# Py5Shape.set_vertices()

The `set_vertices()` method sets the vertex coordinates for all vertices in a `Py5Shape` object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import numpy as np

vertices = np.array([[0, 0], [60, 0], [60, 60], [0, 60]], dtype=np.float64)

def setup():
    global s
    s = py5.create_shape()
    with s.begin_closed_shape():
        s.vertices(vertices)


def draw():
    global vertices
    vertices += np.random.rand(4, 2) * 2 - 1
    s.set_vertices(vertices)

    py5.translate(20, 20)
    py5.shape(s)
```

</div></div>

</div>

## Description

The `set_vertices()` method sets the vertex coordinates for all vertices in a `Py5Shape` object. This method is similar to but much faster than [](py5shape_set_vertex) when used in a `for` loop.

This method can only be used outside the [](py5shape_begin_shape) and [](py5shape_end_shape) methods.

## Signatures

```python
set_vertices(
    coordinates: Sequence[Sequence[float]],  # 2D array of vertex coordinates
    /,
) -> None
```

Updated on October 12, 2026 17:24:20pm UTC
