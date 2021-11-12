Py5Shape.set_path()
===================

Set many vertex points at the same time, using a numpy array.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_set_path_0.png
    :alt: example picture for set_path()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    import numpy as np

    def setup():
        vertices = 100 * np.random.rand(25, 2)
        s = py5.create_shape()
        s.begin_shape()
        s.no_fill()
        s.set_path(vertices.shape[0], vertices)
        s.end_shape()
        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Set many vertex points at the same time, using a numpy array. This will be faster and more efficient than repeatedly calling :doc:`py5shape_set_vertex` in a loop. Setting the vertex codes is not supported, so the vertices will be regular vertices and not bezier, quadratic or curve vertices.

The ``vcount`` parameter cannot be larger than the first dimension of the ``verts`` array.

Underlying Processing method: PShape.setPath

Syntax
------

.. code:: python

    set_path(vcount: int, verts: NDArray[(Any, Any), Float], /) -> None

Parameters
----------

* **vcount**: `int` - number of vertices
* **verts**: `NDArray[(Any, Any), Float]` - array of vertex coordinates


Updated on November 12, 2021 11:30:58am UTC

