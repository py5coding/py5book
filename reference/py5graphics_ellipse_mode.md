# Py5Graphics.ellipse_mode()

Modifies the location from which ellipses are drawn by changing the way in which parameters given to [](py5graphics_ellipse) are intepreted.

## Description

Modifies the location from which ellipses are drawn by changing the way in which parameters given to [](py5graphics_ellipse) are intepreted.

The default mode is `ellipse_mode(CENTER)`, which interprets the first two parameters of [](py5graphics_ellipse) as the shape's center point, while the third and fourth parameters are its width and height.

`ellipse_mode(RADIUS)` also uses the first two parameters of [](py5graphics_ellipse) as the shape's center point, but uses the third and fourth parameters to specify half of the shapes's width and height.

`ellipse_mode(CORNER)` interprets the first two parameters of [](py5graphics_ellipse) as the upper-left corner of the shape, while the third and fourth parameters are its width and height.

`ellipse_mode(CORNERS)` interprets the first two parameters of [](py5graphics_ellipse) as the location of one corner of the ellipse's bounding box, and the third and fourth parameters as the location of the opposite corner.

The parameter must be written in ALL CAPS because Python is a case-sensitive language.

This method is the same as [](sketch_ellipse_mode) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_ellipse_mode).

Underlying Processing method: PGraphics.ellipseMode

## Signatures

```python
ellipse_mode(
    mode: int,  # either CENTER, RADIUS, CORNER, or CORNERS
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
