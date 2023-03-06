# clear()

Clear the drawing surface by setting every pixel to black.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for clear()](/images/reference/Sketch_clear_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.fill(255)
    py5.rect(5, 5, 40, 40)
    py5.clear()
    py5.rect(55, 55, 40, 40)
```

</div></div>

</div>

## Description

Clear the drawing surface by setting every pixel to black. Calling this method is the same as passing `0` to the [](sketch_background) method, as in `background(0)`.

This method behaves differently than [](py5graphics_clear) because `Py5Graphics` objects allow transparent pixels.

Underlying Processing method: [clear](https://processing.org/reference/clear_.html)

## Signatures

```python
clear() -> None
```

Updated on March 06, 2023 02:49:26am UTC
