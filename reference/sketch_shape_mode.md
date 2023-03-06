# shape_mode()

Modifies the location from which shapes draw.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for shape_mode()](/images/reference/Sketch_shape_mode_0.png)

</div><div class="example-cell-code">

```python
def setup():
    global bot
    bot = py5.load_shape("bot.svg")


def draw():
    py5.shape_mode(py5.CENTER)
    py5.shape(bot, 35, 35, 50, 50)
    py5.shape_mode(py5.CORNER)
    py5.shape(bot, 35, 35, 50, 50)
```

</div></div>

</div>

## Description

Modifies the location from which shapes draw. The default mode is `shape_mode(CORNER)`, which specifies the location to be the upper left corner of the shape and uses the third and fourth parameters of [](sketch_shape) to specify the width and height. The syntax `shape_mode(CORNERS)` uses the first and second parameters of [](sketch_shape) to set the location of one corner and uses the third and fourth parameters to set the opposite corner. The syntax `shape_mode(CENTER)` draws the shape from its center point and uses the third and forth parameters of [](sketch_shape) to specify the width and height. The parameter must be written in ALL CAPS because Python is a case sensitive language.

Underlying Processing method: [shapeMode](https://processing.org/reference/shapeMode_.html)

## Signatures

```python
shape_mode(
    mode: int,  # either CORNER, CORNERS, CENTER
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
