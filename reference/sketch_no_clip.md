# no_clip()

Disables the clipping previously started by the [](sketch_clip) function.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(200, 200)
    py5.image_mode(py5.CENTER)


def draw():
    py5.background(204)
    if py5.is_mouse_pressed:
        py5.clip(py5.mouse_x, py5.mouse_y, 100, 100)
    else:
        py5.no_clip()

    py5.line(0, 0, py5.width, py5.height)
    py5.line(0, py5.height, py5.width, 0)
```

</div></div>

</div>

## Description

Disables the clipping previously started by the [](sketch_clip) function.

Underlying Processing method: [noClip](https://processing.org/reference/noClip_.html)

## Signatures

```python
no_clip() -> None
```

Updated on March 06, 2023 02:49:26am UTC
