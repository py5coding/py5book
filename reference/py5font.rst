Py5Font
=======

Py5Font is the font class for py5.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Font_0.png
    :alt: example picture for Py5Font

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        font = py5.create_font("DejaVu Sans", 32)
        py5.text_font(font)
        py5.text("word", 10, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Py5Font is the font class for py5. To create a font to use with py5, use :doc:`py5functions_create_font_file`. This will create a font in the format py5 requires. Py5 displays fonts using the .vlw font format, which uses images for each letter, rather than defining them through vector data. The :doc:`sketch_load_font` function constructs a new font and :doc:`sketch_text_font` makes a font active. The :doc:`py5font_list` method creates a list of the fonts installed on the computer, which is useful information to use with the :doc:`sketch_create_font` function for dynamically converting fonts into a format to use with py5.

To create a new font dynamically, use the :doc:`sketch_create_font` function. Do not use the syntax ``Py5Font()``.

Underlying Processing class: `PFont <https://processing.org/reference/PFont.html>`_

The following methods and fields are provided:

.. include:: include_py5font.rst

Updated on September 01, 2022 16:36:02pm UTC

