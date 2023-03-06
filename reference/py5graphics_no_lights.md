# Py5Graphics.no_lights()

Disable all lighting.

## Description

Disable all lighting. Lighting is turned off by default and enabled with the [](py5graphics_lights) function. This function can be used to disable lighting so that 2D geometry (which does not require lighting) can be drawn after a set of lighted 3D geometry.

This method is the same as [](sketch_no_lights) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_no_lights).

Underlying Processing method: PGraphics.noLights

## Signatures

```python
no_lights() -> None
```

Updated on March 06, 2023 02:49:26am UTC
