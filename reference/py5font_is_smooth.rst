Py5Font.is_smooth()
===================

Boolean value reflecting if smoothing (anti-aliasing) was used when the font was created.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Font_is_smooth_0.png
    :alt: example picture for is_smooth()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        font1 = py5.create_font('DejaVu Sans', 45)
        font2 = py5.create_font('DejaVu Sans', 45, False)

        py5.text_font(font1)
        py5.println(font1.is_smooth())
        py5.text('py5', 10, 40)

        py5.println(font2.is_smooth())
        py5.text_font(font2)
        py5.text('py5', 10, 90)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Boolean value reflecting if smoothing (anti-aliasing) was used when the font was created. By default, :doc:`sketch_create_font` will use smoothing.

Underlying Processing method: PFont.isSmooth

Signatures
----------

.. code:: python

    is_smooth() -> bool

Updated on September 01, 2022 14:08:27pm UTC

