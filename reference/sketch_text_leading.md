# text_leading()

Sets the spacing between lines of text in units of pixels.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for text_leading()](/images/reference/Sketch_text_leading_0.png)

</div><div class="example-cell-code">

```python
def setup():
    # text to display. the "\n" is a "new line" character
    lines_of_text = "L1\nL2\nL3"
    py5.text_size(12)
    py5.fill(0)  # set fill to black
    
    py5.text_leading(10)  # set leading to 10
    py5.text(lines_of_text, 10, 25)
    
    py5.text_leading(20)  # set leading to 20
    py5.text(lines_of_text, 40, 25)
    
    py5.text_leading(30)  # set leading to 30
    py5.text(lines_of_text, 70, 25)
```

</div></div>

</div>

## Description

Sets the spacing between lines of text in units of pixels. This setting will be used in all subsequent calls to the [](sketch_text) function.  Note, however, that the leading is reset by [](sketch_text_size). For example, if the leading is set to 20 with `text_leading(20)`, then if `text_size(48)` is run at a later point, the leading will be reset to the default for the text size of 48.

Underlying Processing method: [textLeading](https://processing.org/reference/textLeading_.html)

## Signatures

```python
text_leading(
    leading: float,  # the size in pixels for spacing between lines
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
