# User Functions

## Animated Sketches

The foundation of animated py5 Sketches are the `setup()` and `draw()` user functions. The `setup()` function is called once when the Sketch begins running and the `draw()` function gets called repeatedly in (usually) regular intervals.

Here is a straightforward example:

```python
def setup():
    py5.size(500, 500)
    py5.frame_rate(30)
    py5.rect_mode(py5.CENTER)
    py5.fill(255, 0, 0)


def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)
```

Here, the `setup()` function executes py5 commands that only need to be executed once. The [](/reference/sketch_size) method creates the Sketch window and sets the window's width and height. The [](/reference/sketch_frame_rate) method tells py5 the speed at which to call the `draw()` method. In this case, it will be called 30 times a second. And finally, the [](/reference/sketch_fill) method sets the shape fill color to red.

Code that you want to be called once should be placed in the `setup()` function. Typically this code will do things like load image assets and set drawing styles.

Code that you want to be called repeatedly should be placed in the `draw()` method. Typically this code will draw to the Sketch window, as well as supporting Python code that determines what should be drawn.

Within the `setup()` function, the [](/reference/sketch_frame_count) property will be zero. In the `draw()` function, it will be one or more.

## Static Sketches

A py5 Sketch need not be animated; you can also create static Sketches by omitting the `draw()` function. For example:

```python
def setup():
    py5.size(500, 500)
    py5.frame_rate(30)
    py5.rect_mode(py5.CENTER)
    py5.fill(255, 0, 0)

    for _ in range(10):
        py5.rect(py5.random(500), py5.random(500), 10, 10)

    py5.save('/tmp/static_sketch.png')
```

This Sketch is similar to the previous one except it will draw 10 random rectangles and then stop drawing.

For static Sketches, code that you would typically see in the `draw()` function is placed in the `setup()` function. This technique is useful for creating static images.

## Settings

There is a little bit of magic taking place within the `setup()` function. Before executing your Sketch, py5 will split the user's `setup()` function into its own `settings()` and `setup()` functions. For our previous example, the new code would be:

```python
def setttings():
    py5.size(500, 500)


def setup():
    py5.frame_rate(30)
    py5.rect_mode(py5.CENTER)
    py5.fill(255, 0, 0)

    for _ in range(10):
        py5.rect(py5.random(500), py5.random(500), 10, 10)

    py5.save('/tmp/static_sketch.png')
```

The call to [](/reference/sketch_size) is moved to a separate `settings()` function. The rest of the code remained in `setup()`.

This code transformation is facilitated by a few organizational rules about how the user must write their `setup()` function. The key rule is that the call to [](/reference/sketch_size) must be first, before the calls to methods like [](/reference/sketch_frame_rate) and [](/reference/sketch_fill). The other special methods that must be used at the beginning of `setup()`, before other code, are [](/reference/sketch_full_screen), [](/reference/sketch_smooth), [](/reference/sketch_no_smooth), and [](/reference/sketch_pixel_density). When the user's `setup()` function is organized in this way, py5 is able to reliably separate the code and divide it into two new functions.

The code separation process can manage the inclusion of global statements, comments, and docstrings. The recommended coding style for Python is to place global statements at the very beginning of a function or method, and py5 allows for that in user `setup()` functions. Here is an example that demonstrates this:

```python
def setup():
    # user setup function
    global shape
    py5.size(500, 500)
    py5.frame_rate(30)
    py5.rect_mode(py5.CENTER)
    shape = py5.create_shape(py5.RECT, 0, 0, 50, 50)


def draw():
    py5.background(204)
    py5.shape(shape, py5.mouse_x, py5.mouse_y)
```

For this example, the transformed code would be:

```python
def settings():
    # user setup function

    py5.size(500, 500)


def setup():

    global shape

    py5.frame_rate(30)
    py5.rect_mode(py5.CENTER)
    shape = py5.create_shape(py5.RECT, 0, 0, 50, 50)


def draw():
    py5.background(204)
    py5.shape(shape, py5.mouse_x, py5.mouse_y)
```

The vertical space you see in these `settings()` and `setup()` functions are there to ensure that any exceptions thrown by the executed code will point to the correct line numbers in the user's `setup()` function. This completes the illusion of the user's `setup()` function.

Why this might be useful, use variable to choose between fullscreen and window, etc

Class Mode, requires `settings()`

## Keyboard Events

`key_pressed()`
`key_typed()`
`key_released()`

Mention `Py5KeyEvent` objects

## Mouse Events

`mouse_clicked()`
`mouse_dragged()`
`mouse_moved()`
`mouse_entered()`
`mouse_exited()`
`mouse_pressed()`
`mouse_released()`
`mouse_wheel()`

Mention `Py5MouseEvent` objects

## Everything Else

### Window Events

`window_moved()`
`window_resized()`

### Sketch Exiting Event

`exiting()`

### Performance Improvement

`predraw_update()`

### Camera3D Support

`pre_draw()`
`post_draw()`

### Movie Events

`movie_event()`
