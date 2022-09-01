Py5Surface.set_visible()
========================

Set the Sketch window's visiblity.

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
        py5.println(py5.frame_count)

    py5.run_sketch(block=False)
    surface = py5.get_surface()

    # hide the sketch.
    surface.set_visible(False)
    # the sketch is no longer visible but there is still output

    # after waiting a bit, make the sketch visible again
    surface.set_visible(True)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

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
                surface.set_location(py5.random_int(py5.display_width),
                                     py5.random_int(py5.display_height))
            surface.set_visible(visible)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Set the Sketch window's visiblity. The animation will continue to run but the window will not be visible.

Underlying Processing method: PSurface.setVisible

Signatures
----------

.. code:: python

    set_visible(
        visible: bool,  # desired surface visiblity
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

