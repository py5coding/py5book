width
=====

System variable that stores the width of the display window.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_width_0.png
    :alt: example picture for width

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_stroke()
        py5.background(0)
        py5.rect(0, 40, py5.width, 20)
        py5.rect(0, 60, py5.width//2, 20)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

System variable that stores the width of the display window. This value is set by the first parameter of the :doc:`sketch_size` function. For example, the function call ``size(320, 240)`` sets the ``width`` variable to the value 320. The value of ``width`` defaults to 100 if :doc:`sketch_size` is not used in a program.

Underlying Java field: `width <https://processing.org/reference/width.html>`_


Updated on September 11, 2021 16:51:34pm UTC

