println()
=========

Print text or other values to the screen.

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

    def draw():
        py5.square(py5.random_int(py5.width), py5.random_int(py5.height), 10)
        py5.println(f"frame count = {py5.frame_count}")

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Print text or other values to the screen. For a Sketch running outside of a Jupyter Notebook, this method will behave the same as the Python's builtin ``print`` method. For Sketches running in a Jupyter Notebook, this will place text in the output of the cell that made the :doc:`sketch_run_sketch` call.

When running a Sketch asynchronously through Jupyter Notebook, any ``print`` statements using Python's builtin function will always appear in the output of the currently active cell. This will rarely be desirable, as the active cell will keep changing as the user executes code elsewhere in the notebook. This method was created to provide users with print functionality in a Sketch without having to cope with output moving from one cell to the next.

Use :doc:`sketch_set_println_stream` to customize the behavior of ``println()``.

Syntax
------

.. code:: python

    println(*args, sep: str = ' ', end: str = '\n', stderr: bool = False) -> None

Parameters
----------

* **args**: - values to be printed
* **end**: `str = '\\n'` - string appended after the last value, defaults to newline character
* **sep**: `str = ' '` - string inserted between values, defaults to a space
* **stderr**: `bool = False` - use stderr instead of stdout


Updated on September 11, 2021 16:51:34pm UTC

