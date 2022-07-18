np_random
=========

Access the numpy random number generator that py5 uses to provide random number functionality.

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
        py5.np_random.shuffle(words)
        # Prints the words in a random order
        for word in words:
            py5.println(word)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Access the numpy random number generator that py5 uses to provide random number functionality. Py5 uses a numpy random number generator to provide a breadth of random number functions such as :doc:`sketch_random_choice`, :doc:`sketch_random_gaussian`, and :doc:`sketch_random_int`. The functions py5 provides are the ones you are most likely to need, but numpy is capable of much more than what py5 makes available. Access this property to access all of numpy's random number functions.

All of the random numbers generated through this property can be influenced by :doc:`sketch_random_seed`.


Updated on July 18, 2022 17:22:20pm UTC

