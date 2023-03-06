# rect()

Draws a rectangle to the screen.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for rect()](/images/reference/Sketch_rect_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.rect(30, 20, 55, 55)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for rect()](/images/reference/Sketch_rect_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.rect(30, 20, 55, 55, 7)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for rect()](/images/reference/Sketch_rect_2.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.rect(30, 20, 55, 55, 3, 6, 12, 18)
```

</div></div>

</div>

## Description

Draws a rectangle to the screen. A rectangle is a four-sided shape with every angle at ninety degrees. By default, the first two parameters set the location of the upper-left corner, the third sets the width, and the fourth sets the height. The way these parameters are interpreted, however, may be changed with the [](sketch_rect_mode) function.

To draw a rounded rectangle, add a fifth parameter, which is used as the radius value for all four corners.

To use a different radius value for each corner, include eight parameters. When using eight parameters, the latter four set the radius of the arc at each corner separately, starting with the top-left corner and moving clockwise around the rectangle.

Underlying Processing method: [rect](https://processing.org/reference/rect_.html)

## Signatures

```python
rect(
    a: float,  # x-coordinate of the rectangle by default
    b: float,  # y-coordinate of the rectangle by default
    c: float,  # width of the rectangle by default
    d: float,  # height of the rectangle by default
    /,
) -> None

rect(
    a: float,  # x-coordinate of the rectangle by default
    b: float,  # y-coordinate of the rectangle by default
    c: float,  # width of the rectangle by default
    d: float,  # height of the rectangle by default
    r: float,  # radii for all four corners
    /,
) -> None

rect(
    a: float,  # x-coordinate of the rectangle by default
    b: float,  # y-coordinate of the rectangle by default
    c: float,  # width of the rectangle by default
    d: float,  # height of the rectangle by default
    tl: float,  # radius for top-left corner
    tr: float,  # radius for top-right corner
    br: float,  # radius for bottom-right corner
    bl: float,  # radius for bottom-left corner
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
