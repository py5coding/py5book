text_leading()
==============

Sets the spacing between lines of text in units of pixels.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_leading_0.png
    :alt: example picture for text_leading()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        # text to display. the "\n" is a "new line" character
        lines_of_text = "L1\nL2\nL3"
        py5.text_size(12)
        py5.fill(0)  # set fill to black
    
        py5.text_leading(10)  # set leading to 10
        py5.text(lines_of_text, 10, 25)
    
        py5.text_leading(20)  # set leading to 20
        py5.text(lines_of_text, 40, 25)
    
        py5.text_leading(30)  # set leading to 30
        py5.text(lines_of_text, 70, 25)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the spacing between lines of text in units of pixels. This setting will be used in all subsequent calls to the :doc:`sketch_text` function.  Note, however, that the leading is reset by :doc:`sketch_text_size`. For example, if the leading is set to 20 with ``text_leading(20)``, then if ``text_size(48)`` is run at a later point, the leading will be reset to the default for the text size of 48.

Underlying Java method: `textLeading <https://processing.org/reference/textLeading_.html>`_

Syntax
------

.. code:: python

    text_leading(leading: float, /) -> None

Parameters
----------

* **leading**: `float` - the size in pixels for spacing between lines


Updated on September 11, 2021 16:51:34pm UTC

