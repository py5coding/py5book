mouse_x
=======

The system variable ``mouse_x`` always contains the current horizontal coordinate of the mouse.

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
        py5.line(py5.mouse_x, 20, py5.mouse_x, 80)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The system variable ``mouse_x`` always contains the current horizontal coordinate of the mouse.

Note that py5 can only track the mouse position when the pointer is over the current window. The default value of ``mouse_x`` is ``0``, so ``0`` will be returned until the mouse moves in front of the Sketch window. (This typically happens when a Sketch is first run.)  Once the mouse moves away from the window, ``mouse_x`` will continue to report its most recent position.

Underlying Java field: `mouseX <https://processing.org/reference/mouseX.html>`_


Updated on September 11, 2021 16:51:34pm UTC

