g
=

The :doc:`py5graphics` object used by the Sketch.

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

    def setup():
        py5.g.rect(10, 10, 50, 50)
        py5.println(type(py5.g))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The :doc:`py5graphics` object used by the Sketch. Internally, all of Processing's drawing functionality comes from interaction with PGraphics objects, and this will provide direct access to the PGraphics object used by the Sketch.

Underlying Processing field: g

Updated on August 25, 2022 20:01:47pm UTC

