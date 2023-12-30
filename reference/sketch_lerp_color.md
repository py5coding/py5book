# lerp_color()

Calculates a color between two colors at a specific increment.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for lerp_color()](/images/reference/Sketch_lerp_color_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.stroke(255)
    py5.background(51)
    from_ = "#CC6600"
    to = "#006699"
    inter_a = py5.lerp_color(from_, to, .33)
    inter_b = py5.lerp_color(from_, to, .66)
    py5.fill(from_)
    py5.rect(10, 20, 20, 60)
    py5.fill(inter_a)
    py5.rect(30, 20, 20, 60)
    py5.fill(inter_b)
    py5.rect(50, 20, 20, 60)
    py5.fill(to)
    py5.rect(70, 20, 20, 60)
```

</div></div>

</div>

## Description

Calculates a color between two colors at a specific increment. The `amt` parameter is the amount to interpolate between the two values where 0.0 is equal to the first point, 0.1 is very near the first point, 0.5 is halfway in between, etc. 

An amount below 0 will be treated as 0. Likewise, amounts above 1 will be capped at 1. This is different from the behavior of [](sketch_lerp), but necessary because otherwise numbers outside the range will produce strange and unexpected colors.

This method has additional color functionality that is not reflected in the method's signatures. For example, you can pass the name of a color (e.g. "green", "mediumpurple", etc). Look at the online ["All About Colors"](/integrations/colors) Python Ecosystem Integration tutorial for more information.

Underlying Processing method: [lerpColor](https://processing.org/reference/lerpColor_.html)

## Signatures

```python
lerp_color(
    c1: int,  # interpolate from this color
    c2: int,  # interpolate to this color
    amt: float,  # between 0.0 and 1.0
    /,
) -> int

lerp_color(
    c1: int,  # interpolate from this color
    c2: int,  # interpolate to this color
    amt: float,  # between 0.0 and 1.0
    mode: int,  # either RGB or HSB
    /,
) -> int
```

Updated on December 25, 2023 16:36:33pm UTC
