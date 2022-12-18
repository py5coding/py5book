pmouse_y
========

The system variable ``pmouse_y`` always contains the vertical position of the mouse in the frame previous to the current frame.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    # move the mouse quickly to see the difference
    # between the current and previous position
    def draw():
        py5.background(204)
        py5.line(20, py5.mouse_y, 80, py5.pmouse_y)
        py5.println(py5.mouse_y, ":", py5.pmouse_y)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The system variable ``pmouse_y`` always contains the vertical position of the mouse in the frame previous to the current frame.

For more detail on how ``pmouse_y`` is updated inside of mouse events and ``draw()``, see the reference for :doc:`sketch_pmouse_x`.

Underlying Processing field: `pmouseY <https://processing.org/reference/pmouseY.html>`_

Updated on September 01, 2022 16:36:02pm UTC

