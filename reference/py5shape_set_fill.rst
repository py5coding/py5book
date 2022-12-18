Py5Shape.set_fill()
===================

The ``set_fill()`` method defines the fill color of a ``Py5Shape``.

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
        global c
        py5.size(640, 360, py5.P2D)
        c = py5.create_shape(py5.RECT, -20, -20, 40, 40)
        c.set_stroke("#FFFFFF")


    def draw():
        py5.background(51)
        c.set_fill(py5.color(py5.random_int(255)))
        py5.translate(py5.mouse_x, py5.mouse_y)
        py5.shape(c)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The ``set_fill()`` method defines the fill color of a ``Py5Shape``. This method is used after shapes are created or when a shape is defined explicitly (e.g. ``create_shape(RECT, 20, 20, 60, 60)``) as shown in the example. When a shape is created with :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape`, its attributes may be changed with :doc:`py5shape_fill` and :doc:`py5shape_stroke` between the calls to :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape`. However, after the shape is created, only the ``set_fill()`` method can define a new fill value for the ``Py5Shape``.

Underlying Processing method: `PShape.setFill <https://processing.org/reference/PShape_setFill_.html>`_

Signatures
----------

.. code:: python

    set_fill(
        fill: bool,  # allow fill
        /,
    ) -> None

    set_fill(
        fill: int,  # any color value
        /,
    ) -> None

    set_fill(
        index: int,  # vertex index
        fill: int,  # any color value
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

