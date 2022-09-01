Py5Shape.get_child_count()
==========================

Returns the number of children within the ``Py5Shape`` object.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        us_map = py5.load_shape("us_map.svg")
        count = us_map.get_child_count()
        py5.println(count)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Returns the number of children within the ``Py5Shape`` object.

Underlying Processing method: `PShape.getChildCount <https://processing.org/reference/PShape_getChildCount_.html>`_

Signatures
----------

.. code:: python

    get_child_count() -> int
Updated on September 01, 2022 12:53:02pm UTC

