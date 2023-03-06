# shininess()

Sets the amount of gloss in the surface of shapes.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for shininess()](/images/reference/Sketch_shininess_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.background(0)
    py5.no_stroke()
    py5.background(0)
    py5.fill(0, 51, 102)
    py5.ambient_light(102, 102, 102)
    py5.light_specular(204, 204, 204)
    py5.directional_light(102, 102, 102, 0, 0, -1)
    py5.specular(255, 255, 255)
    py5.translate(30, 50, 0)
    py5.shininess(1.0)
    py5.sphere(20)  # left sphere
    py5.translate(40, 0, 0)
    py5.shininess(5.0)
    py5.sphere(20)  # right sphere
```

</div></div>

</div>

## Description

Sets the amount of gloss in the surface of shapes. Use in combination with [](sketch_ambient), [](sketch_specular), and [](sketch_emissive) to set the material properties of shapes.

Underlying Processing method: [shininess](https://processing.org/reference/shininess_.html)

## Signatures

```python
shininess(
    shine: float,  # degree of shininess
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
