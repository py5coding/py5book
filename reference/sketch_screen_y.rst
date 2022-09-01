screen_y()
==========

Takes a three-dimensional X, Y, Z position and returns the Y value for where it will appear on a (two-dimensional) screen.

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
        py5.size(100, 100, py5.P3D)


    def draw():
        py5.background(204)

        x = py5.mouse_x
        y = py5.mouse_y
        z = -100

        # draw "X" at z = -100
        py5.stroke(255)
        py5.line(x-10, y-10, z, x+10, y+10, z)
        py5.line(x+10, y-10, z, x-10, y+10, z)

        # draw gray line at z = 0 and same
        # y value. notice the parallax
        py5.stroke(102)
        py5.line(0, y, 0, py5.width, y, 0)

        # draw black line at z = 0 to match
        # the y value element drawn at z = -100
        py5.stroke(0)
        the_y = py5.screen_y(x, y, z)
        py5.line(0, the_y, 0, py5.width, the_y, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Takes a three-dimensional X, Y, Z position and returns the Y value for where it will appear on a (two-dimensional) screen.

Underlying Processing method: `screenY <https://processing.org/reference/screenY_.html>`_

Signatures
----------

.. code:: python

    screen_y(
        x: float,  # 3D x-coordinate to be mapped
        y: float,  # 3D y-coordinate to be mapped
        /,
    ) -> float

    screen_y(
        x: float,  # 3D x-coordinate to be mapped
        y: float,  # 3D y-coordinate to be mapped
        z: float,  # 3D z-coordinate to be mapped
        /,
    ) -> float

Updated on September 01, 2022 14:08:27pm UTC

