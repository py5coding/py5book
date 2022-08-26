Py5Shape.no_tint()
==================

Stop applying a color tint to a shape's texture map.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_no_tint_0.png
    :alt: example picture for no_tint()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)
        img = py5.load_image("tower.jpg")
        s = py5.create_shape()
        s.begin_shape()
        s.texture(img)
        s.tint(0, 0, 255)
        s.vertex(20, 20, 0, 0)
        s.vertex(20, 80, 0, 100)
        s.no_tint()
        s.vertex(80, 80, 100, 100)
        s.vertex(80, 20, 100, 0)
        s.end_shape(py5.CLOSE)

        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Stop applying a color tint to a shape's texture map. Use :doc:`py5shape_tint` to start applying a color tint.

Both :doc:`py5shape_tint` and ``no_tint()`` can be used to control the coloring of textures in 3D.

Underlying Processing method: PShape.noTint

Signatures
------

.. code:: python

    no_tint() -> None
Updated on August 25, 2022 20:01:47pm UTC

