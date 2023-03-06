# Py5Graphics.camera()

Sets the position of the camera through setting the eye position, the center of the scene, and which axis is facing upward.

## Description

Sets the position of the camera through setting the eye position, the center of the scene, and which axis is facing upward. Moving the eye position and the direction it is pointing (the center of the scene) allows the images to be seen from different angles. The version without any parameters sets the camera to the default position, pointing to the center of the Py5Graphics drawing surface with the Y axis as up. The default values are `camera(width//2.0, height//2.0, (height//2.0) / tan(PI*30.0 / 180.0), width//2.0, height//2.0, 0, 0, 1, 0)`. This function is similar to `glu_look_at()` in OpenGL, but it first clears the current camera settings.

This method is the same as [](sketch_camera) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_camera).

Underlying Processing method: PGraphics.camera

## Signatures

```python
camera() -> None

camera(
    eye_x: float,  # x-coordinate for the eye
    eye_y: float,  # y-coordinate for the eye
    eye_z: float,  # z-coordinate for the eye
    center_x: float,  # x-coordinate for the center of the scene
    center_y: float,  # y-coordinate for the center of the scene
    center_z: float,  # z-coordinate for the center of the scene
    up_x: float,  # usually 0.0, 1.0, or -1.0
    up_y: float,  # usually 0.0, 1.0, or -1.0
    up_z: float,  # usually 0.0, 1.0, or -1.0
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
