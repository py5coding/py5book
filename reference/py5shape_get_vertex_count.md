# Py5Shape.get_vertex_count()

The `get_vertex_count()` method returns the number of vertices that make up a `Py5Shape`.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global s
    s = py5.create_shape()
    s.begin_shape()
    s.vertex(0, 0)
    s.vertex(60, 0)
    s.vertex(60, 60)
    s.vertex(0, 60)
    s.end_shape(py5.CLOSE)


def draw():
    py5.translate(20, 20)
    for i in range(0, s.get_vertex_count()):
        v = s.get_vertex(i)
        v[0] += py5.random(-1, 1)
        v[1] += py5.random(-1, 1)
        s.set_vertex(i, v)

    py5.shape(s)
```

</div></div>

</div>

## Description

The `get_vertex_count()` method returns the number of vertices that make up a `Py5Shape`. In the example, the value 4 is returned by the `get_vertex_count()` method because 4 vertices are defined in `setup()`.

Use the `include_children` parameter to include the shape's children if the shape happens to be a `GROUP` shape. By default, a shape's children will not be included in the count.

Underlying Processing method: [PShape.getVertexCount](https://processing.org/reference/PShape_getVertexCount_.html)

## Signatures

```python
get_vertex_count() -> int

get_vertex_count(
    include_children: bool,  # include vertices in the shape's children
    /,
) -> int
```

Updated on April 18, 2025 05:23:11am UTC
