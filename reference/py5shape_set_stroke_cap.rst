Py5Shape.set_stroke_cap()
=========================

Sets the style for rendering line endings in a ``Py5Shape`` object.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_set_stroke_cap_0.png
    :alt: example picture for set_stroke_cap()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        s = py5.create_shape()
        s.begin_shape()
        s.stroke_weight(12.0)
        s.vertex(20, 0)
        s.vertex(80, 0)
        s.end_shape()

        py5.shape(s, 0, 30)
        s.set_stroke_cap(py5.SQUARE)
        py5.shape(s, 0, 50)
        s.set_stroke_cap(py5.PROJECT)
        py5.shape(s, 0, 70)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the style for rendering line endings in a ``Py5Shape`` object. These ends are either squared, extended, or rounded, each of which specified with the corresponding parameters: ``SQUARE``, ``PROJECT``, and ``ROUND``. The default cap is ``ROUND``.

This method differs from :doc:`py5shape_stroke_cap` in that it is only to be used outside the :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` methods.

Underlying Processing method: PShape.setStrokeCap

Signatures
----------

.. code:: python

    set_stroke_cap(
        cap: int,  # either SQUARE, PROJECT, or ROUND
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

