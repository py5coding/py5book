# text_descent()

Returns descent of the current font at its current size.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for text_descent()](/images/reference/Sketch_text_descent_0.png)

</div><div class="example-cell-code">

```python
def setup():
    base = py5.height * 0.75
    scalar = 0.8  # different for each font
    
    py5.text_size(32)  # set initial text size
    a = py5.text_descent() * scalar  # calc ascent
    py5.line(0, base+a, py5.width, base+a)
    py5.text("dp", 0, base)  # draw text on baseline
    
    py5.text_size(64)  # increase text size
    a = py5.text_descent() * scalar  # recalc ascent
    py5.line(40, base+a, py5.width, base+a)
    py5.text("dp", 40, base)  # draw text on baseline
```

</div></div>

</div>

## Description

Returns descent of the current font at its current size. This information is useful for determining the height of the font below the baseline.

Underlying Processing method: [textDescent](https://processing.org/reference/textDescent_.html)

## Signatures

```python
text_descent() -> float
```

Updated on March 06, 2023 02:49:26am UTC
