rotate()
========

Rotates the amount specified by the ``angle`` parameter.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_rotate_0.png
    :alt: example picture for rotate()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.translate(py5.width//2, py5.height//2)
        py5.rotate(py5.PI/3.0)
        py5.rect(-26, -26, 52, 52)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Rotates the amount specified by the ``angle`` parameter. Angles must be specified in radians (values from ``0`` to ``TWO_PI``), or they can be converted from degrees to radians with the :doc:`sketch_radians` function. 
 
The coordinates are always rotated around their relative position to the origin. Positive numbers rotate objects in a clockwise direction and negative numbers rotate in the couterclockwise direction. Transformations apply to everything that happens afterward, and subsequent calls to the function compound the effect. For example, calling ``rotate(PI/2.0)`` once and then calling ``rotate(PI/2.0)`` a second time is the same as a single ``rotate(PI)``. All tranformations are reset when ``draw()`` begins again. 
 
Technically, ``rotate()`` multiplies the current transformation matrix by a rotation matrix. This function can be further controlled by :doc:`sketch_push_matrix` and :doc:`sketch_pop_matrix`.

Underlying Processing method: `rotate <https://processing.org/reference/rotate_.html>`_

Signatures
------

.. code:: python

    rotate(
        angle: float,  # angle of rotation specified in radians
        /,
    ) -> None

    rotate(
        angle: float,  # angle of rotation specified in radians
        x: float,  # x-coordinate of vector to rotate around
        y: float,  # y-coordinate of vector to rotate around
        z: float,  # z-coordinate of vector to rotate around
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

