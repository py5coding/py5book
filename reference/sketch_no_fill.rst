no_fill()
=========

Disables filling geometry.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_no_fill_0.png
    :alt: example picture for no_fill()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.rect(15, 10, 55, 55)
        py5.no_fill()
        py5.rect(30, 20, 55, 55)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Disables filling geometry. If both :doc:`sketch_no_stroke` and ``no_fill()`` are called, nothing will be drawn to the screen.

Underlying Processing method: `noFill <https://processing.org/reference/noFill_.html>`_

Signatures
----------

.. code:: python

    no_fill() -> None
Updated on September 01, 2022 12:53:02pm UTC

