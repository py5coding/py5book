# width

Variable that stores the width of the display window.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for width](/images/reference/Sketch_width_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.no_stroke()
    py5.background(0)
    py5.rect(0, 40, py5.width, 20)
    py5.rect(0, 60, py5.width//2, 20)
```

</div></div>

</div>

## Description

Variable that stores the width of the display window. This value is set by the first parameter of the [](sketch_size) function. For example, the function call `size(320, 240)` sets the `width` variable to the value 320. The value of `width` defaults to 100 if [](sketch_size) is not used in a program.

Underlying Processing field: [width](https://processing.org/reference/width.html)

Updated on December 07, 2024 22:07:08pm UTC
