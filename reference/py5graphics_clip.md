# Py5Graphics.clip()

Limits the rendering to the boundaries of a rectangle defined by the parameters.

## Description

Limits the rendering to the boundaries of a rectangle defined by the parameters. The boundaries are drawn based on the state of the [](py5graphics_image_mode) fuction, either `CORNER`, `CORNERS`, or `CENTER`.

This method is the same as [](sketch_clip) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_clip).

Underlying Processing method: PGraphics.clip

## Signatures

```python
clip(
    a: float,  # x-coordinate of the rectangle, by default
    b: float,  # y-coordinate of the rectangle, by default
    c: float,  # width of the rectangle, by default
    d: float,  # height of the rectangle, by default
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
