# translate()

Specifies an amount to displace objects within the display window.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for translate()](/images/reference/Sketch_translate_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.translate(30, 20)
    py5.rect(0, 0, 55, 55)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for translate()](/images/reference/Sketch_translate_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    # translating in 3D requires P3D
    # as the parameter to size()
    # translate 30 across, 20 down, and
    # 50 back, or "away" from_ the screen.
    py5.translate(30, 20, -50)
    py5.rect(0, 0, 55, 55)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for translate()](/images/reference/Sketch_translate_2.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.rect(0, 0, 55, 55)  # draw rect at original 0,0
    py5.translate(30, 20)
    py5.rect(0, 0, 55, 55)  # draw rect at new 0,0
    py5.translate(14, 14)
    py5.rect(0, 0, 55, 55)  # draw rect at new 0,0
```

</div></div>

</div>

## Description

Specifies an amount to displace objects within the display window. The `x` parameter specifies left/right translation, the `y` parameter specifies up/down translation, and the `z` parameter specifies translations toward/away from the screen. Using this function with the `z` parameter requires using `P3D` as a parameter in combination with size as shown in the second example.

Transformations are cumulative and apply to everything that happens after and subsequent calls to the function accumulates the effect. For example, calling `translate(50, 0)` and then `translate(20, 0)` is the same as `translate(70, 0)`. If `translate()` is called within `draw()`, the transformation is reset when the loop begins again. This function can be further controlled by using [](sketch_push_matrix) and [](sketch_pop_matrix).

Underlying Processing method: [translate](https://processing.org/reference/translate_.html)

## Signatures

```python
translate(
    x: float,  # left/right translation
    y: float,  # up/down translation
    /,
) -> None

translate(
    x: float,  # left/right translation
    y: float,  # up/down translation
    z: float,  # forward/backward translation
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
