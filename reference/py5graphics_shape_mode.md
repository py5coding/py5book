# Py5Graphics.shape_mode()

Modifies the location from which shapes draw.

## Description

Modifies the location from which shapes draw. The default mode is `shape_mode(CORNER)`, which specifies the location to be the upper left corner of the shape and uses the third and fourth parameters of [](py5graphics_shape) to specify the width and height. The syntax `shape_mode(CORNERS)` uses the first and second parameters of [](py5graphics_shape) to set the location of one corner and uses the third and fourth parameters to set the opposite corner. The syntax `shape_mode(CENTER)` draws the shape from its center point and uses the third and forth parameters of [](py5graphics_shape) to specify the width and height. The parameter must be written in ALL CAPS because Python is a case sensitive language.

This method is the same as [](sketch_shape_mode) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_shape_mode).

Underlying Processing method: PGraphics.shapeMode

## Signatures

```python
shape_mode(
    mode: int,  # either CORNER, CORNERS, CENTER
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
