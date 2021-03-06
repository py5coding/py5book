Py5Shape.get_child()
====================

Extracts a child ``Py5Shape`` object from a parent ``Py5Shape`` object that is defined as a ``GROUP``.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_child_0.png
    :alt: example picture for get_child()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        states = py5.load_shape("us_map.svg")
        ohio = states.get_child("OH")
        ohio.disable_style()

        py5.background(192)
        py5.scale(0.1)
        py5.translate(25, 225)
        py5.shape(states, 0, 0)
        py5.fill(255, 0, 0)
        py5.shape(ohio, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Extracts a child ``Py5Shape`` object from a parent ``Py5Shape`` object that is defined as a ``GROUP``. Specify the name of the shape with the ``target`` parameter, or use the index with the ``index`` parameter. The shape is returned as a ``Py5Shape`` object, or ``None`` is returned if there is an error.

Underlying Processing method: `PShape.getChild <https://processing.org/reference/PShape_getChild_.html>`_

Syntax
------

.. code:: python

    get_child(index: int, /) -> Py5Shape
    get_child(target: str, /) -> Py5Shape

Parameters
----------

* **index**: `int` - the layer position of the shape to get
* **target**: `str` - the name of the shape to get


Updated on November 12, 2021 11:30:58am UTC

