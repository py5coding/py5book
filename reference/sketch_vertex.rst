vertex()
========

Add a new vertex to a shape.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_vertex_0.png
    :alt: example picture for vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.begin_shape(py5.POINTS)
        py5.vertex(30, 20)
        py5.vertex(85, 20)
        py5.vertex(85, 75)
        py5.vertex(30, 75)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_vertex_1.png
    :alt: example picture for vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        # drawing vertices in 3D requires P3D
        # as a parameter to size()
        py5.begin_shape()
        py5.vertex(30, 20, 10)
        py5.vertex(85, 20, 10)
        py5.vertex(85, 75, 10)
        py5.vertex(30, 75, 10)
        py5.end_shape(py5.CLOSE)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_vertex_2.png
    :alt: example picture for vertex()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        img = py5.load_image("laDefense.jpg")
        py5.no_stroke()
        py5.begin_shape()
        py5.texture(img)
        # "laDefense.jpg" is 100x100 pixels in size so
        # the values 0 and 100 are used for the
        # parameters "u" and "v" to map it directly
        # to the vertex points
        py5.vertex(10, 20, 0, 0)
        py5.vertex(80, 5, 100, 0)
        py5.vertex(95, 90, 100, 100)
        py5.vertex(40, 95, 0, 100)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Add a new vertex to a shape. All shapes are constructed by connecting a series of vertices. The ``vertex()`` method is used to specify the vertex coordinates for points, lines, triangles, quads, and polygons. It is used exclusively within the :doc:`sketch_begin_shape` and :doc:`sketch_end_shape` functions.

Drawing a vertex in 3D using the ``z`` parameter requires the ``P3D`` renderer, as shown in the second example.

This method is also used to map a texture onto geometry. The :doc:`sketch_texture` function declares the texture to apply to the geometry and the ``u`` and ``v`` coordinates define the mapping of this texture to the form. By default, the coordinates used for ``u`` and ``v`` are specified in relation to the image's size in pixels, but this relation can be changed with the Sketch's :doc:`sketch_texture_mode` method.

Underlying Processing method: `vertex <https://processing.org/reference/vertex_.html>`_

Syntax
------

.. code:: python

    vertex(v: NDArray[(Any,), Float], /) -> None
    vertex(x: float, y: float, /) -> None
    vertex(x: float, y: float, u: float, v: float, /) -> None
    vertex(x: float, y: float, z: float, /) -> None
    vertex(x: float, y: float, z: float, u: float, v: float, /) -> None

Parameters
----------

* **u**: `float` - horizontal coordinate for the texture mapping
* **v**: `NDArray[(Any,), Float]` - vertical coordinate for the texture mapping
* **v**: `float` - vertical coordinate for the texture mapping
* **x**: `float` - x-coordinate of the vertex
* **y**: `float` - y-coordinate of the vertex
* **z**: `float` - z-coordinate of the vertex


Updated on November 12, 2021 11:30:58am UTC

