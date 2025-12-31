---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.7
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"editable": true, "slideshow": {"slide_type": ""}}

# How to Use Processing Libraries

This is an introduction to py5's integration with [Processing Libraries](https://processing.org/reference/libraries).

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Processing Libraries

Processing offers a [collection of community maintained libraries](https://processing.org/reference/libraries), implemented in Java, that can add extra features to a Processing Sketch. Because py5 is built around the Processing Java code, these community maintained libraries can in theory work with py5. In reality, not all of them work perfectly with py5, but with a bit of effort and experimentation one can often use many of them productively in a py5 Sketch.

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Managing Libraries

The first step is to download and install a Processing Library. The easiest way to do this is with py5's built in tools for managing Processing Libraries. Start with the [](/reference/py5tools_processing_download_library) function to download a few Processing Libraries.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
import time
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
import py5_tools

py5_tools.processing.download_library("PeasyCam")
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5_tools.processing.download_library('JavaFX')
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

You can use the [](/reference/py5tools_processing_library_storage_dir) method to get the location of where these libraries are stored. This location is comparable to where other Python libraries will store downloaded files.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5_tools.processing.library_storage_dir()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

The default location of this directory for Windows users is in the `AppData/Local/py5/processing-libraries` subdirectory of your home directory. For Linux and MacOS users, it is in your `.cache/py5/processing-libraries` subdirectory. If you'd like to move this someplace else, set the `PY5_HOME` environment variable to your preferred location.

This directory is intended to be a place that py5 maintains, so please don't directly add, edit, or remove files from this directory. If you have your own jar files you'd like to add to a Sketch, put them in a `jars` subdirectory relative to the current working directory of your Python code. Or use the `PY5_JARS` environment variable to point to a directory of jar files that you manage yourself.

To get a list of currently installed libraries, use [](/reference/py5tools_processing_installed_libraries).

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5_tools.processing.installed_libraries()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

You can use [](/reference/py5tools_processing_remove_library) if you want to remove a previously installed library. Use [](/reference/py5tools_processing_check_library) to test if a library has already been installed, although calling [](/reference/py5tools_processing_download_library) multiple times is also acceptable. It won't re-download a library if py5 sees that it has already downloaded the most recent version.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
if not py5_tools.processing.check_library("PeasyCam"):
    py5_tools.processing.download_library("PeasyCam")
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Using Processing Libraries

Once your Processing Library has been installed, you can import py5 and begin your Sketch code. Importing py5 will add the installed Processing Libraries to the classpath. This can only be done once, so if you want to install anything else later, you'll need to restart your Python session.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
import py5
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

For this PeasyCam example, our next task is to import the PeasyCam Java class. JPype makes this easy to do and very much like regular Python imports.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
from peasy import PeasyCam
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Now, our actual Sketch code.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(500, 500, py5.P3D)
    PeasyCam(py5.get_current_sketch(), 500)

def draw():
    py5.background(128)
    py5.box(200)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

In this example, the `PeasyCam(py5.get_current_sketch(), 500)` code will link a PeasyCam instance to the py5 Sketch. Everything else is typical py5 code.

Our last step is to run the Sketch and admire our work:

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-output]
---
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
py5.exit_sketch()
time.sleep(1)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## JavaFX

The tools described on this page provide an avenue for using Processing's JavaFX renderer. The code and libraries for JavaFX are quite large so they must be installed separately.

Once installed, you can use the JavaFX renderer. It provides excellent 2D graphics without the use of OpenGL.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(500, 500, py5.FX2D)

def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-output]
---
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
py5.exit_sketch()
time.sleep(1)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

### JavaFX Limitations

JavaFX with py5 has some known limitations.

With JavaFX you are limited to running one Sketch per Python session. For a Python script this is irrelevant but you might not want to use JavaFX in a Jupyter Notebook, where you would typically run multiple Sketches. In addition, on MacOS the JavaFX Sketch window might not get focus when run from a Jupyter Notebook, which is a nuisance. Other than that, this library seems to work just fine with py5.
