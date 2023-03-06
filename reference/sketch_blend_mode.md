# blend_mode()

Blends the pixels in the display window according to a defined mode.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.background(0)
    py5.blend_mode(py5.ADD)
    py5.stroke(102)
    py5.stroke_weight(30)
    py5.line(25, 25, 75, 75)
    py5.line(75, 25, 25, 75)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P2D)
    py5.blend_mode(py5.MULTIPLY)
    py5.stroke(51)
    py5.stroke_weight(30)
    py5.line(25, 25, 75, 75)
    py5.line(75, 25, 25, 75)
```

</div></div>

</div>

## Description

Blends the pixels in the display window according to a defined mode. There is a choice of the following modes to blend the source pixels (A) with the ones of pixels already in the display window (B). Each pixel's final color is the result of applying one of the blend modes with each channel of (A) and (B) independently. The red channel is compared with red, green with green, and blue with blue.

* BLEND: linear interpolation of colors: `C = A*factor + B`. This is the default.
* ADD: additive blending with white clip: `C = min(A*factor + B, 255)`
* SUBTRACT: subtractive blending with black clip: `C = max(B - A*factor, 0)`
* DARKEST: only the darkest color succeeds: `C = min(A*factor, B)`
* LIGHTEST: only the lightest color succeeds: `C = max(A*factor, B)`
* DIFFERENCE: subtract colors from underlying image.
* EXCLUSION: similar to DIFFERENCE, but less extreme.
* MULTIPLY: multiply the colors, result will always be darker.
* SCREEN: opposite multiply, uses inverse values of the colors.
* REPLACE: the pixels entirely replace the others and don't utilize alpha (transparency) values

We recommend using `blend_mode()` and not the previous [](sketch_blend) function. However, unlike [](sketch_blend), the `blend_mode()` function does not support the following: `HARD_LIGHT`, `SOFT_LIGHT`, `OVERLAY`, `DODGE`, `BURN`. On older hardware, the `LIGHTEST`, `DARKEST`, and `DIFFERENCE` modes might not be available as well.

Underlying Processing method: [blendMode](https://processing.org/reference/blendMode_.html)

## Signatures

```python
blend_mode(
    mode: int,  # the blending mode to use
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
