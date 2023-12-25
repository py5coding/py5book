# Py5Shape.set_tint()

Apply a color tint to a shape's texture map.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for set_tint()](/images/reference/Py5Shape_set_tint_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P2D)
    img = py5.load_image("tower.jpg")
    s = py5.create_shape()
    s.begin_shape()
    s.texture(img)
    s.vertex(20, 20, 0, 0)
    s.vertex(20, 80, 0, 100)
    s.vertex(80, 80, 100, 100)
    s.vertex(80, 20, 100, 0)
    s.end_shape(py5.CLOSE)

    s.set_tint(0, "#0000FF")
    s.set_tint(2, "#FF0000")
    py5.shape(s)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global s
    py5.size(100, 100, py5.P2D)
    img = py5.load_image("tower.jpg")
    s = py5.create_shape()
    s.begin_shape()
    s.texture(img)
    s.tint(0, 0, 255)
    s.vertex(20, 20, 0, 0)
    s.vertex(20, 80, 0, 100)
    s.vertex(80, 80, 100, 100)
    s.vertex(80, 20, 100, 0)
    s.end_shape(py5.CLOSE)


def draw():
    if py5.frame_count == 50:
        s.set_tint(False)
    if py5.frame_count == 100:
        s.set_tint("#FF0000")

    py5.shape(s)
```

</div></div>

</div>

## Description

Apply a color tint to a shape's texture map. This can be done for either the entire shape or one vertex.

This method differs from [](py5shape_tint) in that it is only to be used outside the [](py5shape_begin_shape) and [](py5shape_end_shape) methods. This method only works with the `P2D` and `P3D` renderers.

Calling this method with the boolean parameter `False` will delete the assigned tint. A later call with the boolean parameter `True` will not restore it; you must reassign the tint color, as shown in the second example.

This method has additional color functionality that is not reflected in the method's signatures. For example, you can pass the name of a color (e.g. "green", "mediumpurple", etc). Look at the online ["All About Colors"](/integrations/colors) Python Ecosystem Integration tutorial for more information.

Underlying Processing method: PShape.setTint

## Signatures

```python
set_tint(
    fill: int,  # color value in hexadecimal notation
    /,
) -> None

set_tint(
    index: int,  # vertex index
    tint: int,  # color value in hexadecimal notation
    /,
) -> None

set_tint(
    tint: bool,  # allow tint
    /,
) -> None
```

Updated on December 25, 2023 16:36:33pm UTC
