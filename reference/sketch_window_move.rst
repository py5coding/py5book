window_move()
=============

Set the Sketch's window location.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    py5.run_sketch(block=False)
    # move the sketch window to the upper left corner of the display
    py5.window_move(0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    # this sketch will hide itself and reappear elsewhere on your display.
    def setup():
        global surface
        global visible
        surface = py5.get_surface()
        visible = True


    def draw():
        global visible
        if py5.frame_count % 250 == 0:
            # this negates the visible variable
            visible = not visible
            if visible:
                py5.window_move(py5.random_int(py5.display_width),
                                py5.random_int(py5.display_height))
            surface.set_visible(visible)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Set the Sketch's window location. Calling this repeatedly from the ``draw()`` function may result in a sluggish Sketch. Negative or invalid coordinates are ignored. To hide a Sketch window, use :doc:`py5surface_set_visible`.

This method provides the same functionality as :doc:`py5surface_set_location` but without the need to interact directly with the :doc:`py5surface` object.

Underlying Processing method: windowMove

Signatures
----------

.. code:: python

    window_move(
        x: int,  # x-coordinate for window location
        y: int,  # y-coordinate for window location
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

