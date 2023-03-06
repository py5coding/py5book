# end_raw()

Complement to [](sketch_begin_raw); they must always be used together.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(400, 400, py5.P2D)
    py5.begin_raw(py5.PDF, "raw.pdf")


def draw():
    py5.line(py5.pmouse_x, py5.pmouse_y, py5.mouse_x, py5.mouse_y)


def key_pressed():
    if py5.key == ' ':
        py5.end_raw()
        py5.exit_sketch()
```

</div></div>

</div>

## Description

Complement to [](sketch_begin_raw); they must always be used together. See the [](sketch_begin_raw) reference for details.

Underlying Processing method: [endRaw](https://processing.org/reference/endRaw_.html)

## Signatures

```python
end_raw() -> None
```

Updated on March 06, 2023 02:49:26am UTC
