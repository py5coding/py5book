# brightness()

Extracts the brightness value from a color.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for brightness()](/images/reference/Sketch_brightness_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.no_stroke()
    py5.color_mode(py5.HSB, 255)
    c = py5.color(0, 126, 255)
    py5.fill(c)
    py5.rect(15, 20, 35, 60)
    value = py5.brightness(c)  # sets 'value' to 255
    py5.fill(value)
    py5.rect(50, 20, 35, 60)
```

</div></div>

</div>

## Description

Extracts the brightness value from a color.

Underlying Processing method: [brightness](https://processing.org/reference/brightness_.html)

## Signatures

```python
brightness(
    rgb: int,  # any value of the color datatype
    /,
) -> float
```

Updated on March 06, 2023 02:49:26am UTC
