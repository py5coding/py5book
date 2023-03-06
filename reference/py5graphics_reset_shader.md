# Py5Graphics.reset_shader()

Restores the default shaders.

## Description

Restores the default shaders. Code that runs after `reset_shader()` will not be affected by previously defined shaders.

This method is the same as [](sketch_reset_shader) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_reset_shader).

Underlying Processing method: PGraphics.resetShader

## Signatures

```python
reset_shader() -> None

reset_shader(
    kind: int,  # type of shader, either POINTS, LINES, or TRIANGLES
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
