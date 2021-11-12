smooth()
========

Draws all geometry with smooth (anti-aliased) edges.

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
        py5.smooth(2)
        py5.no_stroke()


    def draw():
        py5.background(0)
        py5.ellipse(30, 48, 36, 36)
        py5.ellipse(70, 48, 36, 36)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    x = 0

    def setup():
        py5.full_screen(py5.P2D, py5.SPAN)
        py5.smooth(4)


    def draw():
        global x
        py5.background(0)
        py5.ellipse(x, py5.height//2, py5.height/4, py5.height/4)
        x += 1

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Draws all geometry with smooth (anti-aliased) edges. This behavior is the default, so ``smooth()`` only needs to be used when a program needs to set the smoothing in a different way. The ``level`` parameter increases the amount of smoothness. This is the level of over sampling applied to the graphics buffer.

With the ``P2D`` and ``P3D`` renderers, ``smooth(2)`` is the default, this is called "2x anti-aliasing." The code ``smooth(4)`` is used for 4x anti-aliasing and ``smooth(8)`` is specified for "8x anti-aliasing." The maximum anti-aliasing level is determined by the hardware of the machine that is running the software, so ``smooth(4)`` and ``smooth(8)`` will not work with every computer.

The default renderer uses ``smooth(3)`` by default. This is bicubic smoothing. The other option for the default renderer is ``smooth(2)``, which is bilinear smoothing.

The ``smooth()`` function can only be set once within a Sketch. It is intended to be called from the ``settings()`` function. The :doc:`sketch_no_smooth` function follows the same rules.

When programming in module mode and imported mode, py5 will allow calls to ``smooth()`` from the ``setup()`` function if it is called at the beginning of ``setup()``. This allows the user to omit the ``settings()`` function, much like what can be done while programming in the Processing IDE. Py5 does this by inspecting the ``setup()`` function and attempting to split it into synthetic ``settings()`` and ``setup()`` functions if both were not created by the user and the real ``setup()`` function contains a call to ``smooth()``, or calls to :doc:`sketch_size`, :doc:`sketch_full_screen`, :doc:`sketch_no_smooth`, or :doc:`sketch_pixel_density`. Calls to those functions must be at the very beginning of ``setup()``, before any other Python code (but comments are ok). This feature is not available when programming in class mode.

Underlying Processing method: `smooth <https://processing.org/reference/smooth_.html>`_

Syntax
------

.. code:: python

    smooth() -> None
    smooth(level: int, /) -> None

Parameters
----------

* **level**: `int` - either 2, 3, 4, or 8 depending on the renderer


Updated on November 12, 2021 11:30:58am UTC

