# print_projection()

Prints the current projection matrix to standard output.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.print_projection()

    # the program above prints this data:
    # 01.7321  00.0000  00.0000  00.0000
    # 00.0000 -01.7321  00.0000  00.0000
    # 00.0000  00.0000 -01.0202 -17.4955
    # 00.0000  00.0000 -01.0000  00.0000
```

</div></div>

</div>

## Description

Prints the current projection matrix to standard output.

Underlying Processing method: [printProjection](https://processing.org/reference/printProjection_.html)

## Signatures

```python
print_projection() -> None
```

Updated on March 06, 2023 02:49:26am UTC
