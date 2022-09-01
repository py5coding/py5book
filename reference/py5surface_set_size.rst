Py5Surface.set_size()
=====================

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

    # while the sketch is running, get the surface and change the size
    surface = py5.get_surface()
    surface.set_size(400, 400)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Set a new width and height for the Sketch window. You do not need to call :doc:`py5surface_set_resizable` before calling this.

Changing the window size will clear the drawing canvas. If you do this, the :doc:`sketch_width` and :doc:`sketch_height` variables will change.

This method provides the same functionality as :doc:`sketch_window_resize`.

Underlying Processing method: PSurface.setSize

Signatures
----------

.. code:: python

    set_size(
        width: int,  # new window width
        height: int,  # new window height
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

