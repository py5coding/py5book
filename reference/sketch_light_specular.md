# light_specular()

Sets the specular color for lights.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for light_specular()](/images/reference/Sketch_light_specular_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.background(0)
    py5.no_stroke()
    py5.directional_light(102, 102, 102, 0, 0, -1)
    py5.light_specular(204, 204, 204)
    py5.directional_light(102, 102, 102, 0, 1, -1)
    py5.light_specular(102, 102, 102)
    py5.translate(20, 50, 0)
    py5.specular(51, 51, 51)
    py5.sphere(30)
    py5.translate(60, 0, 0)
    py5.specular(102, 102, 102)
    py5.sphere(30)
```

</div></div>

</div>

## Description

Sets the specular color for lights. Like [](sketch_fill), it affects only the elements which are created after it in the code. Specular refers to light which bounces off a surface in a preferred direction (rather than bouncing in all directions like a diffuse light) and is used for creating highlights. The specular quality of a light interacts with the specular material qualities set through the [](sketch_specular) and [](sketch_shininess) functions.

Underlying Processing method: [lightSpecular](https://processing.org/reference/lightSpecular_.html)

## Signatures

```python
light_specular(
    v1: float,  # red or hue value (depending on current color mode)
    v2: float,  # green or saturation value (depending on current color mode)
    v3: float,  # blue or brightness value (depending on current color mode)
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
