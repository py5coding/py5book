Py5Shape.contains()
===================

Boolean value reflecting if the given coordinates are or are not contained within the ``Py5Shape`` object.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_contains_0.png
    :alt: example picture for contains()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        chr_p = py5.create_font('DejaVu Sans', 32).get_shape('p')
        x_vertex_values = [chr_p.get_vertex_x(i) for i in range(chr_p.get_vertex_code_count())]
        y_vertex_values = [chr_p.get_vertex_y(i) for i in range(chr_p.get_vertex_code_count())]
        min_x, max_x = min(x_vertex_values), max(x_vertex_values)
        min_y, max_y = min(y_vertex_values), max(y_vertex_values)

        for _ in range(1000):
            x, y = py5.random(min_x, max_x), py5.random(min_y, max_y)
            if chr_p.contains(x, y):
                py5.point(2 * x, 2 * y + py5.height / 2)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Boolean value reflecting if the given coordinates are or are not contained within the ``Py5Shape`` object. This method will only work for a ``Py5Shape`` object that is a ``PATH`` shape or a ``GROUP`` of ``PATH`` shapes. Use :doc:`py5shape_get_family` to determine how a ``Py5Shape`` object was defined.

This method uses a coordinate system that is unique to the shape and how the paths were created. To get the range of relevant coordinates, start by finding the minimum and maximum values for the vertices using :doc:`py5shape_get_vertex_x` and :doc:`py5shape_get_vertex_y`. Do not use :doc:`py5shape_get_width` or :doc:`py5shape_get_height`.

Underlying Java method: PShape.contains

Syntax
------

.. code:: python

    contains(x: float, y: float, /) -> bool

Parameters
----------

* **x**: `float` - x-coordinate
* **y**: `float` - y-coordinate


Updated on September 11, 2021 16:51:34pm UTC

