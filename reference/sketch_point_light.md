# point_light()

Adds a point light.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for point_light()](/images/reference/Sketch_point_light_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.background(0)
    py5.no_stroke()
    py5.point_light(51, 102, 126, 35, 40, 36)
    py5.translate(80, 50, 0)
    py5.sphere(30)
```

</div></div>

</div>

## Description

Adds a point light. Lights need to be included in the `draw()` to remain persistent in a looping program. Placing them in the `setup()` of a looping program will cause them to only have an effect the first time through the loop. The `v1`, `v2`, and `v3` parameters are interpreted as either RGB or HSB values, depending on the current color mode. The `x`, `y`, and `z` parameters set the position of the light.

Underlying Processing method: [pointLight](https://processing.org/reference/pointLight_.html)

## Signatures

```python
point_light(
    v1: float,  # red or hue value (depending on current color mode)
    v2: float,  # green or saturation value (depending on current color mode)
    v3: float,  # blue or brightness value (depending on current color mode)
    x: float,  # x-coordinate of the light
    y: float,  # y-coordinate of the light
    z: float,  # z-coordinate of the light
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
