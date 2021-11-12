Py5Graphics.bezier_vertices()
=============================

Create a collection of bezier vertices.

Description
-----------

Create a collection of bezier vertices. The purpose of this method is to provide an alternative to repeatedly calling :doc:`py5graphics_bezier_vertex` in a loop. For a large number of bezier vertices, the performance of ``bezier_vertices()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each bezier vertex. The first few columns are for the first control point, the next few columns are for the second control point, and the final few columns are for the anchor point. There should be six or nine columns for 2D or 3D points, respectively.

This method is the same as :doc:`sketch_bezier_vertices` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_bezier_vertices`.

Underlying Processing method: PGraphics.bezierVertices

Syntax
------

.. code:: python

    bezier_vertices(coordinates: NDArray[(Any, Any), Float], /) -> None

Parameters
----------

* **coordinates**: `NDArray[(Any, Any), Float]` - array of bezier vertex coordinates


Updated on November 12, 2021 11:30:58am UTC

