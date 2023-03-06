# Py5Vector.set_mag()

Set the vector's magnitude.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
v1 = py5.Py5Vector(3, 4)

print("magnitude =", v1.mag)
# magnitude = 5.0

v1.set_mag(1)

print("magnitude =", v1.mag)
# magnitude = 1.0
```

</div></div>

</div>

## Description

Set the vector's magnitude. Setting this to a non-negative number will adjust the vector's magnitude to that value. Negative values will result in an error.

## Signatures

```python
set_mag(
    mag: float,  # vector magnitude
) -> Py5Vector
```

Updated on March 06, 2023 02:49:26am UTC
