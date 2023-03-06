# Py5Shape.get_kind()

Get the Py5Shape object's "kind" number.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_kind()](/images/reference/Py5Shape_get_kind_0.png)

</div><div class="example-cell-code">

```python
# this is just a subset of the possible values
PY5SHAPE_KIND_VALS = {py5.Py5Shape.GROUP: 'GROUP',
                      py5.Py5Shape.ELLIPSE: 'ELLIPSE'}


def setup():
    s = py5.load_shape("bot.svg")
    for child in s.get_children():
        py5.println(PY5SHAPE_KIND_VALS[child.get_kind()])

    py5.background(192)
    py5.scale(0.25)
    py5.shape(s, py5.width//2, py5.height//2)
```

</div></div>

</div>

## Description

Get the Py5Shape object's "kind" number.

Underlying Processing method: PShape.getKind

## Signatures

```python
get_kind() -> int
```

Updated on March 06, 2023 02:49:26am UTC
