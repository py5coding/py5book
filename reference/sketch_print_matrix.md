# print_matrix()

Prints the current matrix to standard output.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.print_matrix()
    # prints:
    # 01.0000  00.0000  00.0000 -50.0000
    # 00.0000  01.0000  00.0000 -50.0000
    # 00.0000  00.0000  01.0000 -86.6025
    # 00.0000  00.0000  00.0000  01.0000

    py5.reset_matrix()
    py5.print_matrix()
    # prints:
    # 1.0000  0.0000  0.0000  0.0000
    # 0.0000  1.0000  0.0000  0.0000
    # 0.0000  0.0000  1.0000  0.0000
    # 0.0000  0.0000  0.0000  1.0000
```

</div></div>

</div>

## Description

Prints the current matrix to standard output.

Underlying Processing method: [printMatrix](https://processing.org/reference/printMatrix_.html)

## Signatures

```python
print_matrix() -> None
```

Updated on March 06, 2023 02:49:26am UTC
