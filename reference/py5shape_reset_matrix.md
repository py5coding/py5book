# Py5Shape.reset_matrix()

Replaces the current matrix of a shape with the identity matrix.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global s
    s = py5.load_shape("bot.svg")
    s.rotate(py5.PI/6)


def draw():
    py5.background(204)
    py5.scale(0.2)
    py5.shape(s, py5.width//2, py5.height//2)


def mouse_pressed():
    # removes all transformations applied to shape
    # loads the identity matrix
    s.reset_matrix()
```

</div></div>

</div>

## Description

Replaces the current matrix of a shape with the identity matrix. The equivalent function in OpenGL is `gl_load_identity()`.

Underlying Processing method: [PShape.resetMatrix](https://processing.org/reference/PShape_resetMatrix_.html)

## Signatures

```python
reset_matrix() -> None
```

Updated on March 06, 2023 02:49:26am UTC
