save_json()
===========

Save JSON data to a file.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    data = dict(mouse_x=[], mouse_y=[])

    def draw():
        py5.point(py5.mouse_x, py5.mouse_y)
        if py5.frame_count % 60 == 0:
            data['mouse_x'].append(py5.mouse_x)
            data['mouse_y'].append(py5.mouse_y)
        if py5.frame_count == 600:
            py5.save_json(data, 'data/mouse_positions.json')
            py5.exit_sketch()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Save JSON data to a file. If ``filename`` is not an absolute path, it will be saved relative to the current working directory (:doc:`sketch_sketch_path`).

The JSON data is saved using the Python json library with the ``dump`` method, and the ``kwargs`` parameter is passed along to that method.

Syntax
------

.. code:: python

    save_json(json_data: Any, filename: Union[str, Path], **kwargs: dict[str, Any]) -> None

Parameters
----------

* **filename**: `Union[str, Path]` - filename to save JSON data object to
* **json_data**: `Any` - json data object
* **kwargs**: `dict[str, Any]` - keyword arguments


Updated on March 01, 2022 12:15:01pm UTC

