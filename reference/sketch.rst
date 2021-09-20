Sketch
======

Core py5 class for leveraging py5's functionality.

Description
-----------

Core py5 class for leveraging py5's functionality. This is analogous to the PApplet class in Processing. Launch the Sketch with the :doc:`sketch_run_sketch` method.

The core functions to be implemented by the py5 coder are ``settings``, ``setup``, and ``draw``. The first two will be run once at Sketch initialization and the third will be run in an animation thread, once per frame. The following event functions are also supported: 

    * ``key_pressed``
    * ``key_typed``
    * ``key_released``
    * ``mouse_clicked``
    * ``mouse_dragged``
    * ``mouse_moved``
    * ``mouse_entered``
    * ``mouse_exited``
    * ``mouse_pressed``
    * ``mouse_released``
    * ``mouse_wheel``
    * ``exiting``

When coding in class mode, all of the above functions should be class methods. When coding in module mode or imported mode, the above functions should be stand-alone functions available in the local namespace in which :doc:`sketch_run_sketch` was called.

Underlying Java class: PApplet

The following methods and fields are provided:

.. include:: include_sketch.rst

Updated on September 20, 2021 11:55:29am UTC

