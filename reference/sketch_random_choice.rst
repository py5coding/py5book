random_choice()
===============

Select a random item from a list.

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

    def setup():
        words = ["apple", "bear", "cat", "dog"]
        word = py5.random_choice(words)
        py5.println(word)  # Prints one of the four words

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Select a random item from a list. The list items can be of any type. This function's randomness can be influenced by :doc:`sketch_random_seed`.

This function makes calls to numpy to select the random items.

Syntax
------

.. code:: python

    random_choice(objects: List[Any]) -> Any

Parameters
----------

* **objects**: `List[Any]` - list of objects to choose from


Updated on September 11, 2021 16:51:34pm UTC

