# stroke_cap()

Sets the style for rendering line endings.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for stroke_cap()](/images/reference/Sketch_stroke_cap_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.stroke_weight(12.0)
    py5.stroke_cap(py5.ROUND)
    py5.line(20, 30, 80, 30)
    py5.stroke_cap(py5.SQUARE)
    py5.line(20, 50, 80, 50)
    py5.stroke_cap(py5.PROJECT)
    py5.line(20, 70, 80, 70)
```

</div></div>

</div>

## Description

Sets the style for rendering line endings. These ends are either squared, extended, or rounded, each of which specified with the corresponding parameters: `SQUARE`, `PROJECT`, and `ROUND`. The default cap is `ROUND`.

To make [](sketch_point) appear square, use `stroke_cap(PROJECT)`. Using `stroke_cap(SQUARE)` (no cap) causes points to become invisible.

Underlying Processing method: [strokeCap](https://processing.org/reference/strokeCap_.html)

## Signatures

```python
stroke_cap(
    cap: int,  # either SQUARE, PROJECT, or ROUND
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
