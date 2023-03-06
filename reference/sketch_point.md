# point()

Draws a point, a coordinate in space at the dimension of one pixel.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for point()](/images/reference/Sketch_point_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.no_smooth()
    py5.point(30, 20)
    py5.point(85, 20)
    py5.point(85, 75)
    py5.point(30, 75)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for point()](/images/reference/Sketch_point_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.no_smooth()
    py5.point(30, 20, -50)
    py5.point(85, 20, -50)
    py5.point(85, 75, -50)
    py5.point(30, 75, -50)
```

</div></div>

</div>

## Description

Draws a point, a coordinate in space at the dimension of one pixel. The first parameter is the horizontal value for the point, the second value is the vertical value for the point, and the optional third value is the depth value. Drawing this shape in 3D with the `z` parameter requires the `P3D` parameter in combination with [](sketch_size) as shown in the second example.

Use [](sketch_stroke) to set the color of a `point()`.

Point appears round with the default `stroke_cap(ROUND)` and square with `stroke_cap(PROJECT)`. Points are invisible with `stroke_cap(SQUARE)` (no cap).

Using `point()` with `strokeWeight(1)` or smaller may draw nothing to the screen, depending on the graphics settings of the computer. Workarounds include setting the pixel using the [](sketch_pixels) or [](sketch_np_pixels) arrays or drawing the point using either [](sketch_circle) or [](sketch_square).

Underlying Processing method: [point](https://processing.org/reference/point_.html)

## Signatures

```python
point(
    x: float,  # x-coordinate of the point
    y: float,  # y-coordinate of the point
    /,
) -> None

point(
    x: float,  # x-coordinate of the point
    y: float,  # y-coordinate of the point
    z: float,  # z-coordinate of the point
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
