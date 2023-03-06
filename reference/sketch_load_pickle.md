# load_pickle()

Load a pickled Python object from a file.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global mouse_x_positions, mouse_y_positions
    py5.size(250, 250)
    py5.stroke_weight(10)
    data = py5.load_pickle('mouse_positions.pkl')
    mouse_x_positions = data['mouse_x']
    mouse_y_positions = data['mouse_y']


def draw():
    i = py5.frame_count
    if i < len(mouse_x_positions) and i < len(mouse_y_positions):
        py5.point(mouse_x_positions[i], mouse_y_positions[i])
```

</div></div>

</div>

## Description

Load a pickled Python object from a file. The path can be in the data directory, relative to the current working directory ([](sketch_sketch_path)), or an absolute path.

There are security risks associated with Python pickle files. A pickle file can contain malicious code, so never load a pickle file from an untrusted source.

Underlying Processing method: loadPickle

## Signatures

```python
load_pickle(
    pickle_path: Union[str, Path]  # file path for pickle object file
) -> Any
```

Updated on March 06, 2023 02:49:26am UTC
