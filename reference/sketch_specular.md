# specular()

Sets the specular color of the materials used for shapes drawn to the screen, which sets the color of highlights.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for specular()](/images/reference/Sketch_specular_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.background(0)
    py5.no_stroke()
    py5.background(0)
    py5.fill(0, 51, 102)
    py5.light_specular(255, 255, 255)
    py5.directional_light(204, 204, 204, 0, 0, -1)
    py5.translate(20, 50, 0)
    py5.specular(255, 255, 255)
    py5.sphere(30)
    py5.translate(60, 0, 0)
    py5.specular(204, 102, 0)
    py5.sphere(30)
```

</div></div>

</div>

## Description

Sets the specular color of the materials used for shapes drawn to the screen, which sets the color of highlights. Specular refers to light which bounces off a surface in a preferred direction (rather than bouncing in all directions like a diffuse light). Use in combination with [](sketch_emissive), [](sketch_ambient), and [](sketch_shininess) to set the material properties of shapes.

This method has additional color functionality that is not reflected in the method's signatures. For example, you can pass the name of a color (e.g. "green", "mediumpurple", etc). Look at the online ["All About Colors"](/integrations/colors) Python Ecosystem Integration tutorial for more information.

Underlying Processing method: [specular](https://processing.org/reference/specular_.html)

## Signatures

```python
specular(
    gray: float,  # value between black and white, by default 0 to 255
    /,
) -> None

specular(
    rgb: int,  # color to set
    /,
) -> None

specular(
    v1: float,  # red or hue value (depending on current color mode)
    v2: float,  # green or saturation value (depending on current color mode)
    v3: float,  # blue or brightness value (depending on current color mode)
    /,
) -> None
```

Updated on December 25, 2023 16:36:33pm UTC
