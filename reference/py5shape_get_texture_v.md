# Py5Shape.get_texture_v()

Get the vertical texture mapping coordinate for a particular vertex.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_texture_v()](/images/reference/Py5Shape_get_texture_v_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P2D)
    img = py5.load_image("tower.jpg")
    s = py5.create_shape()
    s.begin_shape()
    s.texture(img)
    s.vertex(20, 20, 0, 0)
    s.vertex(20, 80, 0, 100)
    s.vertex(80, 80, 100, 100)
    s.vertex(80, 20, 100, 0)
    s.end_shape(py5.CLOSE)

    py5.shape(s)

    for i in range(s.get_vertex_count()):
        u = s.get_texture_u(i)
        v = s.get_texture_v(i)
        py5.println(f"vertex {i}: u = {u} v = {v}")
```

</div></div>

</div>

## Description

Get the vertical texture mapping coordinate for a particular vertex. Returned values will always range from 0 to 1, regardless of what the Sketch's [](sketch_texture_mode) setting is.

Underlying Processing method: PShape.getTextureV

## Signatures

```python
get_texture_v(
    index: int,  # vertex index
    /,
) -> float
```

Updated on March 06, 2023 02:49:26am UTC
