Py5Shape.set_texture()
======================

Set a ``Py5Shape`` object's texture.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_set_texture_0.png
    :alt: example picture for set_texture()

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

Set a ``Py5Shape`` object's texture. This method differs from :doc:`py5shape_texture` in that it is only to be used outside the :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` methods. This method only works with the ``P2D`` and ``P3D`` renderers. This method can be used in conjunction with :doc:`py5shape_set_texture_mode` and :doc:`py5shape_set_texture_uv`.

When textures are in use, the fill color is ignored. Instead, use :doc:`py5shape_tint` to specify the color of the texture as it is applied to the shape.

Underlying Processing method: PShape.setTexture

Signatures
----------

.. code:: python

    set_texture(
        tex: Py5Image,  # reference to a Py5Image object
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

