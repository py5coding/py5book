no_cursor()
===========

Hides the cursor from view.

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

    # press the mouse to hide the cursor
    def draw():
        if py5.is_mouse_pressed:
            py5.no_cursor()
        else:
            py5.cursor(py5.HAND)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Hides the cursor from view. Will not work when running the program in full screen (Present) mode.

Underlying Processing method: `noCursor <https://processing.org/reference/noCursor_.html>`_

Signatures
------

.. code:: python

    no_cursor() -> None
Updated on August 25, 2022 20:01:47pm UTC

