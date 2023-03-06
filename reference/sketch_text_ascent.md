# text_ascent()

Returns ascent of the current font at its current size.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for text_ascent()](/images/reference/Sketch_text_ascent_0.png)

</div><div class="example-cell-code">

```python
def setup():
    base = py5.height * 0.75
    scalar = 0.8  # different for each font
    
    py5.text_size(32)  # set initial text size
    a = py5.text_ascent() * scalar  # calc ascent
    py5.line(0, base-a, py5.width, base-a)
    py5.text("dp", 0, base)  # draw text on baseline
    
    py5.text_size(64)  # increase text size
    a = py5.text_ascent() * scalar  # recalc ascent
    py5.line(40, base-a, py5.width, base-a)
    py5.text("dp", 40, base)  # draw text on baseline
```

</div></div>

</div>

## Description

Returns ascent of the current font at its current size. This information is useful for determining the height of the font above the baseline.

Underlying Processing method: [textAscent](https://processing.org/reference/textAscent_.html)

## Signatures

```python
text_ascent() -> float
```

Updated on March 06, 2023 02:49:26am UTC
