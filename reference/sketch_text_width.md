# text_width()

Calculates and returns the width of any character or text string.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for text_width()](/images/reference/Sketch_text_width_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.text_size(28)
    
    c = 't'
    cw = py5.text_width(c)
    py5.text(c, 0, 40)
    py5.line(cw, 0, cw, 50)

    s = "Tokyo"
    sw = py5.text_width(s)
    py5.text(s, 0, 85)
    py5.line(sw, 50, sw, 100)
```

</div></div>

</div>

## Description

Calculates and returns the width of any character or text string.

Underlying Processing method: [textWidth](https://processing.org/reference/textWidth_.html)

## Signatures

```python
text_width(
    c: chr,  # the character to measure
    /,
) -> float

text_width(
    chars: Iterator[chr],  # the characters to measure
    start: int,  # first character to measure
    length: int,  # number of characters to measure
    /,
) -> float

text_width(
    str: str,  # the String of characters to measure
    /,
) -> float
```

Updated on January 06, 2025 23:06:20pm UTC
