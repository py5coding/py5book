Py5Shape.texture_mode()
=======================

Sets a ``Py5Shape`` object's coordinate space for texture mapping.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_texture_mode_0.png
    :alt: example picture for texture_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.no_stroke()
        img = py5.load_image("laDefense.jpg")
        # call py5.texture_mode() here to inherit mode setting
        # py5.texture_mode(py5.IMAGE)
        s = py5.create_shape()
        s.begin_shape()
        s.texture(img)
        s.texture_mode(py5.IMAGE)
        s.vertex(10, 20, 0, 0)
        s.vertex(80, 5, 100, 0)
        s.vertex(95, 90, 100, 100)
        s.vertex(40, 95, 0, 100)
        s.end_shape()

        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_texture_mode_1.png
    :alt: example picture for texture_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.no_stroke()
        img = py5.load_image("laDefense.jpg")
        # call py5.texture_mode() here to inherit mode setting
        # py5.texture_mode(py5.NORMAL)
        s = py5.create_shape()
        s.begin_shape()
        s.texture(img)
        s.texture_mode(py5.NORMAL)
        s.vertex(10, 20, 0, 0)
        s.vertex(80, 5, 1, 0)
        s.vertex(95, 90, 1, 1)
        s.vertex(40, 95, 0, 1)
        s.end_shape()

        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets a ``Py5Shape`` object's coordinate space for texture mapping. The default mode is ``IMAGE``, which refers to the actual pixel coordinates of the image. ``NORMAL`` refers to a normalized space of values ranging from 0 to 1. This function only works with the ``P2D`` and ``P3D`` renderers.

If this method is not used, it will inherit the current texture mode setting from the Sketch when the shape is created.

With ``IMAGE``, if an image is 100 x 200 pixels, mapping the image onto the entire size of a quad would require the points (0,0) (100,0) (100,200) (0,200). The same mapping in ``NORMAL`` is (0,0) (1,0) (1,1) (0,1).

Underlying Processing method: PShape.textureMode

Syntax
------

.. code:: python

    texture_mode(mode: int, /) -> None

Parameters
----------

* **mode**: `int` - either IMAGE or NORMAL


Updated on November 12, 2021 11:30:58am UTC

