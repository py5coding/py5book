# load_shape()

Loads geometry into a variable of type `Py5Shape`.

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
    py5.shape(s, 10, 10, 80, 80)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global s
    py5.size(100, 100, py5.P3D)
    # the file "teapot.obj" must be in the data folder
    # of the current sketch to load successfully
    s = py5.load_shape("teapot.obj")


def draw():
    py5.background(204)
    py5.translate(py5.width//2, py5.height//2)
    py5.scale(12)
    py5.shape(s, 0, 0)
```

</div></div>

</div>

## Description

Loads geometry into a variable of type `Py5Shape`. SVG and OBJ files may be loaded. To load correctly, the file must be located in the data directory of the current Sketch. In most cases, `load_shape()` should be used inside `setup()` because loading shapes inside `draw()` will reduce the speed of a Sketch.

Alternatively, the file maybe be loaded from anywhere on the local computer using an absolute path (something that starts with / on Unix and Linux, or a drive letter on Windows), or the filename parameter can be a URL for a file found on a network.

If the shape file is not available or for whatever reason a shape cannot be created, an exception will be thrown.

Underlying Processing method: [loadShape](https://processing.org/reference/loadShape_.html)

## Signatures

```python
load_shape(
    filename: str,  # name of file to load, can be .svg or .obj
    /,
) -> Py5Shape

load_shape(
    filename: str,  # name of file to load, can be .svg or .obj
    options: str,  # unused parameter
    /,
) -> Py5Shape
```

Updated on October 06, 2023 13:36:04pm UTC
