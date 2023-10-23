---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# All About Colors

link to matplotlib

Somewhere in here I should document how color objects are printed to the terminal

## setup

To use all of the features documented on this page, you'll need to install the
matplotlib and colour libraries with pip or with conda.

```bash
pip install matplotlib colour
```

```bash
conda install matplotlib colour -c conda-forge
```

For more information, refer to the [colour library's documentation on github](https://github.com/vaab/colour)
or matplotlib's [Getting Started](https://matplotlib.org/stable/users/getting_started/)
page.

## hex codes

Use any hex code

as a string, 3, 4, 6, or 8 characters
3 - rgb
4 - rgba
6 - rrggbb
8 - rrggbbaa

Consistent with hex strings for web / html

eg: `#ff0000` for red

Can also use a hexidecimal integer, like so. For this, it is always `0x` followed
by 8 values, order is alpha, red, green, blue.

`0xffff0000`

## matplotlib colors

If you have matplotlib installed, any string that matplotlib accepts as a color
will work in py5.

However, this requires you to remember the names of colors and how to properly
spell them.

## builtin color names

`css4_colors`
`xkcd_colors`

## colour library

Color class

Uses RGB, HSL (not the same as HSB), hex, or web (css4 colors)

## matplotlib colormaps

Colormode based on matplotlib

```python
def setup():
    py5.color_mode(py5.CMAP, 'plasma', 100, 100)
```

Pass the name of any of matplotlib's builtin colormaps:

https://matplotlib.org/stable/gallery/color/colormap_reference.html

Or an actual Colormap instance, either from matplotlib library or from a 3rd
party library.

https://matplotlib.org/mpl-third-party/#colormaps-and-styles

Or you can create your own Colormap instance with your own color settings.
