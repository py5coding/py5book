Py5Shape.set_specular()
=======================

Sets the specular color of a ``Py5Shape`` object's material, which sets the color of highlight.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_set_specular_0.png
    :alt: example picture for set_specular()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.background(0)
        py5.light_specular(255, 255, 255)
        py5.directional_light(204, 204, 204, 0, 0, -1)
        py5.no_stroke()
        s = py5.create_shape(py5.SPHERE, 20)

        s.set_specular("#FFFFFF")
        py5.shape(s, 50, 25)
        s.set_specular("#CC6600")
        py5.shape(s, 50, 75)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the specular color of a ``Py5Shape`` object's material, which sets the color of highlight. This is part of the material properties of a ``Py5Shape`` object.

The ``specular`` parameter can be applied to the entire ``Py5Shape`` object or to a single vertex.

This method can only be used for a complete ``Py5Shape`` object, and never within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Processing method: PShape.setSpecular

Signatures
------

.. code:: python

    set_specular(
        index: int,  # vertex index
        specular: int,  # any color value
        /,
    ) -> None

    set_specular(
        specular: int,  # any color value
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

