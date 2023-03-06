# background()

The `background()` function sets the color used for the background of the py5 window.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for background()](/images/reference/Sketch_background_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.background(51)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for background()](/images/reference/Sketch_background_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.background(255, 204, 0)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for background()](/images/reference/Sketch_background_2.png)

</div><div class="example-cell-code">

```python
def setup():
    img = py5.load_image("laDefense.jpg")
    py5.background(img)
```

</div></div>

</div>

## Description

The `background()` function sets the color used for the background of the py5 window. The default background is light gray. This function is typically used within `draw()` to clear the display window at the beginning of each frame, but it can be used inside `setup()` to set the background on the first frame of animation or if the backgound need only be set once.
 
An image can also be used as the background for a Sketch, although the image's width and height must match that of the Sketch window. Images used with `background()` will ignore the current [](sketch_tint) setting. To resize an image to the size of the Sketch window, use `image.resize(width, height)`.
 
It is not possible to use the transparency `alpha` parameter with background colors on the main drawing surface. It can only be used along with a `Py5Graphics` object and [](sketch_create_graphics).

Underlying Processing method: [background](https://processing.org/reference/background_.html)

## Signatures

```python
background(
    gray: float,  # specifies a value between white and black
    /,
) -> None

background(
    gray: float,  # specifies a value between white and black
    alpha: float,  # opacity of the background
    /,
) -> None

background(
    image: Py5Image,  # Py5Image to set as background (must be same size as the Sketch window)
    /,
) -> None

background(
    rgb: int,  # any value of the color datatype
    /,
) -> None

background(
    rgb: int,  # any value of the color datatype
    alpha: float,  # opacity of the background
    /,
) -> None

background(
    v1: float,  # red or hue value (depending on the current color mode)
    v2: float,  # green or saturation value (depending on the current color mode)
    v3: float,  # blue or brightness value (depending on the current color mode)
    /,
) -> None

background(
    v1: float,  # red or hue value (depending on the current color mode)
    v2: float,  # green or saturation value (depending on the current color mode)
    v3: float,  # blue or brightness value (depending on the current color mode)
    alpha: float,  # opacity of the background
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
