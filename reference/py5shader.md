# Py5Shader

This class encapsulates a GLSL shader program, including a vertex and a fragment shader.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global blur
    py5.size(640, 360, py5.P2D)
    # shaders files must be in the "data" folder to load correctly
    blur = py5.load_shader("blur.glsl")
    py5.stroke(0, 102, 153)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.apply_filter(blur)
    py5.rect(py5.mouse_x-75, py5.mouse_y, 150, 150)
    py5.ellipse(py5.mouse_x+75, py5.mouse_y, 150, 150)
```

</div></div>

</div>

## Description

This class encapsulates a GLSL shader program, including a vertex and a fragment shader. It's compatible with the `P2D` and `P3D` renderers, but not with the default renderer. Use the [](sketch_load_shader) function to load your shader code and create `Py5Shader` objects.

Underlying Processing class: [PShader](https://processing.org/reference/PShader.html)

The following methods and fields are provided:

```{include} include_py5shader.md
```

Updated on March 06, 2023 02:49:26am UTC
