has_thread()
============

Determine if a thread of a given name exists and is currently running.

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

    import time


    def slow_thread():
        py5.println('starting slow thread')
        time.sleep(7)
        py5.println('finishing slow thread')


    def setup():
        py5.launch_thread(slow_thread, name='slow thread')


    def draw():
        if py5.has_thread('slow thread'):
            py5.background(0, 255, 0)
        else:
            py5.background(255, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Determine if a thread of a given name exists and is currently running. You can get the list of all currently running threads with :doc:`sketch_list_threads`.

Syntax
------

.. code:: python

    has_thread(name: str) -> None

Parameters
----------

* **name**: `str` - name of thread


Updated on September 11, 2021 16:51:34pm UTC

