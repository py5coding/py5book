# Py5Vector.norm

Normalized copy of the vector.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
v1 = py5.Py5Vector(40, 0)
v2 = py5.Py5Vector(50, 50)

print(v1)
# Py5Vector2D(40., 0.)
print(v1.norm)
# Py5Vector2D(1., 0.)
print(v2)
# Py5Vector2D(50., 50.)
print(v2.norm)
# Py5Vector2D(0.70710678, 0.70710678)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global v1
    v1 = py5.Py5Vector(40, 0)


def draw():
    py5.background(255)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.stroke(0)
    py5.stroke_weight(4)
    py5.line(0, 0, v1.x, v1.y)
    vm = py5.Py5Vector(py5.mouse_x - py5.width / 2, py5.mouse_y - py5.height / 2)
    py5.stroke_weight(2)
    py5.stroke(0, 255, 0)
    py5.line(0, 0, vm.x, vm.y)
    v2 = v1.norm.dot(vm) * v1.norm
    py5.stroke(255, 0, 0)
    py5.line(0, 0, v2.x, v2.y)
```

</div></div>

</div>

## Description

Normalized copy of the vector. The normalized copy will have a magnitude of 1.0. This property cannot be used on a vector of zeros, because a vector of zeros cannot be normalized.

Updated on March 06, 2023 02:49:26am UTC
