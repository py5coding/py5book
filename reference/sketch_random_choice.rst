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

Signatures
----------

.. code:: python

    random_choice(
        objects: list[Any],  # list of objects to choose from
        size: int = 1,  # number of random items to select
        replace: bool = True,  # whether to select random items with or without replacement
    ) -> Any

Updated on September 01, 2022 14:08:27pm UTC

