# is_key_pressed

The `is_key_pressed` variable stores whether or not a keyboard button is currently being pressed.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
# click on the window to give it focus,
# and press the 'b' key.

def draw():
    if py5.is_key_pressed:
        if py5.key in ['b', 'B']:
           py5.fill(0)
    else:
        py5.fill(255)

    py5.rect(25, 25, 50, 50)
```

</div></div>

</div>

## Description

The `is_key_pressed` variable stores whether or not a keyboard button is currently being pressed. The value is true when `any` keyboard button is pressed, and false if no button is pressed. The [](sketch_key) variable and [](sketch_key_code) variables (see the related reference entries) can be used to determine which button has been pressed.

Updated on March 06, 2023 02:49:26am UTC
