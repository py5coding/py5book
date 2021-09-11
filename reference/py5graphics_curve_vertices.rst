Py5Graphics.curve_vertices()
============================

Create a collection of curve vertices.

Description
-----------

Create a collection of curve vertices. The purpose of this method is to provide an alternative to repeatedly calling :doc:`py5graphics_curve_vertex` in a loop. For a large number of curve vertices, the performance of ``curve_vertices()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each curve vertex.  There should be two or three columns for 2D or 3D points, respectively.

This method is the same as :doc:`sketch_curve_vertices` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_curve_vertices`.

Underlying Java method: PGraphics.curveVertices

Syntax
------

.. code:: python

    curve_vertices(coordinates: NDArray[(Any, Any), Float], /) -> None

Parameters
----------

* **coordinates**: `NDArray[(Any, Any), Float]` - array of curve vertex coordinates


Updated on September 11, 2021 16:51:34pm UTC

