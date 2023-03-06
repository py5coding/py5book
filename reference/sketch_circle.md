# circle()

Draws a circle to the screen.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for circle()](/images/reference/Sketch_circle_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.circle(56, 46, 55)
```

</div></div>

</div>

## Description

Draws a circle to the screen. By default, the first two parameters set the location of the center, and the third sets the shape's width and height. The origin may be changed with the [](sketch_ellipse_mode) function.

Underlying Processing method: [circle](https://processing.org/reference/circle_.html)

## Signatures

```python
circle(
    x: float,  # x-coordinate of the ellipse
    y: float,  # y-coordinate of the ellipse
    extent: float,  # width and height of the ellipse by default
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
