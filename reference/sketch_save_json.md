# save_json()

Save JSON data to a file.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
data = dict(mouse_x=[], mouse_y=[])

def setup():
    py5.size(250, 250)
    py5.stroke_weight(10)


def draw():
    data['mouse_x'].append(py5.mouse_x)
    data['mouse_y'].append(py5.mouse_y)
    py5.point(py5.mouse_x, py5.mouse_y)
    if py5.frame_count == 600:
        py5.save_json(data, 'data/mouse_positions.json')
        py5.exit_sketch()
```

</div></div>

</div>

## Description

Save JSON data to a file. If `filename` is not an absolute path, it will be saved relative to the current working directory ([](sketch_sketch_path)). The saved file can be reloaded with [](sketch_load_json).

The JSON data is saved using the Python json library with the `dump` method, and the `kwargs` parameter is passed along to that method.

## Signatures

```python
save_json(
    json_data: Any,  # json data object
    filename: Union[str, Path],  # filename to save JSON data object to
    **kwargs: dict[str, Any]
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
