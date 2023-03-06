# Py5Graphics.spot_light()

Adds a spot light.

## Description

Adds a spot light. The `v1`, `v2`, and `v3` parameters are interpreted as either RGB or HSB values, depending on the current color mode. The `x`, `y`, and `z` parameters specify the position of the light and `nx`, `ny`, `nz` specify the direction of light. The `angle` parameter affects angle of the spotlight cone, while `concentration` sets the bias of light focusing toward the center of that cone.

This method is the same as [](sketch_spot_light) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_spot_light).

Underlying Processing method: PGraphics.spotLight

## Signatures

```python
spot_light(
    v1: float,  # red or hue value (depending on current color mode)
    v2: float,  # green or saturation value (depending on current color mode)
    v3: float,  # blue or brightness value (depending on current color mode)
    x: float,  # x-coordinate of the light
    y: float,  # y-coordinate of the light
    z: float,  # z-coordinate of the light
    nx: float,  # direction along the x axis
    ny: float,  # direction along the y axis
    nz: float,  # direction along the z axis
    angle: float,  # angle of the spotlight cone
    concentration: float,  # exponent determining the center bias of the cone
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
