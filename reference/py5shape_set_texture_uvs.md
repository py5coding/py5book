# Py5Shape.set_texture_uvs()

Set all of the uv texture mapping coordinates for a `Py5Shape` object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for set_texture_uvs()](/images/reference/Py5Shape_set_texture_uvs_0.png)

</div><div class="example-cell-code">

```python
import numpy as np

def setup():
    py5.size(100, 100, py5.P2D)
    img = py5.load_image("tower.jpg")
    s = py5.create_shape()
    with s.begin_closed_shape():
        s.vertex(20, 20)
        s.vertex(20, 80)
        s.vertex(80, 80)
        s.vertex(80, 20)

    s.set_texture(img)
    s.set_texture_mode(py5.NORMAL)
    uvs = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
    s.set_texture_uvs(uvs)

    py5.shape(s)
```

</div></div>

</div>

## Description

Set all of the uv texture mapping coordinates for a `Py5Shape` object. This method can only be used outside the [](py5shape_begin_shape) and [](py5shape_end_shape) methods. This method is similar to but much faster than [](py5shape_set_texture_uv) when used in a `for` loop.

The uv texture coordinates define the mapping of a `Py5Shape` object's texture to the form. By default, the coordinates used for `u` and `v` are specified in relation to the image's size in pixels, but this relation can be changed with the `Py5Shape` object's [](py5shape_set_texture_mode) method.

## Signatures

```python
set_texture_uvs(
    uvs: Sequence[Sequence[float]],  # horizontal and vertical coordinates for the texture mapping
    /,
) -> None
```

Updated on October 12, 2026 17:40:58pm UTC
