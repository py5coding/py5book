list_threads()
==============

List the names of all of the currently running threads.

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

    def thread1():
        py5.println('thread 1')


    def thread2():
        py5.println('thread 2')


    def setup():
        py5.frame_rate(10)
        py5.launch_repeating_thread(thread1, name='thread 1', time_delay=1.2)
        py5.launch_repeating_thread(thread2, name='thread 2', time_delay=1.8)


    def draw():
        py5.println('running threads:', ', '.join(py5.list_threads()))
        if py5.frame_count == 50:
            py5.stop_all_threads()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

List the names of all of the currently running threads. The names of previously launched threads that have exited will be removed from the list.

Signatures
------

.. code:: python

    list_threads() -> None
Updated on August 25, 2022 20:01:47pm UTC

