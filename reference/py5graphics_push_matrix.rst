Py5Graphics.push_matrix()
=========================

Pushes the current transformation matrix onto the matrix stack.

Description
-----------

Pushes the current transformation matrix onto the matrix stack. Understanding ``push_matrix()`` and :doc:`py5graphics_pop_matrix` requires understanding the concept of a matrix stack. The ``push_matrix()`` function saves the current coordinate system to the stack and :doc:`py5graphics_pop_matrix` restores the prior coordinate system. ``push_matrix()`` and :doc:`py5graphics_pop_matrix` are used in conjuction with the other transformation functions and may be embedded to control the scope of the transformations.

This method is the same as :doc:`sketch_push_matrix` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_push_matrix`.

Underlying Java method: PGraphics.pushMatrix

Syntax
------

.. code:: python

    push_matrix() -> None

Updated on September 11, 2021 16:51:34pm UTC

