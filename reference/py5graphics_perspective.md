# Py5Graphics.perspective()

Sets a perspective projection applying foreshortening, making distant objects appear smaller than closer ones.

## Description

Sets a perspective projection applying foreshortening, making distant objects appear smaller than closer ones. The parameters define a viewing volume with the shape of truncated pyramid. Objects near to the front of the volume appear their actual size, while farther objects appear smaller. This projection simulates the perspective of the world more accurately than orthographic projection. The version of perspective without parameters sets the default perspective and the version with four parameters allows the programmer to set the area precisely. The default values are: `perspective(PI/3.0, width/height, cameraZ/10.0, cameraZ*10.0)` where cameraZ is `((height/2.0) / tan(PI*60.0/360.0))`.

This method is the same as [](sketch_perspective) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_perspective).

Underlying Processing method: PGraphics.perspective

## Signatures

```python
perspective() -> None

perspective(
    fovy: float,  # field-of-view angle (in radians) for vertical direction
    aspect: float,  # ratio of width to height
    z_near: float,  # z-position of nearest clipping plane
    z_far: float,  # z-position of farthest clipping plane
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
