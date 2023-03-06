# stroke_weight()

Sets the width of the stroke used for lines, points, and the border around shapes.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for stroke_weight()](/images/reference/Sketch_stroke_weight_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.stroke_weight(1)  # default
    py5.line(20, 20, 80, 20)
    py5.stroke_weight(4)  # thicker
    py5.line(20, 40, 80, 40)
    py5.stroke_weight(10)  # beastly
    py5.line(20, 70, 80, 70)
```

</div></div>

</div>

## Description

Sets the width of the stroke used for lines, points, and the border around shapes. All widths are set in units of pixels.

Using [](sketch_point) with `strokeWeight(1)` or smaller may draw nothing to the screen, depending on the graphics settings of the computer. Workarounds include setting the pixel using the [](sketch_pixels) or [](sketch_np_pixels) arrays or drawing the point using either [](sketch_circle) or [](sketch_square).

Underlying Processing method: [strokeWeight](https://processing.org/reference/strokeWeight_.html)

## Signatures

```python
stroke_weight(
    weight: float,  # the weight (in pixels) of the stroke
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
