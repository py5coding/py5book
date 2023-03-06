# begin_contour()

Use the `begin_contour()` and [](sketch_end_contour) methods to create negative shapes within shapes such as the center of the letter 'O'.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for begin_contour()](/images/reference/Sketch_begin_contour_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.translate(50, 50)
    py5.stroke(255, 0, 0)
    py5.begin_shape()
    # exterior part of shape, clockwise winding
    py5.vertex(-40, -40)
    py5.vertex(40, -40)
    py5.vertex(40, 40)
    py5.vertex(-40, 40)
    py5.begin_contour()
    # interior part of shape, counter-clockwise winding
    py5.vertex(-20, -20)
    py5.vertex(-20, 20)
    py5.vertex(20, 20)
    py5.vertex(20, -20)
    py5.end_contour()
    py5.end_shape(py5.CLOSE)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for begin_contour()](/images/reference/Sketch_begin_contour_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.translate(50, 50)
    py5.stroke(255, 0, 0)
    with py5.begin_closed_shape():
        # exterior part of shape, clockwise winding
        py5.vertex(-40, -40)
        py5.vertex(40, -40)
        py5.vertex(40, 40)
        py5.vertex(-40, 40)
        with py5.begin_contour():
            # interior part of shape, counter-clockwise winding
            py5.vertex(-20, -20)
            py5.vertex(-20, 20)
            py5.vertex(20, 20)
            py5.vertex(20, -20)
```

</div></div>

</div>

## Description

Use the `begin_contour()` and [](sketch_end_contour) methods to create negative shapes within shapes such as the center of the letter 'O'. The `begin_contour()` method begins recording vertices for the shape and [](sketch_end_contour) stops recording. The vertices that define a negative shape must "wind" in the opposite direction from the exterior shape. First draw vertices for the exterior shape in clockwise order, then for internal shapes, draw vertices counterclockwise.

These methods can only be used within a [](sketch_begin_shape) & [](sketch_end_shape) pair and transformations such as [](sketch_translate), [](sketch_rotate), and [](sketch_scale) do not work within a `begin_contour()` & [](sketch_end_contour) pair. It is also not possible to use other shapes, such as [](sketch_ellipse) or [](sketch_rect) within.

This method can be used as a context manager to ensure that [](sketch_end_contour) always gets called, as shown in the second example.

Underlying Processing method: [beginContour](https://processing.org/reference/beginContour_.html)

## Signatures

```python
begin_contour() -> None
```

Updated on March 06, 2023 02:49:26am UTC
