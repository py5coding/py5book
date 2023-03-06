# loop()

By default, py5 loops through `draw()` continuously, executing the code within it.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
x = 0


def setup():
    py5.size(200, 200)
    py5.no_loop()  # draw() will not loop


def draw():
    global x
    py5.background(204)
    x = x + .1
    if x > py5.width:
        x = 0

    py5.line(x, 0, x, py5.height)


def mouse_pressed():
    py5.loop()  # holding down the mouse activates looping


def mouse_released():
    py5.no_loop()  # releasing the mouse stops looping draw()
```

</div></div>

</div>

## Description

By default, py5 loops through `draw()` continuously, executing the code within it. However, the `draw()` loop may be stopped by calling [](sketch_no_loop). In that case, the `draw()` loop can be resumed with `loop()`.

Underlying Processing method: [loop](https://processing.org/reference/loop_.html)

## Signatures

```python
loop() -> None
```

Updated on March 06, 2023 02:49:26am UTC
