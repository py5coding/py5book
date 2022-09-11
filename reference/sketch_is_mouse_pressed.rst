is_mouse_pressed
================

The ``is_mouse_pressed`` variable stores whether or not a mouse button is currently being pressed.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    # click within the image and press
    # the left and right mouse buttons to
    # change the value of the rectangle
    def draw():
        if py5.is_mouse_pressed and py5.mouse_button == py5.LEFT:
            py5.fill(0)
        elif py5.is_mouse_pressed and py5.mouse_button == py5.RIGHT:
            py5.fill(255)
        else:
            py5.fill(126)

        py5.rect(25, 25, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The ``is_mouse_pressed`` variable stores whether or not a mouse button is currently being pressed. The value is ``True`` when `any` mouse button is pressed, and ``False`` if no button is pressed. The :doc:`sketch_mouse_button` variable (see the related reference entry) can be used to determine which button has been pressed.

Updated on September 01, 2022 16:36:02pm UTC

