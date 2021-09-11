ortho()
=======

Sets an orthographic projection and defines a parallel clipping volume.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_ortho_0.png
    :alt: example picture for ortho()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.no_fill()
        py5.ortho(-py5.width//2, py5.width//2,
                  -py5.height // 2, py5.height//2)  # same as ortho()
        py5.translate(py5.width//2, py5.height//2, 0)
        py5.rotate_x(-py5.PI/6)
        py5.rotate_y(py5.PI/3)
        py5.box(45)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets an orthographic projection and defines a parallel clipping volume. All objects with the same dimension appear the same size, regardless of whether they are near or far from the camera. The parameters to this function specify the clipping volume where left and right are the minimum and maximum x values, top and bottom are the minimum and maximum y values, and near and far are the minimum and maximum z values. If no parameters are given, the default is used: ``ortho(-width/2, width/2, -height/2, height/2)``.

Underlying Java method: `ortho <https://processing.org/reference/ortho_.html>`_

Syntax
------

.. code:: python

    ortho() -> None
    ortho(left: float, right: float, bottom: float, top: float, /) -> None
    ortho(left: float, right: float, bottom: float, top: float, near: float, far: float, /) -> None

Parameters
----------

* **bottom**: `float` - bottom plane of the clipping volume
* **far**: `float` - maximum distance from the origin away from the viewer
* **left**: `float` - left plane of the clipping volume
* **near**: `float` - maximum distance from the origin to the viewer
* **right**: `float` - right plane of the clipping volume
* **top**: `float` - top plane of the clipping volume


Updated on September 11, 2021 16:51:34pm UTC

