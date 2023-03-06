# camera()

Sets the position of the camera through setting the eye position, the center of the scene, and which axis is facing upward.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for camera()](/images/reference/Sketch_camera_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.no_fill()
    py5.background(204)
    py5.camera(70.0, 35.0, 120.0, 50.0, 50.0, 0.0, 0.0, 1.0, 0.0)
    py5.translate(50, 50, 0)
    py5.rotate_x(-py5.PI/6)
    py5.rotate_y(py5.PI/3)
    py5.box(45)
```

</div></div>

</div>

## Description

Sets the position of the camera through setting the eye position, the center of the scene, and which axis is facing upward. Moving the eye position and the direction it is pointing (the center of the scene) allows the images to be seen from different angles. The version without any parameters sets the camera to the default position, pointing to the center of the display window with the Y axis as up. The default values are `camera(width//2.0, height//2.0, (height//2.0) / tan(PI*30.0 / 180.0), width//2.0, height//2.0, 0, 0, 1, 0)`. This function is similar to `glu_look_at()` in OpenGL, but it first clears the current camera settings.

Underlying Processing method: [camera](https://processing.org/reference/camera_.html)

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
