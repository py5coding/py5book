# push()

The `push()` function saves the current drawing style settings and transformations, while [](sketch_pop) restores these settings.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for push()](/images/reference/Sketch_push_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.fill(255)
    py5.rect(0, 0, 50, 50)  # white rectangle
    
    py5.push()
    py5.translate(30, 20)
    py5.fill(0)
    py5.rect(0, 0, 50, 50)  # black rectangle
    py5.pop()  # restore original settings
    
    py5.fill(100)
    py5.rect(15, 10, 50, 50)  # gray rectangle
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for push()](/images/reference/Sketch_push_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.ellipse(0, 50, 33, 33)  # left circle
    
    with py5.push():
        py5.translate(50, 0)
        py5.stroke_weight(10)
        py5.fill(204, 153, 0)
        py5.ellipse(0, 50, 33, 33)  # middle circle
    
    py5.ellipse(100, 50, 33, 33)  # right circle
```

</div></div>

</div>

## Description

The `push()` function saves the current drawing style settings and transformations, while [](sketch_pop) restores these settings. Note that these functions are always used together. They allow you to change the style and transformation settings and later return to what you had. When a new state is started with `push()`, it builds on the current style and transform information.

`push()` stores information related to the current transformation state and style settings controlled by the following functions: [](sketch_rotate), [](sketch_translate), [](sketch_scale), [](sketch_fill), [](sketch_stroke), [](sketch_tint), [](sketch_stroke_weight), [](sketch_stroke_cap), [](sketch_stroke_join), [](sketch_image_mode), [](sketch_rect_mode), [](sketch_ellipse_mode), [](sketch_color_mode), [](sketch_text_align), [](sketch_text_font), [](sketch_text_mode), [](sketch_text_size), and [](sketch_text_leading).

The `push()` and [](sketch_pop) functions can be used in place of [](sketch_push_matrix), [](sketch_pop_matrix), [](sketch_push_style), and [](sketch_pop_style). The difference is that `push()` and [](sketch_pop) control both the transformations (rotate, scale, translate) and the drawing styles at the same time.

This method can be used as a context manager to ensure that [](sketch_pop) always gets called, as shown in the last example.

Underlying Processing method: [push](https://processing.org/reference/push_.html)

## Signatures

```python
push() -> None
```

Updated on March 06, 2023 02:49:26am UTC
