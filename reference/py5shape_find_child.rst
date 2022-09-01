Py5Shape.find_child()
=====================

Find a target ``Py5Shape`` object from anywhere within a ``Py5Shape`` object that is defined as a ``GROUP``.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_find_child_0.png
    :alt: example picture for find_child()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        states = py5.load_shape("us_map.svg")
        new_york = states.get_child("NY")
        ohio = new_york.find_child("OH")
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

Find a target ``Py5Shape`` object from anywhere within a ``Py5Shape`` object that is defined as a ``GROUP``. This is similar to :doc:`py5shape_get_child` in that it locates a child ``Py5Shape`` object, except that it can start the search from another child shape instead of the parent.

Underlying Processing method: PShape.findChild

Signatures
----------

.. code:: python

    find_child(
        target: str,  # name of child object
        /,
    ) -> Py5Shape
Updated on September 01, 2022 12:53:02pm UTC

