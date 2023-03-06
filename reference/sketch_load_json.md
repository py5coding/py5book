# load_json()

Load a JSON data file from a file or URL.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for load_json()](/images/reference/Sketch_load_json_0.png)

</div><div class="example-cell-code">

```python
def setup():
    data = py5.load_json('colors.json')
    py5.fill(data['red'], data['green'], data['blue'])
    py5.rect(10, 10, 80, 80)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global mouse_x_positions, mouse_y_positions
    py5.size(250, 250)
    py5.stroke_weight(10)
    data = py5.load_json('mouse_positions.json')
    mouse_x_positions = data['mouse_x']
    mouse_y_positions = data['mouse_y']


def draw():
    i = py5.frame_count
    if i < len(mouse_x_positions) and i < len(mouse_y_positions):
        py5.point(mouse_x_positions[i], mouse_y_positions[i])
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global promise
    py5.size(200, 100)
    promise = py5.launch_promise_thread(load_data)


def load_data():
    return py5.load_json('http://py5coding.org/files/secret_message.json')


def draw():
    py5.background(0)
    if promise.is_ready:
        py5.text(promise.result['msg'][:(py5.frame_count // 25)], 20, 50)
```

</div></div>

</div>

## Description

Load a JSON data file from a file or URL. When loading a file, the path can be in the data directory, relative to the current working directory ([](sketch_sketch_path)), or an absolute path. When loading from a URL, the `json_path` parameter must start with `http://` or `https://`.

When loading JSON data from a URL, the data is retrieved using the Python requests library with the `get` method, and any extra keyword arguments (the `kwargs` parameter) are passed along to that method. When loading JSON data from a file, the data is loaded using the Python json library with the `load` method, and again any extra keyword arguments are passed along to that method.

## Signatures

```python
load_json(
    json_path: Union[str, Path],  # url or file path for JSON data file
    **kwargs: dict[str, Any]
) -> Any
```

Updated on March 06, 2023 02:49:26am UTC
