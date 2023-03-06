# end_camera()

The [](sketch_begin_camera) and `end_camera()` methods enable advanced customization of the camera space.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for end_camera()](/images/reference/Sketch_end_camera_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.no_fill()

    py5.begin_camera()
    py5.camera()
    py5.rotate_x(-py5.PI/6)
    py5.end_camera()

    py5.translate(50, 50, 0)
    py5.rotate_y(py5.PI/3)
    py5.box(45)
```

</div></div>

</div>

## Description

The [](sketch_begin_camera) and `end_camera()` methods enable advanced customization of the camera space. Please see the reference for [](sketch_begin_camera) for a description of how the methods are used.

Underlying Processing method: [endCamera](https://processing.org/reference/endCamera_.html)

## Signatures

```python
end_camera() -> None
```

Updated on March 06, 2023 02:49:26am UTC
