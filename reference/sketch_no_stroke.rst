no_stroke()
===========

Disables drawing the stroke (outline).

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_no_stroke_0.png
    :alt: example picture for no_stroke()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.no_stroke()
        py5.rect(30, 20, 55, 55)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Disables drawing the stroke (outline). If both ``no_stroke()`` and :doc:`sketch_no_fill` are called, nothing will be drawn to the screen.

Underlying Processing method: `noStroke <https://processing.org/reference/noStroke_.html>`_

Signatures
----------

.. code:: python

    no_stroke() -> None

Updated on September 01, 2022 16:36:02pm UTC

