---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Charts, Plots, and Matplotlib

[Matplotlib](https://matplotlib.org/) is a widely used library for creating
high quality static, animated, and interactive data visualizations. It has
a long history within the Python community. Matplotlib's contributions to
the scientific community cannot be understated. Integrating matplotlib into
py5 creates many exciting possibilities.

In the future, matplotlib will have even more integrations with py5, beyond
what is discussed here. Stay tuned!

## Setup

Install matplotlib with pip or with conda.

```bash
pip install matplotlib
```

```bash
conda install matplotlib -c conda-forge
```

Refer to matplotlib's [Getting Started](https://matplotlib.org/stable/users/getting_started/)
page or [Installation Guide](https://matplotlib.org/stable/users/installing/index.html)
for more information.

+++

## `Figure` Objects

Converting matplotlib Figure objects to Py5Image objects
with [](/reference/sketch_convert_image) is straightforward
but there are important performance considerations that
must be addressed to use this feature well.

### Example with Performance Problems

Let's start with an example that has some performance problems.
Understanding the performance problems is necessary to show
you how to use py5 and matplotlib together optimally. We
will work through the performance problems to demonstrate
better ways to use py5 and matplotlib in a Sketch.

To begin, we will import matplotlib and some other libraries
we will use for our examples.

```{code-cell} ipython3
from collections import deque

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

import py5_tools
import py5
```

Next we will set matplotlib's drawing style. There are
[many style sheets](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)
to choose from. Here we are using "ggplot" with the "fast" style to improve
[performance](https://matplotlib.org/stable/users/explain/artists/performance.html#using-the-fast-style).

We will not use the matplotlib Jupyter Notebook magic `%matplotlib inline`. It isn't necessary
for this example and it seems to confict with the code py5 uses to run correctly on OSX.

```{code-cell} ipython3
mpl.style.use(['ggplot', 'fast'])
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

For our example we will create a Sketch that plots its own frame rate. We will
collect the frame rate numbers in a special data structure called a
["deque"](https://docs.python.org/3/library/collections.html#collections.deque).
This data structure will store the most recent 250 frame rate observations.
It will do this automatically by removing old values as new values are added.
We will also pre-populate the deque with initial values of 60.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
frame_rates = deque([60] * 250, maxlen=250)
```

Next we will create a function for creating our matplotlib chart. As you can see,
this is a nice looking chart. New observations are added to the right side of
the chart. The data points get successively older as one moves from right to left.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def create_chart(frame_rates):
    figure, ax1 = plt.subplots(1, 1, figsize=(9, 9))
    line, = ax1.plot(range(-len(frame_rates), 0), frame_rates)
    ax1.set_ylim(0, 70)
    ax1.set_xlabel('framerate observations')
    ax1.set_ylabel('framerate per second')
    ax1.set_title('py5 sketch framerate')

    return figure, line


create_chart(frame_rates)
```

Finally, we will set the
[matplotlib backend](https://matplotlib.org/stable/users/explain/figure/backends.html)
to AGG. This backend is non-interactive. It is also faster
than the other backends, making it a good choice for our work with py5.

After setting this backend, matplotlib Figures will no longer
appear embedded in the notebook like you see for the Figure
created above.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
mpl.use('agg')
```

Now, the py5 Sketch. Here, we are creating a new chart in each execution of the
`draw()` method. The Figure object is converted to a Py5Image object using
[](/reference/sketch_convert_image).

Since each call to `draw()` creates a new Figure, we must close each figure with
`plt.close()` to control memory usage.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(950, 950)


def draw():
    frame_rates.append(py5.get_frame_rate())

    figure, _ = create_chart(frame_rates)
    chart = py5.convert_image(figure)
    plt.close(figure)

    py5.background(240)
    py5.image(chart, 25, 25)


py5.run_sketch()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
import time

time.sleep(15)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

This is slow. We can do better.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5_tools.screenshot()
```

### Performance Analysis

We will profile the `draw()` function to investigate why.

```{code-cell} ipython3
py5.profile_draw()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(10)
```

```{code-cell} ipython3
py5.print_line_profiler_stats()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

The Sketch is spending the majority of the time in [](/reference/sketch_convert_image). It is
also spendng a significant amount of time creating the Figure.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

### Improved Example

There are a few quick changes we can make to address this.

The first change is to create the Figure one and only one time in
`setup()`. We can then update the Figure's data with the line's
[`set_ydata()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata)
method. Creating the Figure object once and updating the data is a
much more efficient approach. Repeatedly creating matplotlib
Figures is in general a bad idea.

The second change is to recycle the Py5Image object. The
[](/reference/sketch_convert_image) method lets us provide a Py5Image
object to write the converted image data into. The Py5Image object must
be the correct size. Recycling one Py5Image object in this way is lets
us skip the repeated object creation of new Py5Image objects and garbage
collection of old Py5Image objects.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
frame_rates = deque([60] * 250, maxlen=250)


def setup():
    global figure, line, chart
    py5.size(950, 950)

    figure, line = create_chart(frame_rates)
    chart = py5.convert_image(figure)


def draw():
    frame_rates.append(py5.get_frame_rate())

    line.set_ydata(frame_rates)
    py5.convert_image(figure, dst=chart)

    py5.background(240)
    py5.image(chart, 25, 25)


py5.run_sketch()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(10)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

We can see this is significantly faster but still not the
Sketch performance we are looking for.

```{code-cell} ipython3
py5_tools.screenshot()
```

### Second Performance Analysis

We can again profile the `draw()` function to understand why.

```{code-cell} ipython3
py5.profile_draw()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(10)
```

```{code-cell} ipython3
py5.print_line_profiler_stats()
```

Almost all of the time is spent in [](/reference/sketch_convert_image). The
call itself is much faster than before because of the recycled
Py5Image object, but if we want to improve the performance of this Sketch,
we must figure out how to make it even faster.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

### Example with Threading

The way to make the Sketch even faster is to move the call to
[](/reference/sketch_convert_image) out of the `draw()` function
and into a separate thread.

The updated code is below. We will create a new function called
`update_chart()` that will be repeatedly called by
[](/reference/sketch_launch_repeating_thread).

Moving py5 method calls to a separate thread like this will
sometimes have thread-safety issues. A thread safety issue means
that code running in two different threads will create a conflict.
This can lead to unusual behavior, a programming error, or a crash.

In general, Processing drawing commands are not thread-safe, so
calling py5 methods from a thread like this is risky. This is
especially true when using the OpenGL renderers P2D and P3D.
However, the [](/reference/sketch_convert_image) method does
not attempt to draw to the screen, so using it in a thread like
this is fine.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
frame_rates = deque([60] * 250, maxlen=250)


def update_chart(frame_rates, line, figure, chart):
    line.set_ydata(frame_rates)
    py5.convert_image(figure, dst=chart)


def setup():
    global chart
    py5.size(950, 950)

    figure, line = create_chart(frame_rates)
    chart = py5.convert_image(figure)

    py5.launch_repeating_thread(
        update_chart,
        args=(frame_rates, line, figure, chart)
    )


def draw():
    frame_rates.append(py5.get_frame_rate())

    py5.background(240)
    py5.image(chart, 25, 25)


py5.run_sketch()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(10)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

The performance of this new Sketch is now a solid 60 frames per second.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5_tools.screenshot()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)

del draw
```

## Named Colors

Built in to matplotlib is an extensive list of
[named colors](https://matplotlib.org/stable/gallery/color/named_colors.html).
Matplotlib users can use this list to customize the aesthetics of
their charts. Py5 users can also access this inventory of colors
to customize the aesthetics of a Sketch.

Here is a simple example, referencing each color as a string.

```{code-cell} ipython3
def setup():
    py5.size(400, 400)
    py5.background(240)
    py5.no_stroke()

    # matplotlib base color, magenta
    py5.fill('m')
    py5.rect(20, 20, 170, 170)

    # tableau palette
    py5.fill('tab:orange')
    py5.rect(210, 20, 170, 170)

    # CSS4 colors
    py5.fill('chartreuse')
    py5.rect(20, 210, 170, 170)

    # xkcd color survey
    py5.fill('xkcd:blue with a hint of purple')
    py5.rect(210, 210, 170, 170)


py5.run_sketch()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(1)
```

```{code-cell} ipython3
py5_tools.screenshot()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

This works well, but it requires you to either remember the names
of the available colors or to constantly refer back to the list of
[named colors](https://matplotlib.org/stable/gallery/color/named_colors.html).
This is an extra challenge for non-english speakers, as well as
anyone who cannot remember the correct spelling of words like
"chartreuse."

As an alternative, py5 has a built-in dictionary of the full CSS4
and xkcd color survey inventories available for your use. Access
the dictionaries with `py5.css4_colors` and `py5.xkcd_colors`. These
are especially useful when coding an environment that supports code
completion, such as Jupyter Notebooks or VSCode. Coders will be
able to scroll through the list of color names and select the one
that sounds appropriate for their use case.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(400, 400)
    py5.background(240)
    py5.no_stroke()

    py5.fill(py5.css4_colors.FIREBRICK)
    py5.rect(20, 20, 170, 170)

    py5.fill(py5.css4_colors.PALETURQUOISE)
    py5.rect(210, 20, 170, 170)

    py5.fill(py5.xkcd_colors.PERIWINKLE_BLUE)
    py5.rect(20, 210, 170, 170)

    py5.fill(py5.xkcd_colors.PALE_MAUVE)
    py5.rect(210, 210, 170, 170)


py5.run_sketch()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(1)
```

```{code-cell} ipython3
py5_tools.screenshot()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

This final color dictionary feature is added to py5 when py5 is
built so you can use it without installing matplotlib.

+++

## Colormap Color Mode

Processing has two built-in color modes: RGB (red, green, blue) and
HSB (hue, saturation, brightness). Py5 adds a third: CMAP, short
for colormap.

The main idea behind the Colormap Color Mode is the automatic
mapping of values to the colors of a matplotlib colormap palette.
This includes support for the colormap's bad (`np.nan`) and outlier values.

You will enable the Colormap Color Mode with a call to
[](/reference/sketch_color_mode). You can find the list of built-in
colormaps in matplotlib's
[Colormap reference](https://matplotlib.org/stable/gallery/color/colormap_reference.html).
The scientific community has done extensive research on colormaps
and data visualization. Matplotlib's documentation provides some
insight into how to
[choose colormaps](https://matplotlib.org/stable/users/explain/colors/colormaps.html)
for your use case.

The below example uses the "ocean" colormap with the color
range from 0 to the sketch width (500) and the alpha value
range from 0 to the sketch height (also 500).

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(500, 500)

    py5.color_mode(py5.CMAP, py5.mpl_cmaps.OCEAN, py5.width, py5.height)

    # bypass the colormap functionality with a named color
    py5.background(py5.css4_colors.LIGHTGRAY)

    for _ in range(250):
        x = py5.random(py5.width)
        y = py5.random(py5.height)
        # fill color determined by x
        # transparency determined by y
        py5.fill(x, y)
        py5.rect(x, y, 10, 10)


py5.run_sketch()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(1)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

The above example used `py5.mpl_cmaps`, py5's built-in dictionary of
matplotlib's provided Colormaps. We could have just as easily used the
string "ocean" there, but like named colors, it is easier to not have
to remember the list of available Colormap names.

Observe the call to `py5.background()`, which used a named color.
Non-numeric values will bypass the Colormap functionality.

Here's a screenshot of what this example looks like. As you can see, the
colors blend from left to right and the transparency varies from top to
bottom.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5_tools.screenshot()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

### Creating Colormaps

You are not limited to matplotlib's build-in colormaps. If you like,
you can pass [](/reference/sketch_color_mode) a matplotlib Colormap
object from one of
[matplotlib's 3rd party libraries](https://matplotlib.org/mpl-third-party/#colormaps-and-styles)
or a Colormap object you create yourself.

Matplotlib provides extensive documentation on how to
[create your own Colormap](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html).
For fun, let's create a simple one here.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
colors = [py5.xkcd_colors.RICH_BLUE,
          py5.xkcd_colors.LIGHT_BLUE,
          py5.xkcd_colors.BRIGHT_RED,
          py5.xkcd_colors.BRIGHT_RED]
nodes = [0.0, 0.5, 0.75, 1.0]

py5_colormap = LinearSegmentedColormap.from_list(
    'py5 example colormap',
    list(zip(nodes, colors))
)

py5_colormap
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

We will use our new Colormap object in a Sketch that draws random
points to the screen. The color of each point will be noise values
passed through our Colormap.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(500, 500, py5.P2D)
    py5.color_mode(py5.CMAP, py5_colormap)


def draw():
    py5.no_stroke()
    py5.fill(py5.css4_colors.WHITE, 16)
    py5.rect(0, 0, py5.width, py5.height)

    py5.stroke_weight(10)
    for _ in range(500):
        x = py5.random(py5.width)
        y = py5.random(py5.height)
        val = py5.noise(x / 100, y / 100)
        py5.stroke(val, 128)
        py5.point(x, y)


py5.run_sketch()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

In this example, we didn't pass range values to
[](/reference/sketch_color_mode), so the range defaults to 1.0 for
the grayscale values and 255 for the alpha values.

Here's a screenshot of what this looks like, with the noise
high-points clearly in red.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(5)
```

```{code-cell} ipython3
py5_tools.screenshot()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

### Function Signatures

Since this is a new feature, we should clearly articulate the function signatures and
some details about how all of this works.

The [](/reference/sketch_color_mode) reference documentation provides this signature:

```python
color_mode(
    colormap_mode: int,  # CMAP, activating matplotlib Colormap mode
    color_map: Union[str, matplotlib.colors.Colormap],  # name of builtin matplotlib Colormap
    max_map: float,  # range for the color map
    max_a: float,  # range for the alpha
    /,
) -> None
```

The first parameter will be `CMAP` and the second parameter will be the name of one of the
built-in matplotlib Colormaps or an actual `matplotlib.colors.Colormap` instance. The third
parameter sets the value of the maximum input range; the minimum is always zero. The last
parameter sets the value of the maximum alpha value, and works just like the other color
modes. The third and fourth parameters are optional and default to 1.0 and 255, respectively.

In our first example, we used this code:

```python
def setup():
    py5.size(500, 500)

    py5.color_mode(py5.CMAP, py5.mpl_cmaps.OCEAN, py5.width, py5.height)
```

The `max_map` and `max_a` values are both 500.

If we then set the stroke style property with `py5.stroke(42)`, py5 would divide the input
value 42 by 500 and pass the result into the Colormap. The color value and alpha value
would be set by the output of the Colormap. If we set the stroke style property with
`py5.stroke(42, 250)`, py5 would get the same color value from the Colormap but override
the alpha value to be 250 divided by 500.

You can bypass the colormap functionality by passing a non-numeric argument such as
a named color or a color hex code. Refer to [](/integrations/colors) for more possibilities.

When this color mode is activated, py5 will accept `np.nan` values and map them to the
Colormap's "bad" or invalid color setting. Typically this is completely transparent.
If this isn't what you want, the best choice is to create your own Colormap and
use the instance's [set_bad()](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_bad)
method. You can also set a new "bad" value for a built-in Colormap.

This Colormap Color Mode feature does not work for Py5Graphics or
Py5Shape objects. It is only available for your Sketch. This
shouldn't limit you in any way because you can always use the
Sketch's [](/reference/sketch_color) method as a work-around
(i.e. `shape.fill(py5.color(42))`).
