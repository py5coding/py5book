Py5Shape.get_vertex_codes()
===========================

Get the vertex codes for a ``Py5Shape`` object.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_vertex_codes_0.png
    :alt: example picture for get_vertex_codes()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    SHAPE_VERTEX_CODES = {py5.Py5Shape.BREAK: 'BREAK',
                          py5.Py5Shape.VERTEX: 'VERTEX'}


    def setup():
        py5.size(100, 100, py5.P2D)
        s = py5.create_shape()
        s.begin_shape()
        s.vertex(20, 20)
        s.vertex(80, 20)
        s.vertex(80, 80)
        s.vertex(20, 80)
        s.begin_contour()
        s.vertex(40, 40)
        s.vertex(40, 60)
        s.vertex(60, 60)
        s.vertex(60, 40)
        s.end_contour()
        s.end_shape(py5.CLOSE)
        py5.shape(s)

        py5.println(s.get_vertex_count(), s.get_vertex_code_count())  # 8 9
        # ['VERTEX', 'VERTEX', 'VERTEX', 'VERTEX', 'BREAK', 'VERTEX', 'VERTEX', 'VERTEX', 'VERTEX']
        py5.println([SHAPE_VERTEX_CODES[i] for i in s.get_vertex_codes()])

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Get the vertex codes for a ``Py5Shape`` object. The vertex codes can be used to inspect a shape's geometry to determine what kind of vertices it has. Each can be one of ``BREAK``, ``VERTEX``, ``BEZIER_VERTEX``, ``QUADRATIC_VERTEX`` or ``CURVE_VERTEX``.

The vertex codes will not necessarily align with the vertices because number of vertex codes may be larger than the number of vertices. This will be the case for shapes that use contours, and therefore contain ``BREAK`` codes.

Underlying Processing method: PShape.getVertexCodes

Signatures
----------

.. code:: python

    get_vertex_codes() -> npt.NDArray[np.integer]

Updated on September 01, 2022 14:08:27pm UTC

