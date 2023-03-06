# ellipse_mode()

Modifies the location from which ellipses are drawn by changing the way in which parameters given to [](sketch_ellipse) are intepreted.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for ellipse_mode()](/images/reference/Sketch_ellipse_mode_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.ellipse_mode(py5.RADIUS)  # set ellipse_mode to RADIUS
    py5.fill(255)  # set fill to white
    py5.ellipse(50, 50, 30, 30)  # draw white ellipse using RADIUS mode
    
    py5.ellipse_mode(py5.CENTER)  # set ellipse_mode to CENTER
    py5.fill(100)  # set fill to gray
    py5.ellipse(50, 50, 30, 30)  # draw gray ellipse using CENTER mode
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for ellipse_mode()](/images/reference/Sketch_ellipse_mode_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.ellipse_mode(py5.CORNER)  # set ellipse_mode is CORNER
    py5.fill(255)  # set fill to white
    py5.ellipse(25, 25, 50, 50)  # draw white ellipse using CORNER mode
    
    py5.ellipse_mode(py5.CORNERS)  # set ellipse_mode to CORNERS
    py5.fill(100)  # set fill to gray
    py5.ellipse(25, 25, 50, 50)  # draw gray ellipse using CORNERS mode
```

</div></div>

</div>

## Description

Modifies the location from which ellipses are drawn by changing the way in which parameters given to [](sketch_ellipse) are intepreted.

The default mode is `ellipse_mode(CENTER)`, which interprets the first two parameters of [](sketch_ellipse) as the shape's center point, while the third and fourth parameters are its width and height.

`ellipse_mode(RADIUS)` also uses the first two parameters of [](sketch_ellipse) as the shape's center point, but uses the third and fourth parameters to specify half of the shapes's width and height.

`ellipse_mode(CORNER)` interprets the first two parameters of [](sketch_ellipse) as the upper-left corner of the shape, while the third and fourth parameters are its width and height.

`ellipse_mode(CORNERS)` interprets the first two parameters of [](sketch_ellipse) as the location of one corner of the ellipse's bounding box, and the third and fourth parameters as the location of the opposite corner.

The parameter must be written in ALL CAPS because Python is a case-sensitive language.

Underlying Processing method: [ellipseMode](https://processing.org/reference/ellipseMode_.html)

## Signatures

```python
ellipse_mode(
    mode: int,  # either CENTER, RADIUS, CORNER, or CORNERS
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
