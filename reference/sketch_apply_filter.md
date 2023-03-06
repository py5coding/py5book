# apply_filter()

Filters the display window using a preset filter or with a custom shader.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for apply_filter()](/images/reference/Sketch_apply_filter_0.png)

</div><div class="example-cell-code">

```python
def setup():
    img = py5.load_image("apples.jpg")
    py5.image(img, 0, 0)
    py5.apply_filter(py5.THRESHOLD)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for apply_filter()](/images/reference/Sketch_apply_filter_1.png)

</div><div class="example-cell-code">

```python
def setup():
    img = py5.load_image("apples.jpg")
    py5.image(img, 0, 0)
    py5.apply_filter(py5.GRAY)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for apply_filter()](/images/reference/Sketch_apply_filter_2.png)

</div><div class="example-cell-code">

```python
def setup():
    img = py5.load_image("apples.jpg")
    py5.image(img, 0, 0)
    py5.apply_filter(py5.INVERT)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for apply_filter()](/images/reference/Sketch_apply_filter_3.png)

</div><div class="example-cell-code">

```python
def setup():
    img = py5.load_image("apples.jpg")
    py5.image(img, 0, 0)
    py5.apply_filter(py5.POSTERIZE, 4)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for apply_filter()](/images/reference/Sketch_apply_filter_4.png)

</div><div class="example-cell-code">

```python
def setup():
    img = py5.load_image("apples.jpg")
    py5.image(img, 0, 0)
    py5.apply_filter(py5.BLUR, 6)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for apply_filter()](/images/reference/Sketch_apply_filter_5.png)

</div><div class="example-cell-code">

```python
def setup():
    img = py5.load_image("apples.jpg")
    py5.image(img, 0, 0)
    py5.apply_filter(py5.ERODE)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for apply_filter()](/images/reference/Sketch_apply_filter_6.png)

</div><div class="example-cell-code">

```python
def setup():
    img = py5.load_image("apples.jpg")
    py5.image(img, 0, 0)
    py5.apply_filter(py5.DILATE)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for apply_filter()](/images/reference/Sketch_apply_filter_7.png)

</div><div class="example-cell-code">

```python
def setup():
    global blur
    global img
    py5.size(100, 100, py5.P2D)
    blur = py5.load_shader("blur.glsl")
    img = py5.load_image("apples.jpg")
    py5.image(img, 0, 0)


def draw():
    py5.apply_filter(blur)  # blurs more each time through draw()
```

</div></div>

</div>

## Description

Filters the display window using a preset filter or with a custom shader. Using a shader with `apply_filter()` is much faster than without. Shaders require the `P2D` or `P3D` renderer in [](sketch_size).

The presets options are:

* THRESHOLD: Converts the image to black and white pixels depending if they are above or below the threshold defined by the level parameter. The parameter must be between 0.0 (black) and 1.0 (white). If no level is specified, 0.5 is used.
* GRAY: Converts any colors in the image to grayscale equivalents. No parameter is used.
* OPAQUE: Sets the alpha channel to entirely opaque. No parameter is used.
* INVERT: Sets each pixel to its inverse value. No parameter is used.
* POSTERIZE: Limits each channel of the image to the number of colors specified as the parameter. The parameter can be set to values between 2 and 255, but results are most noticeable in the lower ranges.
* BLUR: Executes a Guassian blur with the level parameter specifying the extent of the blurring. If no parameter is used, the blur is equivalent to Guassian blur of radius 1. Larger values increase the blur.
* ERODE: Reduces the light areas. No parameter is used.
* DILATE: Increases the light areas. No parameter is used.

Underlying Processing method: [filter](https://processing.org/reference/filter_.html)

## Signatures

```python
apply_filter(
    kind: int,  # Either THRESHOLD, GRAY, OPAQUE, INVERT, POSTERIZE, BLUR, ERODE, or DILATE
    /,
) -> None

apply_filter(
    kind: int,  # Either THRESHOLD, GRAY, OPAQUE, INVERT, POSTERIZE, BLUR, ERODE, or DILATE
    param: float,  # unique for each, see above
    /,
) -> None

apply_filter(
    shader: Py5Shader,  # the fragment shader to apply
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
