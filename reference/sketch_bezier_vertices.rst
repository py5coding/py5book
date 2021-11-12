bezier_vertices()
=================

Create a collection of bezier vertices.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_bezier_vertices_0.png
    :alt: example picture for bezier_vertices()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    import numpy as np

    def setup():
        random_bezier_vertices = 100 * np.random.rand(25, 6)
        py5.begin_shape()
        py5.vertex(py5.width / 2, py5.height / 2)
        py5.bezier_vertices(random_bezier_vertices)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Create a collection of bezier vertices. The purpose of this method is to provide an alternative to repeatedly calling :doc:`sketch_bezier_vertex` in a loop. For a large number of bezier vertices, the performance of ``bezier_vertices()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each bezier vertex. The first few columns are for the first control point, the next few columns are for the second control point, and the final few columns are for the anchor point. There should be six or nine columns for 2D or 3D points, respectively.

Underlying Processing method: bezierVertices

Syntax
------

.. code:: python

    bezier_vertices(coordinates: NDArray[(Any, Any), Float], /) -> None

Parameters
----------

* **coordinates**: `NDArray[(Any, Any), Float]` - array of bezier vertex coordinates


Updated on November 12, 2021 11:30:58am UTC

