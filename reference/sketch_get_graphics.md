# get_graphics()

Get the [](py5graphics) object used by the Sketch.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.rect(10, 10, 50, 50)
    g = py5.get_graphics()
    py5.println(type(g))
```

</div></div>

</div>

## Description

Get the [](py5graphics) object used by the Sketch. Internally, all of Processing's drawing functionality comes from interaction with PGraphics objects, and this will provide direct access to the PGraphics object used by the Sketch.

Underlying Processing method: getGraphics

## Signatures

```python
get_graphics() -> Py5Graphics
```

Updated on March 06, 2023 02:49:26am UTC
