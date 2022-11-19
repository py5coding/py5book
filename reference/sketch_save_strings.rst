save_strings()
==============

Save a list of strings to a file.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

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

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Save a list of strings to a file. If ``filename`` is not an absolute path, it will be saved relative to the current working directory (:doc:`sketch_sketch_path`). If the contents of the list are not already strings, it will be converted to strings with the Python builtin ``str``. The saved file can be reloaded with :doc:`sketch_load_strings`.

Use the ``end`` parameter to set the line terminator for each string in the list. If items in the list of strings already have line terminators, set the ``end`` parameter to ``''`` to keep the output file from being saved with a blank line after each item.

Underlying Processing method: `saveStrings <https://processing.org/reference/saveStrings_.html>`_

Signatures
----------

.. code:: python

    save_strings(
        string_data: list[str],  # string data to save in a file
        filename: Union[str, Path],  # filename to save string data to
        *,
        end: str = "\n"  # line terminator for each string
    ) -> None

Updated on November 19, 2022 01:41:50am UTC

