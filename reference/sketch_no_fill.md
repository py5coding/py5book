# no_fill()

Disables filling geometry.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for no_fill()](/images/reference/Sketch_no_fill_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.rect(15, 10, 55, 55)
    py5.no_fill()
    py5.rect(30, 20, 55, 55)
```

</div></div>

</div>

## Description

Disables filling geometry. If both [](sketch_no_stroke) and `no_fill()` are called, nothing will be drawn to the screen.

Underlying Processing method: [noFill](https://processing.org/reference/noFill_.html)

## Signatures

```python
no_fill() -> None
```

Updated on March 06, 2023 02:49:26am UTC
