# alpha()

Extracts the alpha value from a color, scaled to match current [](sketch_color_mode).

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for alpha()](/images/reference/Sketch_alpha_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.no_stroke()
    c = py5.color(0, 126, 255, 102)
    py5.fill(c)
    py5.rect(15, 15, 35, 70)
    value = py5.alpha(c)  # sets 'value' to 102
    py5.fill(value)
    py5.rect(50, 15, 35, 70)
```

</div></div>

</div>

## Description

Extracts the alpha value from a color, scaled to match current [](sketch_color_mode).

The `alpha()` function is easy to use and understand, but it is slower than a technique called bit shifting. When working in `color_mode(RGB, 255)`, you can achieve the same results as `alpha()` but with greater speed by using the right shift operator (`>>`) with a bit mask. For example, `alpha(c)` and `c >> 24 & 0xFF` both extract the alpha value from a color variable `c` but the later is faster.

Underlying Processing method: [alpha](https://processing.org/reference/alpha_.html)

## Signatures

```python
alpha(
    rgb: int,  # any value of the color datatype
    /,
) -> float
```

Updated on March 06, 2023 02:49:26am UTC
