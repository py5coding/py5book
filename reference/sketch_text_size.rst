text_size()
===========

Sets the current font size.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_size_0.png
    :alt: example picture for text_size()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.background(0)
        py5.fill(255)
        py5.text_size(26)
        py5.text("WORD", 10, 50)
        py5.text_size(14)
        py5.text("WORD", 10, 70)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the current font size. This size will be used in all subsequent calls to the :doc:`sketch_text` function. Font size is measured in units of pixels.

Underlying Processing method: `textSize <https://processing.org/reference/textSize_.html>`_

Signatures
------

.. code:: python

    text_size(
        size: float,  # the size of the letters in units of pixels
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

