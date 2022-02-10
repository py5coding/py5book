window_size()
=============

Set a new width and height for the Sketch window.

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
        py5.square(py5.random(py5.width), py5.random(py5.height), 10)

    py5.run_sketch(block=False)

    # while the sketch is running, change the window size
    py5.window_size(400, 400)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Set a new width and height for the Sketch window. You do not need to call :doc:`sketch_window_resizable` before calling this.

Changing the window size will clear the drawing canvas. If you do this, the :doc:`sketch_width` and :doc:`sketch_height` variables will change.

This method provides the same funcationality as :doc:`py5surface_set_size` but without the need to interact directly with the :doc:`py5surface` object.

Underlying Processing method: windowSize

Syntax
------

.. code:: python

    window_size(new_width: int, new_height: int, /) -> None

Parameters
----------

* **new_height**: `int` - new window height
* **new_width**: `int` - new window width


Updated on February 10, 2022 17:53:43pm UTC

