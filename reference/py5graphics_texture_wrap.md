# Py5Graphics.texture_wrap()

Defines if textures repeat or draw once within a texture map.

## Description

Defines if textures repeat or draw once within a texture map. The two parameters are `CLAMP` (the default behavior) and `REPEAT`. This function only works with the `P2D` and `P3D` renderers.

This method is the same as [](sketch_texture_wrap) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_texture_wrap).

Underlying Processing method: PGraphics.textureWrap

## Signatures

```python
texture_wrap(
    wrap: int,  # Either CLAMP (default) or REPEAT
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
