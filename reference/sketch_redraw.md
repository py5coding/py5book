# redraw()

Executes the code within `draw()` one time.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
x = 0


def setup():
    py5.size(200, 200)
    py5.no_loop()


def draw():
    py5.background(204)
    py5.line(x, 0, x, py5.height)


def mouse_pressed():
    x += 1
    py5.redraw()
```

</div></div>

</div>

## Description

Executes the code within `draw()` one time. This functions allows the program to update the display window only when necessary, for example when an event registered by `mouse_pressed()` or `key_pressed()` occurs. 

In structuring a program, it only makes sense to call `redraw()` within events such as `mouse_pressed()`. This is because `redraw()` does not run `draw()` immediately (it only sets a flag that indicates an update is needed). 

The `redraw()` function does not work properly when called inside `draw()`. To enable/disable animations, use [](sketch_loop) and [](sketch_no_loop).

Underlying Processing method: [redraw](https://processing.org/reference/redraw_.html)

## Signatures

```python
redraw() -> None
```

Updated on March 06, 2023 02:49:26am UTC
