# shader()

Applies the shader specified by the parameters.

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
```

</div></div>

</div>

## Description

Applies the shader specified by the parameters. It's compatible with the `P2D` and `P3D` renderers, but not with the default renderer.

Underlying Processing method: [shader](https://processing.org/reference/shader_.html)

## Signatures

```python
shader(
    shader: Py5Shader,  # name of shader file
    /,
) -> None

shader(
    shader: Py5Shader,  # name of shader file
    kind: int,  # type of shader, either POINTS, LINES, or TRIANGLES
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
