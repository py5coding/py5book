# pixels[]

The `pixels[]` array contains the values for all the pixels in the display window.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for pixels[]](/images/reference/Sketch_pixels_0.png)

</div><div class="example-cell-code">

```python
def setup():
    pink = "#F6C"
    py5.load_pixels()
    for i in range(0, (py5.width*py5.height//2) - py5.width//2):
        py5.pixels[i] = pink
    
    py5.update_pixels()
```

</div></div>

</div>

## Description

The `pixels[]` array contains the values for all the pixels in the display window. These values are of the color datatype. This array is defined by the size of the display window. For example, if the window is 100 x 100 pixels, there will be 10,000 values and if the window is 200 x 300 pixels, there will be 60,000 values. When the pixel density is set to higher than 1 with the [](sketch_pixel_density) function, these values will change. See the reference for [](sketch_pixel_width) or [](sketch_pixel_height) for more information. 

Before accessing this array, the data must loaded with the [](sketch_load_pixels) function. Failure to do so may result in a Java `NullPointerException`. Subsequent changes to the display window will not be reflected in `pixels` until [](sketch_load_pixels) is called again. After `pixels` has been modified, the [](sketch_update_pixels) function must be run to update the content of the display window.

Underlying Processing field: [pixels](https://processing.org/reference/pixels.html)

Updated on March 06, 2023 02:49:26am UTC
