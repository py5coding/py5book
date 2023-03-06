# Py5Vector.normalize()

Normalize the vector by setting the vector's magnitude to 1.0.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
v1 = py5.Py5Vector(3, 4)

print("magnitude =", v1.mag)
# magnitude = 5.0

v1.normalize()

print("magnitude =", v1.mag)
# magnitude = 1.0
```

</div></div>

</div>

## Description

Normalize the vector by setting the vector's magnitude to 1.0. This method cannot be used on a vector of zeros, because a vector of zeros cannot be normalized.

## Signatures

```python
normalize() -> Py5Vector
```

Updated on March 06, 2023 02:49:26am UTC
