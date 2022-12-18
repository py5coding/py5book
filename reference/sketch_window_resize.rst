window_resize()
===============

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

    def draw():
        py5.square(py5.random(py5.width), py5.random(py5.height), 10)

    py5.run_sketch(block=False)

    # while the sketch is running, change the window size
    py5.window_resize(400, 400)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Set a new width and height for the Sketch window. You do not need to call :doc:`sketch_window_resizable` before calling this.

Changing the window size will clear the drawing canvas. If you do this, the :doc:`sketch_width` and :doc:`sketch_height` variables will change.

This method provides the same functionality as :doc:`py5surface_set_size` but without the need to interact directly with the :doc:`py5surface` object.

Underlying Processing method: windowResize

Signatures
----------

.. code:: python

    window_resize(
        new_width: int,  # new window width
        new_height: int,  # new window height
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

