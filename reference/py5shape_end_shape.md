# Py5Shape.end_shape()

This method is used to complete a custom shape created with the [](sketch_create_shape) function.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global s  # the Py5Shape object
    s = py5.create_shape()
    s.begin_shape()
    s.fill(0, 0, 255)
    s.no_stroke()
    s.vertex(0, 0)
    s.vertex(0, 50)
    s.vertex(50, 0)
    s.end_shape()


def draw():
    py5.shape(s, 25, 25)
```

</div></div>

</div>

## Description

This method is used to complete a custom shape created with the [](sketch_create_shape) function. It's always and only used with [](sketch_create_shape).

Underlying Processing method: [PShape.endShape](https://processing.org/reference/PShape_endShape_.html)

## Signatures

```python
end_shape() -> None

end_shape(
    mode: int,  # Either OPEN or CLOSE
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
