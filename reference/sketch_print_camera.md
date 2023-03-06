# print_camera()

Prints the current camera matrix to standard output.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.print_camera()

    # the program above prints this data:
    # 01.0000  00.0000  00.0000 -50.0000
    # 00.0000  01.0000  00.0000 -50.0000
    # 00.0000  00.0000  01.0000 -86.6025
    # 00.0000  00.0000  00.0000  01.0000
```

</div></div>

</div>

## Description

Prints the current camera matrix to standard output.

Underlying Processing method: [printCamera](https://processing.org/reference/printCamera_.html)

## Signatures

```python
print_camera() -> None
```

Updated on March 06, 2023 02:49:26am UTC
