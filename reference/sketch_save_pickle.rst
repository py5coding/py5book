save_pickle()
=============

Pickle a Python object to a file.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    data = dict(mouse_x=[], mouse_y=[])

    def setup():
        py5.size(250, 250)
        py5.stroke_weight(10)


    def draw():
        data['mouse_x'].append(py5.mouse_x)
        data['mouse_y'].append(py5.mouse_y)
        py5.point(py5.mouse_x, py5.mouse_y)
        if py5.frame_count == 600:
            py5.save_pickle(data, 'data/mouse_positions.pkl')
            py5.exit_sketch()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Pickle a Python object to a file. If ``filename`` is not an absolute path, it will be saved relative to the current working directory (:doc:`sketch_sketch_path`). The saved file can be reloaded with :doc:`sketch_load_pickle`.

Object "pickling" is a method for serializing objects and saving them to a file for later retrieval. The recreated objects will be clones of the original objects. Not all Python objects can be saved to a Python pickle file. This limitation prevents any py5 object from being pickled.

Underlying Processing method: savePickle

Signatures
----------

.. code:: python

    save_pickle(
        obj: Any,  # any non-py5 Python object
        filename: Union[str, Path],  # filename to save pickled object to
    ) -> None

Updated on November 19, 2022 01:41:50am UTC

