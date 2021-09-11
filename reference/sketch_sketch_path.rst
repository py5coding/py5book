sketch_path()
=============

The Sketch's current path.

Description
-----------

The Sketch's current path. If the ``where`` parameter is used, the result will be a subdirectory of the current path. 

Result will be relative to Python's current working directory (``os.getcwd()``) unless it was specifically set to something else with the :doc:`sketch_run_sketch` call by including a ``--sketch-path`` argument in the ``py5_options`` parameters.

Underlying Java method: sketchPath

Syntax
------

.. code:: python

    sketch_path() -> Path
    sketch_path(where: str, /) -> Path

Parameters
----------

* **where**: `str` - subdirectories relative to the sketch path


Updated on September 11, 2021 16:51:34pm UTC

