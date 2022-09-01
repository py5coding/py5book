full_screen()
=============

Open a Sketch using the full size of the computer's display.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    # run the code at the full dimensions of the screen currently
    # selected inside the preferences window

    x = 0


    def setup():
        py5.full_screen()
        py5.background(0)
        py5.no_stroke()
        py5.fill(102)


    def draw():
        global x
        py5.rect(x, py5.height*0.2, 1, py5.height*0.6)
        x = x + 2

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    # if more than one screen is attached to the computer, run the
    # code at the full dimensions on the screen defined by the
    # parameter to full_screen()

    x = 0


    def setup():
        py5.full_screen(2)
        py5.background(0)
        py5.no_stroke()
        py5.fill(102)


    def draw():
        global x
        py5.rect(x, py5.height*0.2, 1, py5.height*0.6)
        x = x + 2

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    # run full screen using the P2D renderer on screen 2

    x = 0


    def setup():
        py5.full_screen(py5.P2D, 2)
        py5.background(0)
        py5.no_stroke()
        py5.fill(102)


    def draw():
        global x
        py5.rect(x, py5.height*0.2, 1, py5.height*0.6)
        x = x + 2

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    # if more than one screen is attached to the computer, run the
    # code at the full dimensions across all of the attached screens

    x = 0


    def setup():
        py5.full_screen(py5.P2D, py5.SPAN)
        py5.background(0)
        py5.no_stroke()
        py5.fill(102)


    def draw():
        global x
        py5.rect(x, py5.height*0.2, 1, py5.height*0.6)
        x = x + 2

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Open a Sketch using the full size of the computer's display. This is intended to be called from the ``settings()`` function. The :doc:`sketch_size` and ``full_screen()`` functions cannot both be used in the same program.

When programming in module mode and imported mode, py5 will allow calls to ``full_screen()`` from the ``setup()`` function if it is called at the beginning of ``setup()``. This allows the user to omit the ``settings()`` function, much like what can be done while programming in the Processing IDE. Py5 does this by inspecting the ``setup()`` function and attempting to split it into synthetic ``settings()`` and ``setup()`` functions if both were not created by the user and the real ``setup()`` function contains a call to ``full_screen()``, or calls to :doc:`sketch_size`, :doc:`sketch_smooth`, :doc:`sketch_no_smooth`, or :doc:`sketch_pixel_density`. Calls to those functions must be at the very beginning of ``setup()``, before any other Python code (but comments are ok). This feature is not available when programming in class mode.

When ``full_screen()`` is used without a parameter on a computer with multiple monitors, it will (probably) draw the Sketch to the primary display. When it is used with a single parameter, this number defines the screen to display to program on (e.g. 1, 2, 3...). When used with two parameters, the first defines the renderer to use (e.g. P2D) and the second defines the screen. The ``SPAN`` parameter can be used in place of a screen number to draw the Sketch as a full-screen window across all of the attached displays if there are more than one.

Underlying Processing method: `fullScreen <https://processing.org/reference/fullScreen_.html>`_

Signatures
----------

.. code:: python

    full_screen() -> None

    full_screen(
        display: int,  # the screen to run the Sketch on (1, 2, 3, etc. or on multiple screens using SPAN)
        /,
    ) -> None

    full_screen(
        renderer: str,  # the renderer to use, e.g. P2D, P3D, JAVA2D (default)
        /,
    ) -> None

    full_screen(
        renderer: str,  # the renderer to use, e.g. P2D, P3D, JAVA2D (default)
        display: int,  # the screen to run the Sketch on (1, 2, 3, etc. or on multiple screens using SPAN)
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

