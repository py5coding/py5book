# intercept_escape()

Prevent the Escape key from causing the Sketch to exit.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(200, 200)

def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)

def key_pressed():
    if py5.key == py5.ESC:
        # this code will not work:
        # py5.key = 'x'

        py5.intercept_escape()

    # verify py5.key has not changed
    assert py5.key == py5.ESC
```

</div></div>

</div>

## Description

Prevent the Escape key from causing the Sketch to exit. Normally hitting the Escape key (`ESC`) will cause the Sketch to exit. In Processing, one can write code to change the Escape key's behavior by changing the [](sketch_key) value to something else, perhaps with code similar to `py5.key = 'x'`. That code won't work in py5 because py5 does not allow the user to alter the value of [](sketch_key) like Processing does. The `intercept_escape()` method was created to allow users to achieve the same goal of preventing the Escape key from causing the Sketch to exit.

The `intercept_escape()` method will only do something when [](sketch_key) already equals `ESC`. This function should only be called from the user event functions `key_pressed()`, `key_typed()`, and `key_released()`.

This method will not alter the value of [](sketch_key). This method cannot prevent a Sketch from exiting when the exit is triggered by any other means, such as a call to [](sketch_exit_sketch) or the user closes the window.

## Signatures

```python
intercept_escape() -> None
```

Updated on November 22, 2024 04:29:37am UTC
