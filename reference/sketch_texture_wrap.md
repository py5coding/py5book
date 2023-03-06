# texture_wrap()

Defines if textures repeat or draw once within a texture map.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global img
    py5.size(300, 300, py5.P2D)
    img = py5.load_image("berlin-1.jpg")
    py5.texture_mode(py5.NORMAL)


def draw():
    py5.background(0)
    py5.translate(py5.width//2, py5.height//2)
    py5.rotate(py5.remap(py5.mouse_x, 0, py5.width, -py5.PI, py5.PI))
    if py5.is_mouse_pressed:
        py5.texture_wrap(py5.REPEAT)
    else:
        py5.texture_wrap(py5.CLAMP)

    py5.begin_shape()
    py5.texture(img)
    py5.vertex(-100, -100, 0, 0)
    py5.vertex(100, -100, 2, 0)
    py5.vertex(100, 100, 2, 2)
    py5.vertex(-100, 100, 0, 2)
    py5.end_shape()
```

</div></div>

</div>

## Description

Defines if textures repeat or draw once within a texture map. The two parameters are `CLAMP` (the default behavior) and `REPEAT`. This function only works with the `P2D` and `P3D` renderers.

Underlying Processing method: [textureWrap](https://processing.org/reference/textureWrap_.html)

## Signatures

```python
texture_wrap(
    wrap: int,  # Either CLAMP (default) or REPEAT
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
