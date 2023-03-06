# image_mode()

Modifies the location from which images are drawn by changing the way in which parameters given to [](sketch_image) are intepreted.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for image_mode()](/images/reference/Sketch_image_mode_0.png)

</div><div class="example-cell-code">

```python
def setup():
    global img
    img = py5.load_image("laDefense.jpg")


def draw():
    py5.image_mode(py5.CORNER)
    py5.image(img, 10, 10, 50, 50)  # draw image using CORNER mode
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for image_mode()](/images/reference/Sketch_image_mode_1.png)

</div><div class="example-cell-code">

```python
def setup():
    global img
    img = py5.load_image("laDefense.jpg")


def draw():
    py5.image_mode(py5.CORNERS)
    py5.image(img, 10, 10, 90, 40)  # draw image using CORNERS mode
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for image_mode()](/images/reference/Sketch_image_mode_2.png)

</div><div class="example-cell-code">

```python
def setup():
    global img
    img = py5.load_image("laDefense.jpg")


def draw():
    py5.image_mode(py5.CENTER)
    py5.image(img, 50, 50, 80, 80)  # draw image using CENTER mode
```

</div></div>

</div>

## Description

Modifies the location from which images are drawn by changing the way in which parameters given to [](sketch_image) are intepreted.

The default mode is `image_mode(CORNER)`, which interprets the second and third parameters of [](sketch_image) as the upper-left corner of the image. If two additional parameters are specified, they are used to set the image's width and height.

`image_mode(CORNERS)` interprets the second and third parameters of [](sketch_image) as the location of one corner, and the fourth and fifth parameters as the opposite corner.

`image_mode(CENTER)` interprets the second and third parameters of [](sketch_image) as the image's center point. If two additional parameters are specified, they are used to set the image's width and height.

The parameter must be written in ALL CAPS because Python is a case-sensitive language.

Underlying Processing method: [imageMode](https://processing.org/reference/imageMode_.html)

## Signatures

```python
image_mode(
    mode: int,  # either CORNER, CORNERS, or CENTER
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
