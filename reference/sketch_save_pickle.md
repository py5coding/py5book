# save_pickle()

Pickle a Python object to a file.

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
        py5.save_pickle(data, 'data/mouse_positions.pkl')
        py5.exit_sketch()
```

</div></div>

</div>

## Description

Pickle a Python object to a file. If `filename` is not an absolute path, it will be saved relative to the current working directory ([](sketch_sketch_path)). The saved file can be reloaded with [](sketch_load_pickle).

Object "pickling" is a technique for serializing objects and saving them to a file for later retrieval. The recreated objects will be clones of the original objects. Not all Python objects can be saved to a Python pickle file. This limitation prevents any py5 object from being pickled.

When using py5 in [imported mode](content-py5-modes-imported-mode), pickling will not work on objects instantiated from new classes you have defined yourself on the main sketch file. This applies to py5's `save_pickle()` and [](sketch_load_pickle) methods, as well as the Python's standard library pickle module methods they depend upon. If you need to pickle objects from classes you defined, move the class definitions to a different .py file that you import as a module or import the classes from. Otherwise, you could also try using [module mode](content-py5-modes-module-mode) if you want to use pickle with your classes and keep all the sketch code in a single file.

## Signatures

```python
save_pickle(
    obj: Any,  # any non-py5 Python object
    filename: Union[str, Path],  # filename to save pickled object to
) -> None
```

Updated on March 18, 2024 05:24:22am UTC
