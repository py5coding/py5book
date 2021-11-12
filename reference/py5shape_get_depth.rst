Py5Shape.get_depth()
====================

Get the ``Py5Shape`` object's depth.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_depth_0.png
    :alt: example picture for get_depth()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.sphere_detail(8)
        s1 = py5.create_shape(py5.SPHERE, 40)
        z_values = [s1.get_vertex_z(i) for i in range(s1.get_vertex_count())]
        py5.shape(s1, 50, 50)
        py5.println(s1.get_depth(), min(z_values), max(z_values))  # 80, -40, 40

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Get the ``Py5Shape`` object's depth. This method only makes sense when using the ``P3D`` renderer. It will return 0 when using default renderer.

Underlying Processing method: PShape.getDepth

Syntax
------

.. code:: python

    get_depth() -> float

Updated on November 12, 2021 11:30:58am UTC

