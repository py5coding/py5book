Py5Shape.get_vertex()
=====================

The ``get_vertex()`` method returns a numpy array with the coordinates of the vertex point located at the position defined by the ``index`` parameter.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global s
        s = py5.create_shape()
        s.begin_shape()
        s.vertex(0, 0)
        s.vertex(60, 0)
        s.vertex(60, 60)
        s.vertex(0, 60)
        s.end_shape(py5.CLOSE)


    def draw():
        py5.translate(20, 20)
        for i in range(0, s.get_vertex_count()):
            v = s.get_vertex(i)
            v[0] += py5.random(-1, 1)
            v[1] += py5.random(-1, 1)
            s.set_vertex(i, v)

        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The ``get_vertex()`` method returns a numpy array with the coordinates of the vertex point located at the position defined by the ``index`` parameter. This method works when shapes are created as shown in the example, but won't work properly when a shape is defined explicitly (e.g. ``create_shape(RECT, 20, 20, 80, 80)``.

Underlying Processing method: `PShape.getVertex <https://processing.org/reference/PShape_getVertex_.html>`_

Syntax
------

.. code:: python

    get_vertex(index: int, /) -> NDArray[(Any,), Float]
    get_vertex(index: int, vec: NDArray[(Any,), Float], /) -> NDArray[(Any,), Float]

Parameters
----------

* **index**: `int` - vertex index
* **vec**: `NDArray[(Any,), Float]` - properly sized numpy array to assign the data to


Updated on November 12, 2021 11:30:58am UTC

