# Py5Graphics.lerp_color()

Calculates a color between two colors at a specific increment.

## Description

Calculates a color between two colors at a specific increment. The `amt` parameter is the amount to interpolate between the two values where 0.0 is equal to the first point, 0.1 is very near the first point, 0.5 is halfway in between, etc. 

An amount below 0 will be treated as 0. Likewise, amounts above 1 will be capped at 1. This is different from the behavior of [](sketch_lerp), but necessary because otherwise numbers outside the range will produce strange and unexpected colors.

This method is the same as [](sketch_lerp_color) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_lerp_color).

Underlying Processing method: PGraphics.lerpColor

## Signatures

```python
lerp_color(
    c1: int,  # interpolate from this color
    c2: int,  # interpolate to this color
    amt: float,  # between 0.0 and 1.0
    /,
) -> int

lerp_color(
    c1: int,  # interpolate from this color
    c2: int,  # interpolate to this color
    amt: float,  # between 0.0 and 1.0
    mode: int,  # either RGB or HSB
    /,
) -> int
```

Updated on March 06, 2023 02:49:26am UTC
