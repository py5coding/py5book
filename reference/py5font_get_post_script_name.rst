Py5Font.get_post_script_name()
==============================

Get the font's postscript name.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Font_get_post_script_name_0.png
    :alt: example picture for get_post_script_name()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        font = py5.create_font('DejaVu Sans', 15)
        py5.text_font(font)

        py5.text(font.get_name(), 5, 20)
        py5.text(font.get_post_script_name(), 5, 40)
        py5.text(font.get_size(), 5, 60)
        py5.text(font.get_default_size(), 5, 80)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Get the font's postscript name.

Underlying Processing method: PFont.getPostScriptName

Syntax
------

.. code:: python

    get_post_script_name() -> str

Updated on November 12, 2021 11:30:58am UTC

