Py5Shape.set_ambient()
======================

Sets a ``Py5Shape`` object's ambient reflectance.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_set_ambient_0.png
    :alt: example picture for set_ambient()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.background(0)
        py5.directional_light(153, 153, 153, .5, 0, -1)
        py5.ambient_light(50, 50, 50)
        py5.no_stroke()
        s = py5.create_shape(py5.SPHERE, 20)

        s.set_ambient("#FF0000")
        py5.shape(s, 50, 25)
        s.set_ambient("#FFFF00")
        py5.shape(s, 50, 75)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets a ``Py5Shape`` object's ambient reflectance. This is combined with the ambient light component of the environment. The color components set through the parameters define the reflectance. For example in the default color mode, calling ``set_ambient(255, 127, 0)``, would cause all the red light to reflect and half of the green light to reflect. Use in combination with :doc:`py5shape_set_emissive`, :doc:`py5shape_set_specular`, and :doc:`py5shape_set_shininess` to set the material properties of a ``Py5Shape`` object.

The ``ambient`` parameter can be applied to the entire ``Py5Shape`` object or to a single vertex.

This method can only be used for a complete ``Py5Shape`` object, and never within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Processing method: PShape.setAmbient

Signatures
------

.. code:: python

    set_ambient(
        ambient: int,  # any color value
        /,
    ) -> None

    set_ambient(
        index: int,  # vertex index
        ambient: int,  # any color value
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

