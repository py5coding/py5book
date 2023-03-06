# load_shader()

Loads a shader into a `Py5Shader` object.

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

Loads a shader into a `Py5Shader` object. The shader file must be located in the Sketch's "data" directory to load correctly. Shaders are compatible with the `P2D` and `P3D` renderers, but not with the default renderer.

Alternatively, the file maybe be loaded from anywhere on the local computer using an absolute path (something that starts with / on Unix and Linux, or a drive letter on Windows), or the filename parameter can be a URL for a file found on a network.

If the file is not available or an error occurs, `None` will be returned and an error message will be printed to the console. The error message does not halt the program, however the `None` value may cause an error if your code does not check whether the value returned is `None`.

Underlying Processing method: [loadShader](https://processing.org/reference/loadShader_.html)

## Signatures

```python
load_shader(
    frag_filename: str,  # name of fragment shader file
    /,
) -> Py5Shader

load_shader(
    frag_filename: str,  # name of fragment shader file
    vert_filename: str,  # name of vertex shader file
    /,
) -> Py5Shader
```

Updated on March 06, 2023 02:49:26am UTC
