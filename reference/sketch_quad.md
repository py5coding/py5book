# quad()

A quad is a quadrilateral, a four sided polygon.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for quad()](/images/reference/Sketch_quad_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.quad(38, 31, 86, 20, 69, 63, 30, 76)
```

</div></div>

</div>

## Description

A quad is a quadrilateral, a four sided polygon. It is similar to a rectangle, but the angles between its edges are not constrained to ninety degrees. The first pair of parameters (x1,y1) sets the first vertex and the subsequent pairs should proceed clockwise or counter-clockwise around the defined shape.

Underlying Processing method: [quad](https://processing.org/reference/quad_.html)

## Signatures

```python
quad(
    x1: float,  # x-coordinate of the first corner
    y1: float,  # y-coordinate of the first corner
    x2: float,  # x-coordinate of the second corner
    y2: float,  # y-coordinate of the second corner
    x3: float,  # x-coordinate of the third corner
    y3: float,  # y-coordinate of the third corner
    x4: float,  # x-coordinate of the fourth corner
    y4: float,  # y-coordinate of the fourth corner
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
