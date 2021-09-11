quadratic_vertex()
==================

Specifies vertex coordinates for quadratic Bezier curves.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_quadratic_vertex_0.png
    :alt: example picture for quadratic_vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_fill()
        py5.stroke_weight(4)
        py5.begin_shape()
        py5.vertex(20, 20)
        py5.quadratic_vertex(80, 20, 50, 50)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_quadratic_vertex_1.png
    :alt: example picture for quadratic_vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_fill()
        py5.stroke_weight(4)
        py5.begin_shape()
        py5.vertex(20, 20)
        py5.quadratic_vertex(80, 20, 50, 50)
        py5.quadratic_vertex(20, 80, 80, 80)
        py5.vertex(80, 60)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Specifies vertex coordinates for quadratic Bezier curves. Each call to ``quadratic_vertex()`` defines the position of one control point and one anchor point of a Bezier curve, adding a new segment to a line or shape. The first time ``quadratic_vertex()`` is used within a :doc:`sketch_begin_shape` call, it must be prefaced with a call to :doc:`sketch_vertex` to set the first anchor point. This method must be used between :doc:`sketch_begin_shape` and :doc:`sketch_end_shape` and only when there is no ``MODE`` parameter specified to :doc:`sketch_begin_shape`. Using the 3D version requires rendering with ``P3D``.

Underlying Java method: `quadraticVertex <https://processing.org/reference/quadraticVertex_.html>`_

Syntax
------

.. code:: python

    quadratic_vertex(cx: float, cy: float, cz: float, x3: float, y3: float, z3: float, /) -> None
    quadratic_vertex(cx: float, cy: float, x3: float, y3: float, /) -> None

Parameters
----------

* **cx**: `float` - the x-coordinate of the control point
* **cy**: `float` - the y-coordinate of the control point
* **cz**: `float` - the z-coordinate of the control point
* **x3**: `float` - the x-coordinate of the anchor point
* **y3**: `float` - the y-coordinate of the anchor point
* **z3**: `float` - the z-coordinate of the anchor point


Updated on September 11, 2021 16:51:34pm UTC

