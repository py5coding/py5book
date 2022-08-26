curve_detail()
==============

Sets the resolution at which curves display.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_curve_detail_0.png
    :alt: example picture for curve_detail()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.no_fill()


    def draw():
        py5.curve_detail(1)
        draw_curves(-15)
        py5.stroke(126)
        py5.curve_detail(2)
        draw_curves(0)
        py5.stroke(255)
        py5.curve_detail(4)
        draw_curves(15)


    def draw_curves(y):
        py5.curve(5, 28+y, 5, 28+y, 73, 26+y, 73, 63+y)
        py5.curve(5, 28+y, 73, 26+y, 73, 63+y, 15, 67+y)
        py5.curve(73, 26+y, 73, 63+y, 15, 67+y, 15, 67+y)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the resolution at which curves display. The default value is 20. This function is only useful when using the ``P3D`` renderer as the default ``P2D`` renderer does not use this information.

Underlying Processing method: `curveDetail <https://processing.org/reference/curveDetail_.html>`_

Signatures
------

.. code:: python

    curve_detail(
        detail: int,  # resolution of the curves
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

