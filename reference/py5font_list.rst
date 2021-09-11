Py5Font.list()
==============

Gets a list of the fonts installed on the system.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    font_list = py5.Py5Font.list()
    py5.println(font_list)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Gets a list of the fonts installed on the system. The data is returned as a list of strings. This list provides the names of each font for input into :doc:`sketch_create_font`, which allows py5 to dynamically format fonts.

This works outside of a running Sketch.

Underlying Java method: `PFont.list <https://processing.org/reference/PFont_list_.html>`_

Syntax
------

.. code:: python

    list() -> List[str]

Updated on September 11, 2021 16:51:34pm UTC

