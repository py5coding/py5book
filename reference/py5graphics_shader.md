# Py5Graphics.shader()

Applies the shader specified by the parameters.

## Description

Applies the shader specified by the parameters. It's compatible with the `P2D` and `P3D` renderers, but not with the default renderer.

This method is the same as [](sketch_shader) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_shader).

Underlying Processing method: PGraphics.shader

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
