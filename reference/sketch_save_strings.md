# save_strings()

Save a list of strings to a file.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
mouse_x_history = list()
mouse_y_history = list()

def setup():
    py5.size(250, 250)
    py5.stroke_weight(10)


def draw():
    mouse_x_history.append(py5.mouse_x)
    mouse_y_history.append(py5.mouse_y)
    py5.point(py5.mouse_x, py5.mouse_y)
    if py5.frame_count == 600:
        py5.save_strings(mouse_x_history, 'data/mouse_x_positions.txt')
        py5.save_strings(mouse_y_history, 'data/mouse_y_positions.txt')
        py5.exit_sketch()
```

</div></div>

</div>

## Description

Save a list of strings to a file. If `filename` is not an absolute path, it will be saved relative to the current working directory ([](sketch_sketch_path)). If the contents of the list are not already strings, it will be converted to strings with the Python builtin `str`. The saved file can be reloaded with [](sketch_load_strings).

Use the `end` parameter to set the line terminator for each string in the list. If items in the list of strings already have line terminators, set the `end` parameter to `''` to keep the output file from being saved with a blank line after each item.

## Signatures

```python
save_strings(
    string_data: list[str],  # string data to save in a file
    filename: Union[str, Path],  # filename to save string data to
    *,
    end: str = "\n"  # line terminator for each string
) -> None
```

Updated on March 18, 2024 05:29:28am UTC
