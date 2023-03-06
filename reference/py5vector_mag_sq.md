# Py5Vector.mag_sq

The square of the vector's magnitude.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
v1 = py5.Py5Vector(3, 4)

print("magnitude =", v1.mag)
# magnitude = 5.0
print("magnitude squared =", v1.mag_sq)
# magnitude squared = 25.0

v1.mag_sq = 100

print("magnitude =", v1.mag)
# magnitude = 10.0
print("magnitude squared =", v1.mag_sq)
# magnitude squared = 100.0
```

</div></div>

</div>

## Description

The square of the vector's magnitude. Setting this property to a non-negative number will adjust the vector's squared magnitude to that value. Negative values will result in an error.

Updated on March 06, 2023 02:49:26am UTC
