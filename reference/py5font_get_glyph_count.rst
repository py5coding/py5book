Py5Font.get_glyph_count()
=========================

Get the number of glyphs contained in the font.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Font_get_glyph_count_0.png
    :alt: example picture for get_glyph_count()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)
        font_size = 32
        font1 = py5.create_font('DejaVu Sans', font_size)
        font2 = py5.load_font('DejaVu_Sans-32.vlw')
        font3 = py5.create_font('DejaVu Sans', font_size, True, 'py5')

        py5.println(font1.get_glyph_count())
        py5.println(font2.get_glyph_count())
        py5.println(font3.get_glyph_count())

        py5.text_font(font1)
        py5.text('py5', 10, 30)

        py5.text_font(font2)
        py5.text('py5', 10, 60)

        py5.text_font(font3)
        py5.text('py5', 10, 90)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Get the number of glyphs contained in the font. This will be 0 if the font is a "lazy font" that creates glyphs as they are needed by the Sketch. This will be the case if the font was created with :doc:`sketch_create_font` without using the ``charset`` parameter.

Underlying Java method: PFont.getGlyphCount

Syntax
------

.. code:: python

    get_glyph_count() -> int

Updated on September 11, 2021 16:51:34pm UTC

