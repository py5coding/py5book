# square()

Draws a square to the screen.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for square()](/images/reference/Sketch_square_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.square(30, 20, 55)
```

</div></div>

</div>

## Description

Draws a square to the screen. A square is a four-sided shape with every angle at ninety degrees and each side is the same length. By default, the first two parameters set the location of the upper-left corner, the third sets the width and height. The way these parameters are interpreted, however, may be changed with the [](sketch_rect_mode) function.

Underlying Processing method: [square](https://processing.org/reference/square_.html)

## Signatures

```python
square(
    x: float,  # x-coordinate of the rectangle by default
    y: float,  # y-coordinate of the rectangle by default
    extent: float,  # width and height of the rectangle by default
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
