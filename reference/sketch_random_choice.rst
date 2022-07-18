random_choice()
===============

Select random items from a list.

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

Select random items from a list. The list items can be of any type. If multiple items are selected, this function will by default allow the same item to be selected multiple times. Set the ``replace`` parameter to ``False`` to prevent the same item from being selected multiple times.

This function's randomness can be influenced by :doc:`sketch_random_seed`, and makes calls to numpy to select the random items.

Syntax
------

.. code:: python

    random_choice(objects: list[Any], size: int=1, replace: bool=True) -> Any

Parameters
----------

* **objects**: `list[Any]` - list of objects to choose from
* **replace**: `bool=True` - whether to select random items with or without replacement
* **size**: `int=1` - number of random items to select


Updated on July 18, 2022 17:22:20pm UTC

