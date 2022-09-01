py5_tools.add_options()
=======================

Provide JVM options to use when the JVM starts.

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
    py5_tools.add_options('-Xmx4096m')
    import py5

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Provide JVM options to use when the JVM starts. This is useful to set the JVM memory size, for example.

After the JVM has started, new options cannot be added. This function will throw a ``RuntimeError`` if it is called after the JVM has already started. Use :doc:`py5tools_is_jvm_running` to first determine if the JVM is running.

Signatures
----------

.. code:: python

    add_options(
        *options: list[str],
    ) -> None

Updated on September 01, 2022 14:08:27pm UTC

