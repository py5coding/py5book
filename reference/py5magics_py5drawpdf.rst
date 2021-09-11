%%py5drawpdf
============

Create a PDF with py5.

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

    %%py5drawpdf 200 200 /tmp/test.pdf
    py5.background(128)
    py5.fill(255, 0, 0)
    py5.rect(80, 100, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Create a PDF with py5.

For users who are familiar with Processing and py5 programming, you can pretend the code in this cell will be executed in a Sketch with no ``draw()`` function and your code in the ``setup()`` function. It will use the ``PDF`` renderer.

As this is creating a PDF, you cannot do operations on the :doc:`sketch_pixels` or :doc:`sketch_np_pixels` arrays. Use :doc:`py5magics_py5draw` instead.

Code used in this cell can reference functions and variables defined in other cells. By default, variables and functions created in this cell will be local to only this cell because to do otherwise would be unsafe. If you understand the risks, you can use the ``global`` keyword to add a single function or variable to the notebook namespace or the ``--unsafe`` argument to add everything to the notebook namespace. Either option may be very useful to you, but be aware that using py5 objects in a different notebook cell or reusing them in another Sketch can result in nasty errors and bizzare consequences.

Usage
-----

.. code::

    %%py5drawpdf [--unsafe] width height filename

Arguments
---------

.. code::

    positional arguments:
      width     width of PDF output
      height    height of PDF output
      filename  filename for PDF output

    optional arguments:
      --unsafe  allow new variables to enter the global namespace

Updated on September 11, 2021 16:51:34pm UTC

