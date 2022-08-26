Py5Shape.rotate_y()
===================

Rotates the shape around the y-axis the amount specified by the ``angle`` parameter.

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
        global s
        py5.size(100, 100, py5.P3D)
        s = py5.load_shape("bot.svg")


    def draw():
        py5.background(204)
        py5.scale(0.2)
        py5.shape(s, py5.width//2, py5.height//2)


    def mouse_pressed():
        # rotate the shape around the y-axis each time the mouse is pressed
        s.rotate_y(0.1)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Rotates the shape around the y-axis the amount specified by the ``angle`` parameter. Angles should be specified in radians (values from 0 to ``TWO_PI``) or converted from degrees to radians with the :doc:`sketch_radians` method.

Shapes are always rotated around the upper-left corner of their bounding box. Positive numbers rotate objects in a clockwise direction. Subsequent calls to the method accumulates the effect. For example, calling ``rotate_y(HALF_PI)`` and then ``rotate_y(HALF_PI)`` is the same as ``rotate_y(PI)``. This transformation is applied directly to the shape, it's not refreshed each time ``draw()`` is run. 

This method requires a 3D renderer. You need to use ``P3D`` as a third parameter for the :doc:`sketch_size` function as shown in the example.

Underlying Processing method: `PShape.rotateY <https://processing.org/reference/PShape_rotateY_.html>`_

Signatures
------

.. code:: python

    rotate_y(
        angle: float,  # angle of rotation specified in radians
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

