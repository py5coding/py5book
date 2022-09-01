model_z()
=========

Returns the three-dimensional X, Y, Z position in model space.

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
        py5.size(500, 500, py5.P3D)
        py5.no_fill()


    def draw():
        py5.background(0)

        py5.push_matrix()
        # start at the middle of the screen
        py5.translate(py5.width//2, py5.height//2, -200)
        # some random rotation to make things interesting
        py5.rotate_y(1.0)  # yrot)
        py5.rotate_z(2.0)  # zrot)
        # rotate in X a little more each frame
        py5.rotate_x(py5.frame_count/100.0)
        # offset from_ center
        py5.translate(0, 150, 0)

        # draw a white box outline at (0, 0, 0)
        py5.stroke(255)
        py5.box(50)

        # the box was drawn at (0, 0, 0), store that location
        x = py5.model_x(0, 0, 0)
        y = py5.model_y(0, 0, 0)
        z = py5.model_z(0, 0, 0)
        # clear out all the transformations
        py5.pop_matrix()

        # draw another box at the same (x, y, z) coordinate as the other
        py5.push_matrix()
        py5.translate(x, y, z)
        py5.stroke(255, 0, 0)
        py5.box(50)
        py5.pop_matrix()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Returns the three-dimensional X, Y, Z position in model space. This returns the Z value for a given coordinate based on the current set of transformations (scale, rotate, translate, etc.) The Z value can be used to place an object in space relative to the location of the original point once the transformations are no longer in use.

In the example, the :doc:`sketch_model_x`, :doc:`sketch_model_y`, and ``model_z()`` functions record the location of a box in space after being placed using a series of translate and rotate commands. After :doc:`sketch_pop_matrix` is called, those transformations no longer apply, but the (x, y, z) coordinate returned by the model functions is used to place another box in the same location.

Underlying Processing method: `modelZ <https://processing.org/reference/modelZ_.html>`_

Signatures
----------

.. code:: python

    model_z(
        x: float,  # 3D x-coordinate to be mapped
        y: float,  # 3D y-coordinate to be mapped
        z: float,  # 3D z-coordinate to be mapped
        /,
    ) -> float
Updated on September 01, 2022 12:53:02pm UTC

