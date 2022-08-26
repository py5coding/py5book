bezier_detail()
===============

Sets the resolution at which Beziers display.

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

    # move the mouse left and right to see the detail change

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.no_fill()


    def draw():
        py5.background(204)
        d = int(py5.remap(py5.mouse_x, 0, 100, 1, 20))
        py5.bezier_detail(d)
        py5.bezier(85, 20, 10, 10, 90, 90, 15, 80)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the resolution at which Beziers display. The default value is 20. This function is only useful when using the ``P3D`` renderer; the default ``P2D`` renderer does not use this information.

Underlying Processing method: `bezierDetail <https://processing.org/reference/bezierDetail_.html>`_

Signatures
------

.. code:: python

    bezier_detail(
        detail: int,  # resolution of the curves
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

