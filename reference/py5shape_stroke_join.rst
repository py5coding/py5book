Py5Shape.stroke_join()
======================

Sets the style of the joints which connect line segments in a ``Py5Shape`` object.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_stroke_join_0.png
    :alt: example picture for stroke_join()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        s = py5.create_shape()
        s.begin_shape()
        s.no_fill()
        s.stroke_weight(10.0)
        s.stroke_join(py5.MITER)
        s.vertex(35, 20)
        s.vertex(65, 50)
        s.vertex(35, 80)
        s.end_shape()

        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_stroke_join_1.png
    :alt: example picture for stroke_join()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        s = py5.create_shape()
        s.begin_shape()
        s.no_fill()
        s.stroke_weight(10.0)
        s.stroke_join(py5.BEVEL)
        s.vertex(35, 20)
        s.vertex(65, 50)
        s.vertex(35, 80)
        s.end_shape()

        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_stroke_join_2.png
    :alt: example picture for stroke_join()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        s = py5.create_shape()
        s.begin_shape()
        s.no_fill()
        s.stroke_weight(10.0)
        s.stroke_join(py5.ROUND)
        s.vertex(35, 20)
        s.vertex(65, 50)
        s.vertex(35, 80)
        s.end_shape()

        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the style of the joints which connect line segments in a ``Py5Shape`` object. These joints are either mitered, beveled, or rounded and specified with the corresponding parameters ``MITER``, ``BEVEL``, and ``ROUND``. The default joint is ``MITER``.

This method can only be used within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Processing method: PShape.strokeJoin

Signatures
----------

.. code:: python

    stroke_join(
        join: int,  # either MITER, BEVEL, ROUND
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

