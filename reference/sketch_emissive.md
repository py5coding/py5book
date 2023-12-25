# emissive()

Sets the emissive color of the material used for drawing shapes drawn to the screen.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for emissive()](/images/reference/Sketch_emissive_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.background(0)
    py5.no_stroke()
    py5.background(0)
    py5.directional_light(204, 204, 204, .5, 0, -1)
    py5.emissive(0, 26, 51)
    py5.translate(70, 50, 0)
    py5.sphere(30)
```

</div></div>

</div>

## Description

Sets the emissive color of the material used for drawing shapes drawn to the screen. Use in combination with [](sketch_ambient), [](sketch_specular), and [](sketch_shininess) to set the material properties of shapes.

This method has additional color functionality that is not reflected in the method's signatures. For example, you can pass the name of a color (e.g. "green", "mediumpurple", etc). Look at the online ["All About Colors"](/integrations/colors) Python Ecosystem Integration tutorial for more information.

Underlying Processing method: [emissive](https://processing.org/reference/emissive_.html)

## Signatures

```python
emissive(
    gray: float,  # value between black and white, by default 0 to 255
    /,
) -> None

emissive(
    rgb: int,  # color to set
    /,
) -> None

emissive(
    v1: float,  # red or hue value (depending on current color mode)
    v2: float,  # green or saturation value (depending on current color mode)
    v3: float,  # blue or brightness value (depending on current color mode)
    /,
) -> None
```

Updated on December 25, 2023 16:36:33pm UTC
