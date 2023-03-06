# Py5Shape

Datatype for storing shapes.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for Py5Shape](/images/reference/Py5Shape_0.png)

</div><div class="example-cell-code">

```python
def setup():
    global s
    # the file "bot.svg" must be in the data folder
    # of the current sketch to load successfully
    s = py5.load_shape("bot.svg")


def draw():
    py5.shape(s, 10, 10, 80, 80)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for Py5Shape](/images/reference/Py5Shape_1.png)

</div><div class="example-cell-code">

```python
def setup():
    global s  # the Py5Shape object
    # creating the Py5Shape as a square. the corner
    # is 0,0 so that the center is at 40,40
    s = py5.create_shape(py5.RECT, 0, 0, 80, 80)


def draw():
    py5.shape(s, 10, 10)
```

</div></div>

</div>

## Description

Datatype for storing shapes. Before a shape is used, it must be loaded with the [](sketch_load_shape) or created with the [](sketch_create_shape). The [](sketch_shape) function is used to draw the shape to the display window. Py5 can currently load and display SVG (Scalable Vector Graphics) and OBJ shapes. OBJ files can only be opened using the `P3D` renderer. The [](sketch_load_shape) function supports SVG files created with Inkscape and Adobe Illustrator. It is not a full SVG implementation, but offers some straightforward support for handling vector data. A more complete SVG implementation can be provided by [](sketch_convert_image) if Cairo is installed. See installation instructions for additional detail.

The `Py5Shape` object contains a group of methods that can operate on the shape data.

To create a new shape, use the [](sketch_create_shape) function. Do not use the syntax `Py5Shape()`.

Underlying Processing class: [PShape](https://processing.org/reference/PShape.html)

The following methods and fields are provided:

```{include} include_py5shape.md
```

Updated on March 06, 2023 02:49:26am UTC
