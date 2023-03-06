# @render()

Decorator function to render a single frame using the decorated `draw` function.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
@py5.render(400, 200)
def draw_message(s: py5.Sketch):
    s.background(255)
    s.fill(255, 0, 0)
    s.text_size(20)
    s.text_align(s.CENTER, s.CENTER)
    s.text('hello world', s.width/2, s.height/2)

frame = draw_message()
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
@py5.render(400, 200, py5.P2D)
def draw_message(s: py5.Sketch, message='hello world', color=(255, 0, 0)):
    s.background(255)
    s.fill(*color)
    s.text_size(20)
    s.text_align(s.CENTER, s.CENTER)
    s.text(message, s.width/2, s.height/2)

frame = draw_message('I LIKE ORANGE THINGS', color=(255, 128, 0))
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
@py5.render(100, 100, use_py5graphics=True)
def random_squares(g: py5.Py5Graphics):
    for _ in range(10):
        g.rect(np.random.randint(g.width), np.random.randint(g.height), 10, 10)

frame = random_squares()
```

</div></div>

</div>

## Description

Decorator function to render a single frame using the decorated `draw` function. The output is returned as a `PIL.Image` object.

The decorated draw function's first parameter must be either a `py5.Sketch` object or a `py5.Py5Graphics` object, depending on the parameter `use_py5graphics`. That object must be used for all of the function's py5 commands. The function can have additional positional and keyword arguments. To use them, pass the desired values when you call the decorated function as you would to any other Python function.

On OSX, only the default renderer is currently supported. Other platforms support the default renderer and the OpenGL renderers (P2D and P3D).

The rendered frame can have transparent pixels if and only if the `use_py5graphics` parameter is `True` because only a `py5.Py5Graphics` object can create an image with transparency. There is no need to call [](py5graphics_begin_draw) or [](py5graphics_end_draw) in the decorated function as `@render()` does that for you.

This function facilitates the creation and execution of a py5 Sketch, and as a result makes it easy to run a Sketch inside of another Sketch. This is discouraged, and may fail catastrophically.

This function is available in non-decorator form as [](py5functions_render_frame).

## Signatures

```python
render(
    width: int,  # width of the display window in units of pixels
    height: int,  # height of the display window in units of pixels
    renderer: str = Sketch.HIDDEN,  # rendering engine to use
    use_py5graphics: bool = False,  # pass a py5graphics object instead of a sketch object
) -> Image
```

Updated on March 06, 2023 02:49:26am UTC
