texture()
=========

Sets a texture to be applied to vertex points.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_texture_0.png
    :alt: example picture for texture()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.no_stroke()
        img = py5.load_image("laDefense.jpg")
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

    </div>

Description
-----------

Sets a texture to be applied to vertex points. The ``texture()`` method must be called between :doc:`sketch_begin_shape` and :doc:`sketch_end_shape` and before any calls to :doc:`sketch_vertex`. This method only works with the ``P2D`` and ``P3D`` renderers.

When textures are in use, the fill color is ignored. Instead, use :doc:`sketch_tint` to specify the color of the texture as it is applied to the shape.

Underlying Processing method: `texture <https://processing.org/reference/texture_.html>`_

Signatures
------

.. code:: python

    texture(
        image: Py5Image,  # reference to a Py5Image object
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

