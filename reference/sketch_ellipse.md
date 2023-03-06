# ellipse()

Draws an ellipse (oval) to the screen.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for ellipse()](/images/reference/Sketch_ellipse_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.ellipse(56, 46, 55, 55)
```

</div></div>

</div>

## Description

Draws an ellipse (oval) to the screen. An ellipse with equal width and height is a circle. By default, the first two parameters set the location, and the third and fourth parameters set the shape's width and height. The origin may be changed with the [](sketch_ellipse_mode) function.

Underlying Processing method: [ellipse](https://processing.org/reference/ellipse_.html)

## Signatures

```python
ellipse(
    a: float,  # x-coordinate of the ellipse
    b: float,  # y-coordinate of the ellipse
    c: float,  # width of the ellipse by default
    d: float,  # height of the ellipse by default
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
