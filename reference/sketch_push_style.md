# push_style()

The `push_style()` function saves the current style settings and [](sketch_pop_style) restores the prior settings.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for push_style()](/images/reference/Sketch_push_style_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.ellipse(0, 50, 33, 33)  # left circle
    
    py5.push_style()  # start a new style
    py5.stroke_weight(10)
    py5.fill(204, 153, 0)
    py5.ellipse(50, 50, 33, 33)  # middle circle
    py5.pop_style()  # restore original style
    
    py5.ellipse(100, 50, 33, 33)  # right circle
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for push_style()](/images/reference/Sketch_push_style_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.ellipse(0, 50, 33, 33)  # left circle
    
    with py5.push_style():  # start a new style
        py5.stroke_weight(10)
        py5.fill(204, 153, 0)
        py5.ellipse(33, 50, 33, 33)  # left-middle circle
        
        with py5.push_style():  # start another new style
            py5.stroke(0, 102, 153)
            py5.ellipse(66, 50, 33, 33)  # right-middle circle
    
    py5.ellipse(100, 50, 33, 33)  # right circle
```

</div></div>

</div>

## Description

The `push_style()` function saves the current style settings and [](sketch_pop_style) restores the prior settings. Note that these functions are always used together. They allow you to change the style settings and later return to what you had. When a new style is started with `push_style()`, it builds on the current style information. The `push_style()` and [](sketch_pop_style) method pairs can be nested to provide more control. (See the second example for a demonstration.)

The style information controlled by the following functions are included in the style: [](sketch_fill), [](sketch_stroke), [](sketch_tint), [](sketch_stroke_weight), [](sketch_stroke_cap), [](sketch_stroke_join), [](sketch_image_mode), [](sketch_rect_mode), [](sketch_ellipse_mode), [](sketch_shape_mode), [](sketch_color_mode), [](sketch_text_align), [](sketch_text_font), [](sketch_text_mode), [](sketch_text_size), [](sketch_text_leading), [](sketch_emissive), [](sketch_specular), [](sketch_shininess), and [](sketch_ambient).

This method can be used as a context manager to ensure that [](sketch_pop_style) always gets called, as shown in the last example.

Underlying Processing method: [pushStyle](https://processing.org/reference/pushStyle_.html)

## Signatures

```python
push_style() -> None
```

Updated on March 06, 2023 02:49:26am UTC
