display_width
=============

System variable that stores the width of the entire screen display.

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
        py5.size(py5.display_width, py5.display_height)
        py5.line(0, 0, py5.width, py5.height)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

System variable that stores the width of the entire screen display. This can be used to run a full-screen program on any display size, but calling :doc:`sketch_full_screen` is usually a better choice.

Underlying Processing field: `displayWidth <https://processing.org/reference/displayWidth.html>`_


Updated on November 12, 2021 11:30:58am UTC

