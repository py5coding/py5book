pop_matrix()
============

Pops the current transformation matrix off the matrix stack.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_pop_matrix_0.png
    :alt: example picture for pop_matrix()

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

Pops the current transformation matrix off the matrix stack. Understanding pushing and popping requires understanding the concept of a matrix stack. The :doc:`sketch_push_matrix` function saves the current coordinate system to the stack and ``pop_matrix()`` restores the prior coordinate system. :doc:`sketch_push_matrix` and ``pop_matrix()`` are used in conjuction with the other transformation functions and may be embedded to control the scope of the transformations.

Underlying Java method: `popMatrix <https://processing.org/reference/popMatrix_.html>`_

Syntax
------

.. code:: python

    pop_matrix() -> None

Updated on September 11, 2021 16:51:34pm UTC

