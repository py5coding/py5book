key_code
========

The variable ``key_code`` is used to detect special keys such as the arrow keys (``UP``, ``DOWN``, ``LEFT``, and ``RIGHT``) as well as ``ALT``, ``CONTROL``, and ``SHIFT``.

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

    fill_val = 128


    def draw():
        py5.fill(fill_val)
        py5.rect(25, 25, 50, 50)


    def key_pressed():
        global fill_val
        if py5.key == py5.CODED:
            if py5.key_code == py5.UP:
                fill_val = 255
            elif py5.key_code == py5.DOWN:
                fill_val = 0

        else:
            fill_val = 126

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The variable ``key_code`` is used to detect special keys such as the arrow keys (``UP``, ``DOWN``, ``LEFT``, and ``RIGHT``) as well as ``ALT``, ``CONTROL``, and ``SHIFT``.

When checking for these keys, it can be useful to first check if the key is coded. This is done with the conditional ``if (key == CODED)``, as shown in the example.

The keys included in the ASCII specification (``BACKSPACE``, ``TAB``, ``ENTER``, ``RETURN``, ``ESC``, and ``DELETE``) do not require checking to see if the key is coded; for those keys, you should simply use the :doc:`sketch_key` variable directly (and not ``key_code``).  If you're making cross-platform projects, note that the ``ENTER`` key is commonly used on PCs and Unix, while the ``RETURN`` key is used on Macs. Make sure your program will work on all platforms by checking for both ``ENTER`` and ``RETURN``.

For those familiar with Java, the values for ``UP`` and ``DOWN`` are simply shorter versions of Java's ``key_event.VK_UP`` and ``key_event.VK_DOWN``. Other ``key_code`` values can be found in the Java KeyEvent reference.

There are issues with how ``key_code`` behaves across different renderers and operating systems. Watch out for unexpected behavior as you switch renderers and operating systems and you are using keys are aren't mentioned in this reference entry.

If you are using ``P2D`` or ``P3D`` as your renderer, use the ``NEWT`` KeyEvent constants.

Underlying Processing field: `keyCode <https://processing.org/reference/keyCode.html>`_


Updated on November 12, 2021 11:30:58am UTC

