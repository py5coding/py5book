# box()

A box is an extruded rectangle.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for box()](/images/reference/Sketch_box_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.translate(58, 48, 0)
    py5.rotate_y(0.5)
    py5.no_fill()
    py5.box(40)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for box()](/images/reference/Sketch_box_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.translate(58, 48, 0)
    py5.rotate_y(0.5)
    py5.no_fill()
    py5.box(40, 20, 50)
```

</div></div>

</div>

## Description

A box is an extruded rectangle. A box with equal dimensions on all sides is a cube.

Underlying Processing method: [box](https://processing.org/reference/box_.html)

## Signatures

```python
box(
    size: float,  # dimension of the box in all dimensions (creates a cube)
    /,
) -> None

box(
    w: float,  # dimension of the box in the x-dimension
    h: float,  # dimension of the box in the y-dimension
    d: float,  # dimension of the box in the z-dimension
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
