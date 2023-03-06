# reset_shader()

Restores the default shaders.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global edges
    global img
    py5.size(640, 360, py5.P2D)
    img = py5.load_image("leaves.jpg")
    edges = py5.load_shader("edges.glsl")


def draw():
    py5.shader(edges)
    py5.image(img, 0, 0)
    py5.reset_shader()
    py5.image(img, py5.width//2, 0)
```

</div></div>

</div>

## Description

Restores the default shaders. Code that runs after `reset_shader()` will not be affected by previously defined shaders.

Underlying Processing method: [resetShader](https://processing.org/reference/resetShader_.html)

## Signatures

```python
reset_shader() -> None

reset_shader(
    kind: int,  # type of shader, either POINTS, LINES, or TRIANGLES
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
