Py5Shape.remove_child()
=======================

Removes a child ``Py5Shape`` object from a parent ``Py5Shape`` object that is defined as a ``GROUP``.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_remove_child_0.png
    :alt: example picture for remove_child()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        us_map = py5.load_shape("us_map.svg")
        for child in us_map.get_children():
            if child.get_name()[0] not in 'AEIOU':
                us_map.remove_child(us_map.get_child_index(child))

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

Removes a child ``Py5Shape`` object from a parent ``Py5Shape`` object that is defined as a ``GROUP``.

Underlying Processing method: PShape.removeChild

Signatures
----------

.. code:: python

    remove_child(
        idx: int,  # index value
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

