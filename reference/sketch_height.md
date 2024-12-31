# height

Variable that stores the height of the display window.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for height](/images/reference/Sketch_height_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.no_stroke()
    py5.background(0)
    py5.rect(40, 0, 20, py5.height)
    py5.rect(60, 0, 20, py5.height//2)
```

</div></div>

</div>

## Description

Variable that stores the height of the display window. This value is set by the second parameter of the [](sketch_size) function. For example, the function call `size(320, 240)` sets the `height` variable to the value 240. The value of `height` defaults to 100 if [](sketch_size) is not used in a program.

Underlying Processing field: [height](https://processing.org/reference/height.html)

Updated on December 07, 2024 22:07:08pm UTC
