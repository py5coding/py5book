# Py5Shape.is_visible()

Returns a boolean value `True` if the image is set to be visible, `False` if not.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global s
    # the file "bot.svg" must be in the data folder
    # of the current sketch to load successfully
    s = py5.load_shape("bot.svg")


def draw():
    py5.background(204)
    py5.shape(s, 10, 10, 80, 80)  # draw shape
    s.set_visible(py5.is_mouse_pressed)
    if s.is_visible() == False:  # or use: "if not s.isVisible"
        py5.no_fill()
        py5.rect(10, 10, 80, 80)
```

</div></div>

</div>

## Description

Returns a boolean value `True` if the image is set to be visible, `False` if not. This value can be modified with the [](py5shape_set_visible) method.

The default visibility of a shape is usually controlled by whatever program created the SVG file. For instance, this parameter is controlled by showing or hiding the shape in the layers palette in Adobe Illustrator.

Underlying Processing method: [PShape.isVisible](https://processing.org/reference/PShape_isVisible_.html)

## Signatures

```python
is_visible() -> bool
```

Updated on March 06, 2023 02:49:26am UTC
