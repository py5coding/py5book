ellipse()
=========

Draws an ellipse (oval) to the screen.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_ellipse_0.png
    :alt: example picture for ellipse()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.ellipse(56, 46, 55, 55)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Draws an ellipse (oval) to the screen. An ellipse with equal width and height is a circle. By default, the first two parameters set the location, and the third and fourth parameters set the shape's width and height. The origin may be changed with the :doc:`sketch_ellipse_mode` function.

Underlying Processing method: `ellipse <https://processing.org/reference/ellipse_.html>`_

Signatures
----------

.. code:: python

    ellipse(
        a: float,  # x-coordinate of the ellipse
        b: float,  # y-coordinate of the ellipse
        c: float,  # width of the ellipse by default
        d: float,  # height of the ellipse by default
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

