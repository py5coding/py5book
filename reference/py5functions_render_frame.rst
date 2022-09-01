render_frame()
==============

Helper function to render a single frame using the passed ``draw`` function argument.

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

    def draw_message(s: py5.Sketch):
        s.background(255)
        s.fill(255, 0, 0)
        s.text_size(20)
        s.text_align(s.CENTER, s.CENTER)
        s.text('hello world', s.width/2, s.height/2)

    frame = py5.render_frame(draw_message, 400, 200)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def draw_message(s: py5.Sketch, message='hello world', color=(255, 0, 0)):
        s.background(255)
        s.fill(*color)
        s.text_size(20)
        s.text_align(s.CENTER, s.CENTER)
        s.text(message, s.width/2, s.height/2)

    frame = py5.render_frame(draw_message, 400, 200, py5.P2D,
                             draw_args=('I LIKE ORANGE THINGS',),
                             draw_kwargs=dict(color=(255, 128, 0)))

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def random_squares(g: py5.Py5Graphics):
        for _ in range(10):
            g.rect(np.random.randint(g.width), np.random.randint(g.height), 10, 10)

    frame = py5.render_frame(random_squares, 100, 100, use_py5graphics=True)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Helper function to render a single frame using the passed ``draw`` function argument. The output is returned as a ``PIL.Image`` object.

The passed function's first parameter must be either a ``py5.Sketch`` object or a ``py5.Py5Graphics`` object, depending on the parameter ``use_py5graphics``. That object must be used for all of the function's py5 commands. The function can have additional positional and keyword arguments. To use them, pass the desired values as ``render_frame``'s ``draw_args`` and ``draw_kwargs`` arguments.

On OSX, only the default renderer is currently supported. Other platforms support the default renderer and the OpenGL renderers (P2D and P3D).

The rendered frame can have transparent pixels if and only if the ``use_py5graphics`` parameter is ``True`` because only a ``py5.Py5Graphics`` object can create an image with transparency. There is no need to call :doc:`py5graphics_begin_draw` or :doc:`py5graphics_end_draw` in the passed function as ``render_frame()`` does that for you.

This function facilitates the creation and execution of a py5 Sketch, and as a result makes it easy to run a Sketch inside of another Sketch. This is discouraged, and may fail catastrophically.

This function is available in decorator form as :doc:`py5functions_render`.

Signatures
----------

.. code:: python

    render_frame(
        draw: Callable,  # function that executes py5 draw commands
        width: int,  # width of the display window in units of pixels
        height: int,  # height of the display window in units of pixels
        renderer: str = Sketch.HIDDEN,  # rendering engine to use
        *,
        draw_args: tuple = None,  # additional positional arguments to pass to draw function
        draw_kwargs: dict = None,  # additional keyword arguments to pass to draw function
        use_py5graphics: bool = False  # pass a py5graphics object instead of a sketch object
    ) -> Image

Updated on September 01, 2022 14:08:27pm UTC

