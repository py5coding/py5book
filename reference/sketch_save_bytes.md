# save_bytes()

Save byte data to a file.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
mouse_x_history = list()
mouse_y_history = list()

def setup():
    # for this Sketch, the height and width must be less than 256
    py5.size(250, 250)
    py5.stroke_weight(10)


def draw():
    mouse_x_history.append(py5.mouse_x)
    mouse_y_history.append(py5.mouse_y)
    py5.point(py5.mouse_x, py5.mouse_y)
    if py5.frame_count == 600:
        py5.save_bytes(bytearray(mouse_x_history), 'data/mouse_x_positions.dat')
        py5.save_bytes(bytearray(mouse_y_history), 'data/mouse_y_positions.dat')
        py5.exit_sketch()
```

</div></div>

</div>

## Description

Save byte data to a file. If `filename` is not an absolute path, it will be saved relative to the current working directory ([](sketch_sketch_path)). The saved file can be reloaded with [](sketch_load_bytes).

Underlying Processing method: [saveBytes](https://processing.org/reference/saveBytes_.html)

## Signatures

```python
save_bytes(
    bytes_data: Union[bytes, bytearray],  # byte data to save in a file
    filename: Union[str, Path],  # filename to save byte data to
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
