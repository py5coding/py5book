# Py5Graphics.np_pixels[]

The `np_pixels[]` array contains the values for all the pixels in the Py5Graphics drawing surface.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for np_pixels[]](/images/reference/Py5Graphics_np_pixels_0.png)

</div><div class="example-cell-code">

```python
def setup():
    g = py5.create_graphics(80, 80)
    g.begin_draw()
    g.background(255)
    g.rect(10, 10, 60, 60)
    g.load_np_pixels()
    g.np_pixels[:, 40:, 1:] = [255, 0, 0]
    g.update_np_pixels()
    g.end_draw()
    py5.image(g, 10, 10)
```

</div></div>

</div>

## Description

The `np_pixels[]` array contains the values for all the pixels in the Py5Graphics drawing surface. Unlike the one dimensional array [](py5graphics_pixels), the `np_pixels[]` array organizes the color data in a 3 dimensional numpy array. The size of the array's dimensions are defined by the size of the Py5Graphics drawing surface. The first dimension is the height, the second is the width, and the third represents the color channels. The color channels are ordered alpha, red, green, blue (ARGB). Every value in `np_pixels[]` is an integer between 0 and 255.

This numpy array is very similar to the image arrays used by other popular Python image libraries, but note that some of them like opencv will by default order the color channels as RGBA.

When the pixel density is set to higher than 1 with the [](py5graphics_pixel_density) function, the size of `np_pixels[]`'s height and width dimensions will change. See the reference for [](py5graphics_pixel_width) or [](py5graphics_pixel_height) for more information. Nothing about `np_pixels[]` will change as a result of calls to [](py5graphics_color_mode). 

Much like the [](py5graphics_pixels) array, there are load and update methods that must be called before and after making changes to the data in `np_pixels[]`. Before accessing `np_pixels[]`, the data must be loaded with the [](py5graphics_load_np_pixels) method. If this is not done, `np_pixels` will be equal to `None` and your code will likely result in Python exceptions. After `np_pixels[]` has been modified, the [](py5graphics_update_np_pixels) method must be called to update the content of the Py5Graphics drawing surface.

Working with [](py5graphics_np_pixels) can only be done between calls to [](py5graphics_begin_draw) and [](py5graphics_end_draw).

To set the entire contents of `np_pixels[]` to the contents of another properly sized numpy array, consider using [](py5graphics_set_np_pixels).

Look at the online ["Numpy, Arrays, and Images"](/integrations/numpy) Python Ecosystem Integration tutorial for more information about how to make best use of `np_pixels[]`.

This field is the same as [](sketch_np_pixels) but linked to a `Py5Graphics` object.

Updated on December 25, 2023 17:02:43pm UTC
