window_x
========

The x-coordinate of the current window location.

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

    def draw():
        py5.rect(py5.random(py5.width), py5.random(py5.height), 10, 10)
        py5.println(f'Sketch window location is ({py5.window_x}, {py5.window_y})')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The x-coordinate of the current window location. The location is measured from the Sketch window's upper left corner.

Underlying Processing field: windowX


Updated on February 11, 2022 23:19:53pm UTC

