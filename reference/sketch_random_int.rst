random_int()
============

Generates random integers.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        words = ["apple", "bear", "cat", "dog"]
        index = py5.random_int(len(words)-1)
        py5.println(words[index])  # Prints one of the four words

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Generates random integers. Each time the ``random_int()`` function is called, it returns an unexpected integer within the specified range. This function's randomness can be influenced by :doc:`sketch_random_seed`.

If no parameters are passed to the function, it will return either 0 or 1. Recall that in a Python boolean expression, 0 evaluates to ``False`` and 1 evaluates to ``True``. This is equivalent to a coin toss.

If only one parameter is passed to the function, it will return an integer between zero and the value of the ``high`` parameter, inclusive. For example, ``random(5)`` returns one of 0, 1, 2, 3, 4, or 5.

If two parameters are specified, the function will return an integer with a value between the two values, inclusive. For example, ``random(2, 5)`` returns one of 2, 3, 4, or 5.

If you want to pick a random object from a list, recall that Python uses zero-indexing, so the first index value is 0 and the final index value is one less than the list length. Therefore, to pick a random index to use in the list ``words``, your code should be ``random_int(len(words)-1)``. Omitting the ``-1`` will (occasionally) result in an index out of range error. Alternatively, you can also use :doc:`sketch_random_choice` to pick a random object from a list.

This function makes calls to numpy to generate the random integers.

Signatures
----------

.. code:: python

    random_int() -> int

    random_int(
        high: int,  # upper limit
        /,
    ) -> int

    random_int(
        low: int,  # lower limit
        high: int,  # upper limit
        /,
    ) -> int

Updated on September 01, 2022 16:36:02pm UTC

