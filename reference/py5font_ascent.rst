Py5Font.ascent()
================

Get the ascent of this font from the baseline.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Font_ascent_0.png
    :alt: example picture for ascent()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        font_size = 45
        font = py5.create_font('DejaVu Sans', font_size)
        py5.text_font(font)

        baseline = py5.height / 2
        ascent = baseline - font.ascent() * font_size
        descent = baseline + font.descent() * font_size

        py5.text("py5", 10, baseline)
        py5.line(0, ascent, py5.width, ascent)
        py5.line(0, baseline, py5.width, baseline)
        py5.line(0, descent, py5.width, descent)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Get the ascent of this font from the baseline. The value is based on a font of size 1. Multiply it by the font size to get the offset from the baseline.

Underlying Processing method: PFont.ascent

Signatures
----------

.. code:: python

    ascent() -> float

Updated on September 01, 2022 16:36:02pm UTC

