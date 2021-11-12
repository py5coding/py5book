Py5Graphics.text_width()
========================

Calculates and returns the width of any character or text string.

Description
-----------

Calculates and returns the width of any character or text string.

This method is the same as :doc:`sketch_text_width` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_text_width`.

Underlying Processing method: PGraphics.textWidth

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


Updated on November 12, 2021 11:30:58am UTC

