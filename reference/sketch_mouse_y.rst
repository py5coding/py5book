mouse_y
=======

The system variable ``mouse_y`` always contains the current vertical coordinate of the mouse.

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
        py5.background(204)
        py5.line(20, py5.mouse_y, 80, py5.mouse_y)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The system variable ``mouse_y`` always contains the current vertical coordinate of the mouse.

Note that py5 can only track the mouse position when the pointer is over the current window. The default value of ``mouse_y`` is ``0``, so ``0`` will be returned until the mouse moves in front of the Sketch window. (This typically happens when a Sketch is first run.)  Once the mouse moves away from the window, ``mouse_y`` will continue to report its most recent position.

Underlying Processing field: `mouseY <https://processing.org/reference/mouseY.html>`_


Updated on November 12, 2021 11:30:58am UTC

