get_graphics()
==============

Get the :doc:`py5graphics` object used by the Sketch.

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
        py5.rect(10, 10, 50, 50)
        g = py5.get_graphics()
        py5.println(type(g))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Get the :doc:`py5graphics` object used by the Sketch. Internally, all of Processing's drawing functionality comes from interaction with PGraphics objects, and this will provide direct access to the PGraphics object used by the Sketch.

Underlying Processing method: getGraphics

Signatures
------

.. code:: python

    get_graphics() -> Py5Graphics
Updated on August 25, 2022 20:01:47pm UTC

