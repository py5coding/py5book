# Py5Graphics.texture()

Sets a texture to be applied to vertex points.

## Description

Sets a texture to be applied to vertex points. The `texture()` method must be called between [](py5graphics_begin_shape) and [](py5graphics_end_shape) and before any calls to [](py5graphics_vertex). This method only works with the `P2D` and `P3D` renderers.

When textures are in use, the fill color is ignored. Instead, use [](py5graphics_tint) to specify the color of the texture as it is applied to the shape.

This method is the same as [](sketch_texture) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_texture).

Underlying Processing method: PGraphics.texture

## Signatures

```python
texture(
    image: Py5Image,  # reference to a Py5Image object
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
