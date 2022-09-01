Py5Shape.set_texture_mode()
===========================

Sets a ``Py5Shape`` object's coordinate space for texture mapping.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_set_texture_mode_0.png
    :alt: example picture for set_texture_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)
        img = py5.load_image("tower.jpg")
        s = py5.create_shape()
        s.begin_shape()
        s.vertex(20, 20)
        s.vertex(20, 80)
        s.vertex(80, 80)
        s.vertex(80, 20)
        s.end_shape(py5.CLOSE)

        s.set_texture(img)
        s.set_texture_mode(py5.NORMAL)
        s.set_texture_uv(0, 0, 0)
        s.set_texture_uv(1, 0, 1)
        s.set_texture_uv(2, 1, 1)
        s.set_texture_uv(3, 1, 0)

        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets a ``Py5Shape`` object's coordinate space for texture mapping. This method differs from :doc:`py5shape_texture_mode` in that it is only to be used outside the :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` methods. Use of this method should be followed by calls to :doc:`py5shape_set_texture_uv` to set the mapping coordinates using the new mode.

The default mode is ``IMAGE``, which refers to the actual pixel coordinates of the image. ``NORMAL`` refers to a normalized space of values ranging from 0 to 1. This function only works with the ``P2D`` and ``P3D`` renderers.

With ``IMAGE``, if an image is 100 x 200 pixels, mapping the image onto the entire size of a quad would require the points (0,0) (100,0) (100,200) (0,200). The same mapping in ``NORMAL`` is (0,0) (1,0) (1,1) (0,1).

Underlying Processing method: PShape.setTextureMode

Signatures
----------

.. code:: python

    set_texture_mode(
        mode: int,  # either IMAGE or NORMAL
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

