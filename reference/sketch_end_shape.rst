end_shape()
===========

The ``end_shape()`` function is the companion to :doc:`sketch_begin_shape` and may only be called after :doc:`sketch_begin_shape`.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_end_shape_0.png
    :alt: example picture for end_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_fill()
    
        py5.begin_shape()
        py5.vertex(20, 20)
        py5.vertex(45, 20)
        py5.vertex(45, 80)
        py5.end_shape(py5.CLOSE)
    
        py5.begin_shape()
        py5.vertex(50, 20)
        py5.vertex(75, 20)
        py5.vertex(75, 80)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The ``end_shape()`` function is the companion to :doc:`sketch_begin_shape` and may only be called after :doc:`sketch_begin_shape`. When ``end_shape()`` is called, all of image data defined since the previous call to :doc:`sketch_begin_shape` is written into the image buffer. The constant ``CLOSE`` as the value for the ``MODE`` parameter to close the shape (to connect the beginning and the end).

Underlying Processing method: `endShape <https://processing.org/reference/endShape_.html>`_

Signatures
----------

.. code:: python

    end_shape() -> None

    end_shape(
        mode: int,  # use CLOSE to close the shape
        /,
    ) -> None

Updated on September 01, 2022 14:08:27pm UTC

