# color_mode()

Changes the way py5 interprets color data.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for color_mode()](/images/reference/Sketch_color_mode_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.color_mode(py5.RGB, 100)
    for i in range(0, 100):
        for j in range(0, 100):
            py5.stroke(i, j, 0)
            py5.point(i, j)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for color_mode()](/images/reference/Sketch_color_mode_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.color_mode(py5.HSB, 100)
    for i in range(0, 100):
        for j in range(0, 100):
            py5.stroke(i, j, 100)
            py5.point(i, j)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for color_mode()](/images/reference/Sketch_color_mode_2.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.color_mode(py5.CMAP, py5.mpl_cmaps.VIRIDIS, 100)
    for i in range(0, 100):
        py5.stroke(i)
        py5.line(i, 0, i, 100)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for color_mode()](/images/reference/Sketch_color_mode_3.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.color_mode(py5.CMAP, py5.mpl_cmaps.VIRIDIS, 100, 100)
    py5.background("white")
    for i in range(0, 100):
        for j in range(0, 100):
            py5.stroke(i, j)
            py5.point(i, j)
```

</div></div>

</div>

## Description

Changes the way py5 interprets color data. By default, the parameters for [](sketch_fill), [](sketch_stroke), [](sketch_background), and [](sketch_color) are defined by values between 0 and 255 using the `RGB` color model. The `color_mode()` function is used to change the numerical range used for specifying colors and to switch color systems. For example, calling `color_mode(RGB, 1.0)` will specify that values are specified between 0 and 1. The limits for defining colors are altered by setting the parameters `max`, `max1`, `max2`, `max3`, and `max_a`.

After changing the range of values for colors with code like `color_mode(HSB, 360, 100, 100)`, those ranges remain in use until they are explicitly changed again. For example, after running `color_mode(HSB, 360, 100, 100)` and then changing back to `color_mode(RGB)`, the range for R will be 0 to 360 and the range for G and B will be 0 to 100. To avoid this, be explicit about the ranges when changing the color mode. For instance, instead of `color_mode(RGB)`, write `color_mode(RGB, 255, 255, 255)`.

If you have the matplotlib package (library) installed, py5 adds a `CMAP` mode, short for colormap. The main idea is to map a range of values to a range of colors in a matplotlib colormap palette. You can find the list of built-in colormaps in matplotlib’s [Colormap reference](https://matplotlib.org/stable/gallery/color/colormap_reference.html), which you can then select by passing a constant from `py5.mpl_cmaps` like this: `color_mode(CMAP, mpl_cmaps.OCEAN)`. You can learn more about colormaps in the <a href="/integrations/matplotlib.html#colormap-color-mode">matplotlib integrations documentation in the Charts, Plots, and Matplotlib - Colomap Color Mode section</a>.

Underlying Processing method: [colorMode](https://processing.org/reference/colorMode_.html)

## Signatures

```python
color_mode(
    colormap_mode: int,  # CMAP, activating matplotlib Colormap mode
    color_map: str,  # name of builtin matplotlib Colormap
    /,
) -> None

color_mode(
    colormap_mode: int,  # CMAP, activating matplotlib Colormap mode
    color_map: str,  # name of builtin matplotlib Colormap
    max_map: float,  # range for the color map
    /,
) -> None

color_mode(
    colormap_mode: int,  # CMAP, activating matplotlib Colormap mode
    color_map: str,  # name of builtin matplotlib Colormap
    max_map: float,  # range for the color map
    max_a: float,  # range for the alpha
    /,
) -> None

color_mode(
    colormap_mode: int,  # CMAP, activating matplotlib Colormap mode
    color_map_instance: Colormap,  # matplotlib.colors.Colormap instance
    /,
) -> None

color_mode(
    colormap_mode: int,  # CMAP, activating matplotlib Colormap mode
    color_map_instance: Colormap,  # matplotlib.colors.Colormap instance
    max_map: float,  # range for the color map
    /,
) -> None

color_mode(
    colormap_mode: int,  # CMAP, activating matplotlib Colormap mode
    color_map_instance: Colormap,  # matplotlib.colors.Colormap instance
    max_map: float,  # range for the color map
    max_a: float,  # range for the alpha
    /,
) -> None

color_mode(
    mode: int,  # Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness
    /,
) -> None

color_mode(
    mode: int,  # Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness
    max1: float,  # range for the red or hue depending on the current color mode
    max2: float,  # range for the green or saturation depending on the current color mode
    max3: float,  # range for the blue or brightness depending on the current color mode
    /,
) -> None

color_mode(
    mode: int,  # Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness
    max1: float,  # range for the red or hue depending on the current color mode
    max2: float,  # range for the green or saturation depending on the current color mode
    max3: float,  # range for the blue or brightness depending on the current color mode
    max_a: float,  # range for the alpha
    /,
) -> None

color_mode(
    mode: int,  # Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness
    max: float,  # range for all color elements
    /,
) -> None
```

Updated on October 05, 2025 17:47:38pm UTC
