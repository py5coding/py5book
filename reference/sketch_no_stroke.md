# no_stroke()

Disables drawing the stroke (outline).

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for no_stroke()](/images/reference/Sketch_no_stroke_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.no_stroke()
    py5.rect(30, 20, 55, 55)
```

</div></div>

</div>

## Description

Disables drawing the stroke (outline). If both `no_stroke()` and [](sketch_no_fill) are called, nothing will be drawn to the screen.

Underlying Processing method: [noStroke](https://processing.org/reference/noStroke_.html)

## Signatures

```python
no_stroke() -> None
```

Updated on March 06, 2023 02:49:26am UTC
