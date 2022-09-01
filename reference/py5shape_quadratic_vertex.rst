Py5Shape.quadratic_vertex()
===========================

Specifies a ``Py5Shape`` object's vertex coordinates for quadratic Bezier curves.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_bezier_vertex_0.png
    :alt: example picture for quadratic_vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)
        s = py5.create_shape()
        s.begin_shape()
        s.no_fill()
        s.vertex(20, 20)
        s.quadratic_vertex(80, 20, 50, 50)
        s.end_shape()
        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_bezier_vertex_1.png
    :alt: example picture for quadratic_vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)
        s = py5.create_shape()
        s.begin_shape()
        s.vertex(20, 20)
        s.quadratic_vertex(80, 20, 50, 50)
        s.quadratic_vertex(20, 80, 80, 80)
        s.vertex(80, 60)
        s.end_shape()
        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Specifies a ``Py5Shape`` object's vertex coordinates for quadratic Bezier curves. Each call to ``quadratic_vertex()`` defines the position of one control point and one anchor point of a Bezier curve, adding a new segment to a line or shape. The first time ``quadratic_vertex()`` is used within a :doc:`py5shape_begin_shape` call, it must be prefaced with a call to :doc:`py5shape_vertex` to set the first anchor point. This method must be used between :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` and only when there is no ``MODE`` parameter specified to :doc:`py5shape_begin_shape`.

Drawing 2D bezier curves requires using the ``P2D`` renderer and drawing 3D bezier curves requires using the ``P3D`` renderer. When drawing directly with ``Py5Shape`` objects, bezier curves do not work at all using the default renderer.

Underlying Processing method: PShape.quadraticVertex

Signatures
----------

.. code:: python

    quadratic_vertex(
        cx: float,  # the x-coordinate of the control point
        cy: float,  # the y-coordinate of the control point
        cz: float,  # the z-coordinate of the control point
        x3: float,  # the x-coordinate of the anchor point
        y3: float,  # the y-coordinate of the anchor point
        z3: float,  # the z-coordinate of the anchor point
        /,
    ) -> None

    quadratic_vertex(
        cx: float,  # the x-coordinate of the control point
        cy: float,  # the y-coordinate of the control point
        x3: float,  # the x-coordinate of the anchor point
        y3: float,  # the y-coordinate of the anchor point
        /,
    ) -> None

Updated on September 01, 2022 14:08:27pm UTC

