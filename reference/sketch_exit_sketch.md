# exit_sketch()

Quits/stops/exits the program.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def draw():
    py5.line(py5.mouse_x, py5.mouse_y, 50, 50)


def mouse_pressed():
    py5.exit_sketch()
```

</div></div>

</div>

## Description

Quits/stops/exits the program. Programs without a `draw()` function stop automatically after the last line has run, but programs with `draw()` run continuously until the program is manually stopped or `exit_sketch()` is run.

Rather than terminating immediately, `exit_sketch()` will cause the Sketch to exit after `draw()` has completed (or after `setup()` completes if called during the `setup()` function).

For Python programmers, this is *not* the same as `sys.exit()`. Further, `sys.exit()` should not be used because closing out an application while `draw()` is running may cause a crash (particularly with `P3D`).

Underlying Processing method: [exit](https://processing.org/reference/exit_.html)

## Signatures

```python
exit_sketch() -> None
```

Updated on March 07, 2023 15:37:49pm UTC
