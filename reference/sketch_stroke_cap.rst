stroke_cap()
============

Sets the style for rendering line endings.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_stroke_cap_0.png
    :alt: example picture for stroke_cap()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.stroke_weight(12.0)
        py5.stroke_cap(py5.ROUND)
        py5.line(20, 30, 80, 30)
        py5.stroke_cap(py5.SQUARE)
        py5.line(20, 50, 80, 50)
        py5.stroke_cap(py5.PROJECT)
        py5.line(20, 70, 80, 70)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the style for rendering line endings. These ends are either squared, extended, or rounded, each of which specified with the corresponding parameters: ``SQUARE``, ``PROJECT``, and ``ROUND``. The default cap is ``ROUND``.

To make :doc:`sketch_point` appear square, use ``stroke_cap(PROJECT)``. Using ``stroke_cap(SQUARE)`` (no cap) causes points to become invisible.

Underlying Processing method: `strokeCap <https://processing.org/reference/strokeCap_.html>`_

Signatures
----------

.. code:: python

    stroke_cap(
        cap: int,  # either SQUARE, PROJECT, or ROUND
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

