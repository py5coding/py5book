display_height
==============

System variable that stores the height of the entire screen display.

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

System variable that stores the height of the entire screen display. This can be used to run a full-screen program on any display size, but calling :doc:`sketch_full_screen` is usually a better choice.

Underlying Processing field: `displayHeight <https://processing.org/reference/displayHeight.html>`_

Updated on August 25, 2022 20:01:47pm UTC

