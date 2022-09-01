Py5Shape.get_kind()
===================

Get the Py5Shape object's "kind" number.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_kind_0.png
    :alt: example picture for get_kind()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # this is just a subset of the possible values
    PY5SHAPE_KIND_VALS = {py5.Py5Shape.GROUP: 'GROUP',
                          py5.Py5Shape.ELLIPSE: 'ELLIPSE'}


    def setup():
        s = py5.load_shape("bot.svg")
        for child in s.get_children():
            py5.println(PY5SHAPE_KIND_VALS[child.get_kind()])

        py5.background(192)
        py5.scale(0.25)
        py5.shape(s, py5.width//2, py5.height//2)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Get the Py5Shape object's "kind" number.

Underlying Processing method: PShape.getKind

Signatures
----------

.. code:: python

    get_kind() -> int
Updated on September 01, 2022 12:53:02pm UTC

