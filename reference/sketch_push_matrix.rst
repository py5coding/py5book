push_matrix()
=============

Pushes the current transformation matrix onto the matrix stack.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_push_matrix_0.png
    :alt: example picture for push_matrix()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.fill(255)
        py5.rect(0, 0, 50, 50)  # white rectangle
    
        py5.push_matrix()
        py5.translate(30, 20)
        py5.fill(0)
        py5.rect(0, 0, 50, 50)  # black rectangle
        py5.pop_matrix()
    
        py5.fill(100)
        py5.rect(15, 10, 50, 50)  # gray rectangle

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Pushes the current transformation matrix onto the matrix stack. Understanding ``push_matrix()`` and :doc:`sketch_pop_matrix` requires understanding the concept of a matrix stack. The ``push_matrix()`` function saves the current coordinate system to the stack and :doc:`sketch_pop_matrix` restores the prior coordinate system. ``push_matrix()`` and :doc:`sketch_pop_matrix` are used in conjuction with the other transformation functions and may be embedded to control the scope of the transformations.

Underlying Processing method: `pushMatrix <https://processing.org/reference/pushMatrix_.html>`_

Syntax
------

.. code:: python

    push_matrix() -> None

Updated on November 12, 2021 11:30:58am UTC

