py5_tools.get_classpath()
=========================

Get the Java classpath.

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

Get the Java classpath. If the JVM has not yet started, this will list the jars that have been added with :doc:`py5tools_add_classpath` and :doc:`py5tools_add_jars`. After the JVM has started, the classpath cannot be changed and the aformentioned functions would throw a ``RuntimeError``. Use :doc:`py5tools_is_jvm_running` to first determine if the JVM is running.

Signatures
----------

.. code:: python

    get_classpath() -> str

Updated on September 01, 2022 14:08:27pm UTC

