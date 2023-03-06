# text_size()

Sets the current font size.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for text_size()](/images/reference/Sketch_text_size_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.background(0)
    py5.fill(255)
    py5.text_size(26)
    py5.text("WORD", 10, 50)
    py5.text_size(14)
    py5.text("WORD", 10, 70)
```

</div></div>

</div>

## Description

Sets the current font size. This size will be used in all subsequent calls to the [](sketch_text) function. Font size is measured in units of pixels.

Underlying Processing method: [textSize](https://processing.org/reference/textSize_.html)

## Signatures

```python
text_size(
    size: float,  # the size of the letters in units of pixels
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
