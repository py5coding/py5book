# Py5Shape.no_tint()

Stop applying a color tint to a shape's texture map.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for no_tint()](/images/reference/Py5Shape_no_tint_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P2D)
    img = py5.load_image("tower.jpg")
    s = py5.create_shape()
    s.begin_shape()
    s.texture(img)
    s.tint(0, 0, 255)
    s.vertex(20, 20, 0, 0)
    s.vertex(20, 80, 0, 100)
    s.no_tint()
    s.vertex(80, 80, 100, 100)
    s.vertex(80, 20, 100, 0)
    s.end_shape(py5.CLOSE)

    py5.shape(s)
```

</div></div>

</div>

## Description

Stop applying a color tint to a shape's texture map. Use [](py5shape_tint) to start applying a color tint.

Both [](py5shape_tint) and `no_tint()` can be used to control the coloring of textures in 3D.

Underlying Processing method: PShape.noTint

## Signatures

```python
no_tint() -> None
```

Updated on March 06, 2023 02:49:26am UTC
