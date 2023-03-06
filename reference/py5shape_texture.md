# Py5Shape.texture()

Sets a texture to be applied to a `Py5Shape` object's vertex points.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for texture()](/images/reference/Py5Shape_texture_0.png)

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
```

</div></div>

</div>

## Description

Sets a texture to be applied to a `Py5Shape` object's vertex points. The `texture()` function must be called between [](py5shape_begin_shape) and [](py5shape_end_shape) and before any calls to [](py5shape_vertex). This method only works with the `P2D` and `P3D` renderers.

When textures are in use, the fill color is ignored. Instead, use [](py5shape_tint) to specify the color of the texture as it is applied to the shape.

Underlying Processing method: PShape.texture

## Signatures

```python
texture(
    tex: Py5Image,  # reference to a Py5Image object
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
