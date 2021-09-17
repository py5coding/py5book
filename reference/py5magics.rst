Py5 Magics
==========

The py5 Magics are Jupyter Notebook "meta-commands" that can be within Jupyter Notebooks to enhance py5's ability to work within the notebook.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Magics_0.png
    :alt: example picture for Py5 Magics

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    %%py5draw 100 100
    py5.background(128)
    py5.fill(255, 0, 0)
    py5.rect(40, 50, 25, 25)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    %%py5drawsvg 200 200
    py5.background(128)
    py5.fill(255, 0, 0)
    py5.rect(80, 100, 50, 50)

.. raw:: html

    </div></div>

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

The py5 Magics are Jupyter Notebook "meta-commands" that can be within Jupyter Notebooks to enhance py5's ability to work within the notebook. The py5 magics will enable users to create Sketches and embed the results in the Notebook without defining any functions or calling the :doc:`sketch_size` function.

The following magics are provided:

.. include:: include_py5magics.rst

Updated on September 16, 2021 14:31:43pm UTC

