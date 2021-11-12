Py5Shape.get_children()
=======================

Get the children of a ``Py5Shape`` object as a list of ``Py5Shape`` objects.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_children_0.png
    :alt: example picture for get_children()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        us_map = py5.load_shape("us_map.svg")
        for child in us_map.get_children():
            py5.println(child.get_name())

        py5.background(192)
        py5.scale(0.1)
        py5.translate(25, 225)
        py5.shape(us_map, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Get the children of a ``Py5Shape`` object as a list of ``Py5Shape`` objects. When Processing loads shape objects, it may create a hierarchy of ``Py5Shape`` objects, depending on the organization of the source data file. This method will retrieve the list of Py5Shapes that are the child objects to a given object.

Underlying Processing method: PShape.getChildren

Syntax
------

.. code:: python

    get_children() -> List[Py5Shape]

Updated on November 12, 2021 11:30:58am UTC

