text_width()
============

Calculates and returns the width of any character or text string.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_width_0.png
    :alt: example picture for text_width()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.text_size(28)
    
        c = 't'
        cw = py5.text_width(c)
        py5.text(c, 0, 40)
        py5.line(cw, 0, cw, 50)

        s = "Tokyo"
        sw = py5.text_width(s)
        py5.text(s, 0, 85)
        py5.line(sw, 50, sw, 100)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Calculates and returns the width of any character or text string.

Underlying Java method: `textWidth <https://processing.org/reference/textWidth_.html>`_

Syntax
------

.. code:: python

    text_width(c: chr, /) -> float
    text_width(chars: List[chr], start: int, length: int, /) -> float
    text_width(str: str, /) -> float

Parameters
----------

* **c**: `chr` - the character to measure
* **chars**: `List[chr]` - the character to measure
* **length**: `int` - number of characters to measure
* **start**: `int` - first character to measure
* **str**: `str` - the String of characters to measure


Updated on September 11, 2021 16:51:34pm UTC

