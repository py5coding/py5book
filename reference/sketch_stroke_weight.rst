stroke_weight()
===============

Sets the width of the stroke used for lines, points, and the border around shapes.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_stroke_weight_0.png
    :alt: example picture for stroke_weight()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.stroke_weight(1)  # default
        py5.line(20, 20, 80, 20)
        py5.stroke_weight(4)  # thicker
        py5.line(20, 40, 80, 40)
        py5.stroke_weight(10)  # beastly
        py5.line(20, 70, 80, 70)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the width of the stroke used for lines, points, and the border around shapes. All widths are set in units of pixels.

Using :doc:`sketch_point` with ``strokeWeight(1)`` or smaller may draw nothing to the screen, depending on the graphics settings of the computer. Workarounds include setting the pixel using the :doc:`sketch_pixels` or :doc:`sketch_np_pixels` arrays or drawing the point using either :doc:`sketch_circle` or :doc:`sketch_square`.

Underlying Processing method: `strokeWeight <https://processing.org/reference/strokeWeight_.html>`_

Signatures
----------

.. code:: python

    stroke_weight(
        weight: float,  # the weight (in pixels) of the stroke
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

