Py5Shape.get_child_index()
==========================

Get a child ``Py5Shape`` object's index from a parent ``Py5Shape`` object that is defined as a ``GROUP``.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_child_index_0.png
    :alt: example picture for get_child_index()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        us_map = py5.load_shape("us_map.svg")
        for child in us_map.get_children():
            idx = us_map.get_child_index(child)
            py5.println(child.get_name(), idx)

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

Get a child ``Py5Shape`` object's index from a parent ``Py5Shape`` object that is defined as a ``GROUP``. Inside Processing, a group ``Py5Shape`` object is an ordered list of child shapes. This method will retrieve the index for a particular child in that ordered list. That index value is useful when using other methods such as :doc:`py5shape_get_child` or :doc:`py5shape_remove_child`.

Underlying Processing method: PShape.getChildIndex

Signatures
----------

.. code:: python

    get_child_index(
        who: Py5Shape,  # Py5Shape object
        /,
    ) -> int

Updated on September 01, 2022 16:36:02pm UTC

