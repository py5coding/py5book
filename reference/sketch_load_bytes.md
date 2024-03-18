# load_bytes()

Load byte data from a file or URL.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global mouse_x_positions, mouse_y_positions
    py5.size(250, 250)
    py5.stroke_weight(10)
    mouse_x_positions = py5.load_bytes('mouse_x_positions.dat')
    mouse_y_positions = py5.load_bytes('mouse_y_positions.dat')


def draw():
    i = py5.frame_count
    if i < len(mouse_x_positions) and i < len(mouse_y_positions):
        py5.point(mouse_x_positions[i], mouse_y_positions[i])
```

</div></div>

</div>

## Description

Load byte data from a file or URL. When loading a file, the path can be in the data directory, relative to the current working directory ([](sketch_sketch_path)), or an absolute path. When loading from a URL, the `bytes_path` parameter must start with `http://` or `https://`.

When loading byte data from a URL, the data is retrieved using the Python requests library with the `get` method, and any extra keyword arguments (the `kwargs` parameter) are passed along to that method. When loading byte data from a file, the `kwargs` parameter is not used.

## Signatures

```python
load_bytes(
    bytes_path: Union[str, Path],  # url or file path for bytes data file
    **kwargs: dict[str, Any]
) -> bytearray
```

Updated on March 18, 2024 05:29:28am UTC
