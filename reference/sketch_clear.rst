clear()
=======

Clear the drawing surface by setting every pixel to black.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_clear_0.png
    :alt: example picture for clear()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.fill(255)
        py5.rect(5, 5, 40, 40)
        py5.clear()
        py5.rect(55, 55, 40, 40)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Clear the drawing surface by setting every pixel to black. Calling this method is the same as passing ``0`` to the :doc:`sketch_background` method, as in ``background(0)``.

This method behaves differently than :doc:`py5graphics_clear` because ``Py5Graphics`` objects allow transparent pixels.

Underlying Processing method: `clear <https://processing.org/reference/clear_.html>`_

Signatures
----------

.. code:: python

    clear() -> None

Updated on September 01, 2022 16:36:02pm UTC

