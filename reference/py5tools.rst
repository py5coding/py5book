Py5 Tools
=========

The py5 Tools are extra utility functions not directly related to creating Sketches that help faciliate the use of py5.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    import py5_tools

    print(py5_tools.get_jvm_debug_info())

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    import py5_tools

    py5_tools.add_jars('path/to/project_jars')
    py5_tools.add_classpath('path/to/jar/file/java_code.jar')

    import py5

    py5.println(py5_tools.get_classpath())

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The py5 Tools are extra utility functions not directly related to creating Sketches that help faciliate the use of py5. For example, you can use these to add jar files to the Java classpath before importing py5. All of the py5 Tools are in the Python package ``py5_tools``, which are installed alongside py5 but must be explicitly imported before using them. The ``py5_tools`` package is imported for you when coding in imported mode such as with the py5 Jupyter Notebook kernel.

The following functions are provided:

.. include:: include_py5tools.rst

Updated on September 01, 2022 16:36:02pm UTC

