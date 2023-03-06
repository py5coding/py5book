# Py5Graphics.light_specular()

Sets the specular color for lights.

## Description

Sets the specular color for lights. Like [](py5graphics_fill), it affects only the elements which are created after it in the code. Specular refers to light which bounces off a surface in a preferred direction (rather than bouncing in all directions like a diffuse light) and is used for creating highlights. The specular quality of a light interacts with the specular material qualities set through the [](py5graphics_specular) and [](py5graphics_shininess) functions.

This method is the same as [](sketch_light_specular) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_light_specular).

Underlying Processing method: PGraphics.lightSpecular

## Signatures

```python
light_specular(
    v1: float,  # red or hue value (depending on current color mode)
    v2: float,  # green or saturation value (depending on current color mode)
    v3: float,  # blue or brightness value (depending on current color mode)
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
