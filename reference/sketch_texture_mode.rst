texture_mode()
==============

Sets the coordinate space for texture mapping.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_texture_mode_0.png
    :alt: example picture for texture_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.no_stroke()
        img = py5.load_image("laDefense.jpg")
        py5.texture_mode(py5.IMAGE)
        py5.begin_shape()
        py5.texture(img)
        py5.vertex(10, 20, 0, 0)
        py5.vertex(80, 5, 100, 0)
        py5.vertex(95, 90, 100, 100)
        py5.vertex(40, 95, 0, 100)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_texture_mode_1.png
    :alt: example picture for texture_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.no_stroke()
        img = py5.load_image("laDefense.jpg")
        py5.texture_mode(py5.NORMAL)
        py5.begin_shape()
        py5.texture(img)
        py5.vertex(10, 20, 0, 0)
        py5.vertex(80, 5, 1, 0)
        py5.vertex(95, 90, 1, 1)
        py5.vertex(40, 95, 0, 1)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the coordinate space for texture mapping. The default mode is ``IMAGE``, which refers to the actual pixel coordinates of the image. ``NORMAL`` refers to a normalized space of values ranging from 0 to 1. This function only works with the ``P2D`` and ``P3D`` renderers.

With ``IMAGE``, if an image is 100 x 200 pixels, mapping the image onto the entire size of a quad would require the points (0,0) (100,0) (100,200) (0,200). The same mapping in ``NORMAL`` is (0,0) (1,0) (1,1) (0,1).

Underlying Processing method: `textureMode <https://processing.org/reference/textureMode_.html>`_

Signatures
------

.. code:: python

    texture_mode(
        mode: int,  # either IMAGE or NORMAL
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

