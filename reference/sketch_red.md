# red()

Extracts the red value from a color, scaled to match current [](sketch_color_mode).

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for red()](/images/reference/Sketch_red_0.png)

</div><div class="example-cell-code">

```python
def setup():
    c = "#FFCC00"  # define color 'c'
    py5.fill(c)  # use color variable 'c' as fill color
    py5.rect(15, 20, 35, 60)  # draw left rectangle
    
    red_value = py5.red(c)  # get red in 'c'
    py5.println(red_value)  # print "255.0"
    py5.fill(red_value, 0, 0)  # use 'red_value' in new fill
    py5.rect(50, 20, 35, 60)  # draw right rectangle
```

</div></div>

</div>

## Description

Extracts the red value from a color, scaled to match current [](sketch_color_mode).

The `red()` function is easy to use and understand, but it is slower than a technique called bit shifting. When working in `color_mode(RGB, 255)`, you can achieve the same results as `red()` but with greater speed by using the right shift operator (`>>`) with a bit mask. For example, `red(c)` and `c >> 16 & 0xFF` both extract the red value from a color variable `c` but the later is faster.

This method has additional color functionality that is not reflected in the method's signatures. For example, you can pass the name of a color (e.g. "green", "mediumpurple", etc). Look at the online ["All About Colors"](/integrations/colors) Python Ecosystem Integration tutorial for more information.

Underlying Processing method: [red](https://processing.org/reference/red_.html)

## Signatures

```python
red(
    rgb: int,  # any value of the color datatype
    /,
) -> float
```

Updated on December 25, 2023 16:36:33pm UTC
