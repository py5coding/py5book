# Py5Graphics.texture_mode()

Sets the coordinate space for texture mapping.

## Description

Sets the coordinate space for texture mapping. The default mode is `IMAGE`, which refers to the actual pixel coordinates of the image. `NORMAL` refers to a normalized space of values ranging from 0 to 1. This function only works with the `P2D` and `P3D` renderers.

With `IMAGE`, if an image is 100 x 200 pixels, mapping the image onto the entire size of a quad would require the points (0,0) (100,0) (100,200) (0,200). The same mapping in `NORMAL` is (0,0) (1,0) (1,1) (0,1).

This method is the same as [](sketch_texture_mode) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_texture_mode).

Underlying Processing method: PGraphics.textureMode

## Signatures

```python
texture_mode(
    mode: int,  # either IMAGE or NORMAL
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
