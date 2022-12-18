load_strings()
==============

Load a list of strings from a file or URL.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        global mouse_x_positions, mouse_y_positions
        py5.size(250, 250)
        py5.stroke_weight(10)
        mouse_x_positions = py5.load_strings('mouse_x_positions.txt')
        mouse_y_positions = py5.load_strings('mouse_y_positions.txt')


    def draw():
        i = py5.frame_count
        if i < len(mouse_x_positions) and i < len(mouse_y_positions):
            py5.point(int(mouse_x_positions[i]), int(mouse_y_positions[i]))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Load a list of strings from a file or URL. When loading a file, the path can be in the data directory, relative to the current working directory (:doc:`sketch_sketch_path`), or an absolute path. When loading from a URL, the ``string_path`` parameter must start with ``http://`` or ``https://``.

When loading string data from a URL, the data is retrieved using the Python requests library with the ``get`` method, and any extra keyword arguments (the ``kwargs`` parameter) are passed along to that method. When loading string data from a file, the ``kwargs`` parameter is not used.

Underlying Processing method: `loadStrings <https://processing.org/reference/loadStrings_.html>`_

Signatures
----------

.. code:: python

    load_strings(
        string_path: Union[str, Path],  # url or file path for string data file
        **kwargs: dict[str, Any]
    ) -> list[str]

Updated on November 19, 2022 01:41:50am UTC

