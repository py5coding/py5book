# blue()

Extracts the blue value from a color, scaled to match current [](sketch_color_mode).

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for blue()](/images/reference/Sketch_blue_0.png)

</div><div class="example-cell-code">

```python
def setup():
    c = "#AF64DC"  # define color 'c'
    py5.fill(c)  # use color variable 'c' as fill color
    py5.rect(15, 20, 35, 60)  # draw left rectangle
    
    blue_value = py5.blue(c)  # get blue in 'c'
    py5.println(blue_value)  # prints "220.0"
    py5.fill(0, 0, blue_value)  # use 'blue_value' in new fill
    py5.rect(50, 20, 35, 60)  # draw right rectangle
```

</div></div>

</div>

## Description

Extracts the blue value from a color, scaled to match current [](sketch_color_mode).

The `blue()` function is easy to use and understand, but it is slower than a technique called bit masking. When working in `color_mode(RGB, 255)`, you can achieve the same results as `blue()` but with greater speed by using a bit mask to remove the other color components. For example, `blue(c)` and `c & 0xFF` both extract the blue value from a color variable `c` but the later is faster.

Underlying Processing method: [blue](https://processing.org/reference/blue_.html)

## Signatures

```python
blue(
    rgb: int,  # any value of the color datatype
    /,
) -> float
```

Updated on March 06, 2023 02:49:26am UTC
