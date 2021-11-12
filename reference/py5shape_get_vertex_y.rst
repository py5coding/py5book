Py5Shape.get_vertex_y()
=======================

Get the value of the y coordinate for the vertex ``index``.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_vertex_y_0.png
    :alt: example picture for get_vertex_y()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        s1 = py5.create_shape()
        s1.begin_shape()
        s1.vertex(20, 80)
        s1.vertex(80, 80)
        s1.vertex(50, 20)
        s1.end_shape(py5.CLOSE)
        py5.shape(s1)
        y_values = [s1.get_vertex_y(i) for i in range(s1.get_vertex_count())]
        py5.println(s1.get_height(), min(y_values), max(y_values))  # 80, 20, 80

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_vertex_y_1.png
    :alt: example picture for get_vertex_y()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.sphere_detail(8)
        s1 = py5.create_shape(py5.SPHERE, 40)
        y_values = [s1.get_vertex_y(i) for i in range(s1.get_vertex_count())]
        py5.shape(s1, 50, 50)
        py5.println(s1.get_height(), min(y_values), max(y_values))  # 80, -40, 40

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Get the value of the y coordinate for the vertex ``index``.

Underlying Processing method: PShape.getVertexY

Syntax
------

.. code:: python

    get_vertex_y(index: int, /) -> float

Parameters
----------

* **index**: `int` - vertex index


Updated on November 12, 2021 11:30:58am UTC

