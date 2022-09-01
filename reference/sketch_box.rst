box()
=====

A box is an extruded rectangle.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_box_0.png
    :alt: example picture for box()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.translate(58, 48, 0)
        py5.rotate_y(0.5)
        py5.no_fill()
        py5.box(40)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_box_1.png
    :alt: example picture for box()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.translate(58, 48, 0)
        py5.rotate_y(0.5)
        py5.no_fill()
        py5.box(40, 20, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

A box is an extruded rectangle. A box with equal dimensions on all sides is a cube.

Underlying Processing method: `box <https://processing.org/reference/box_.html>`_

Signatures
----------

.. code:: python

    box(
        size: float,  # dimension of the box in all dimensions (creates a cube)
        /,
    ) -> None

    box(
        w: float,  # dimension of the box in the x-dimension
        h: float,  # dimension of the box in the y-dimension
        d: float,  # dimension of the box in the z-dimension
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

