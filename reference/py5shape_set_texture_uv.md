# Py5Shape.set_texture_uv()

Set the uv texture mapping coordinates for a given vertex in a `Py5Shape` object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for set_texture_uv()](/images/reference/Py5Shape_set_texture_uv_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P2D)
    img = py5.load_image("tower.jpg")
    s = py5.create_shape()
    s.begin_shape()
    s.vertex(20, 20)
    s.vertex(20, 80)
    s.vertex(80, 80)
    s.vertex(80, 20)
    s.end_shape(py5.CLOSE)

    s.set_texture(img)
    s.set_texture_mode(py5.NORMAL)
    s.set_texture_uv(0, 0, 0)
    s.set_texture_uv(1, 0, 1)
    s.set_texture_uv(2, 1, 1)
    s.set_texture_uv(3, 1, 0)

    py5.shape(s)
```

</div></div>

</div>

## Description

Set the uv texture mapping coordinates for a given vertex in a `Py5Shape` object. This method can only be used outside the [](py5shape_begin_shape) and [](py5shape_end_shape) methods.

The `u` and `v` coordinates define the mapping of a `Py5Shape` object's texture to the form. By default, the coordinates used for `u` and `v` are specified in relation to the image's size in pixels, but this relation can be changed with the `Py5Shape` object's [](py5shape_set_texture_mode) method.

Underlying Processing method: PShape.setTextureUV

## Signatures

```python
set_texture_uv(
    index: int,  # vertex index
    u: float,  # horizontal coordinate for the texture mapping
    v: float,  # vertical coordinate for the texture mapping
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
