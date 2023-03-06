# begin_camera()

The `begin_camera()` and [](sketch_end_camera) functions enable advanced customization of the camera space.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for begin_camera()](/images/reference/Sketch_begin_camera_0.png)

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

<div class="example-row"><div class="example-cell-image">

![example picture for begin_camera()](/images/reference/Sketch_begin_camera_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.no_fill()

    with py5.begin_camera():
        py5.camera()
        py5.rotate_x(-py5.PI/6)

    py5.translate(50, 50, 0)
    py5.rotate_y(py5.PI/3)

    py5.box(45)
```

</div></div>

</div>

## Description

The `begin_camera()` and [](sketch_end_camera) functions enable advanced customization of the camera space. The functions are useful if you want to more control over camera movement, however for most users, the [](sketch_camera) function will be sufficient. The camera functions will replace any transformations (such as [](sketch_rotate) or [](sketch_translate)) that occur before them in `draw()`, but they will not automatically replace the camera transform itself. For this reason, camera functions should be placed at the beginning of `draw()` (so that transformations happen afterwards), and the [](sketch_camera) function can be used after `begin_camera()` if you want to reset the camera before applying transformations.

This function sets the matrix mode to the camera matrix so calls such as [](sketch_translate), [](sketch_rotate), [](sketch_apply_matrix) and [](sketch_reset_matrix) affect the camera. `begin_camera()` should always be used with a following [](sketch_end_camera) and pairs of `begin_camera()` and [](sketch_end_camera) cannot be nested.

This method can be used as a context manager to ensure that [](sketch_end_camera) always gets called, as shown in the last example.

Underlying Processing method: [beginCamera](https://processing.org/reference/beginCamera_.html)

## Signatures

```python
begin_camera() -> None
```

Updated on March 06, 2023 02:49:26am UTC
