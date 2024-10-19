# Live Coding

Live Coding is a useful feature to help facilitate the rapid prototyping of ideas. It will enable you to repeatedly change the code of a running Sketch without needing to repeatedly exit a Sketch and call [](/reference/sketch_run_sketch) to start a new one.

The intended purpose of this is to help you quickly write py5 code. In particular, the py5 folks who have daily coding practices would benefit from Live Coding. It is useful for making small adjustments to working py5 code. It could also be used for activities such as Live Coding performances.

This feature is available for py5 in module mode only. It works for code written in `*.py` files and Jupyter Notebooks.

## Live Coding Overview

Before explaining in detail how to use Live Coding, it would be best to first use a concrete example to articulate what Live Coding can and cannot handle.

Consider the following Python code for the below discussion.

```python
import numpy as np

import py5


def setup():
    py5.size(400, 400, py5.P2D)
    py5.smooth(4)

    py5.stroke("red")
    py5.stroke_weight(2)

    py5.rect(50, 50, py5.width - 100, py5.height - 100)


def draw():
    rand_x = py5.width * np.random.rand()
    rand_y = py5.height * np.random.rand()
    py5.circle(rand_x, rand_y, 20)


py5.run_sketch()
```

When executed, the Sketch looks like this:

TODO: insert screenshot

### Changes Live Coding Can Handle

The ultimate goal of Live Coding is for you to use it for idea exploration and code implementation. Once your Sketch works as you would like, you should be able to run the same exact code without Live Coding and get the exact same results. There are a few places where this is impossible, but the limitations are relatively minor and understandable.

Every time the Sketch code is updated, either by saving the *.py file in your editor or executing a Jupyter Notebook cell, the Sketch will (by default) be reset. Your `setup()` function will be executed again, [](/reference/sketch_frame_count) and [](/reference/sketch_millis) will be set to zero, and any calls to style or configuration methods such as [](/reference/sketch_fill) to [](/reference/sketch_color_mode) will be undone. The Sketch should be identical to a new Sketch window. If you can find a situation where this is not the case (and is not a limitation already documented on this page), please [open an issue on GitHub](https://github.com/py5coding/py5generator/issues).

Here are example changes you can make to the above Sketch and how Live Coding will handle them:

* If the calls to [](/reference/sketch_stroke) or [](/reference/sketch_stroke_weight) are removed, Live Coding will reset the stroke color to default color of black and the stroke weight to 1. It will be as if they were never called in the first place.
* If the `draw()` function is commented out, it will be forgotten and the updated Sketch will only have a `setup()` function. The Sketch will no longer be animated. If the `draw()` function is later uncommented, the animation will resume.
* If `import numpy as np` is removed, the numpy library will no longer be available and the calls to `np.random.rand()` will throw exceptions. You will need to either replace the numpy import or re-write that code to use py5's builtin methods such as [](/reference/sketch_random).
* If you added [mouse](/content/user_functions#key-events) or [key](/content/user_functions#mouse-events) event functions such as `key_pressed()` or `mouse_clicked()`, the Sketch would start responding to mouse and key events. If those functions are later removed, the Sketch would stop responding to those events.

There is the option for Live Coding to not reset the Sketch and not call `setup()` when the code is updated. This is discussed later in this documentation.

The example code does not use shaders or make any calls to [](/reference/sketch_hint), but if it did, these would also be reset.

#### Exceptions and Syntax Errors

Live Coding can also handle Python code that throws Exceptions or contains syntax errors. It will not (should not!) ever crash. Exceptions and syntax errors will be reported to the terminal or Jupyter Notebook. For example, if we incorrectly modify the [](/reference/sketch_circle) call to add a fourth parameter, we will see the following:

```txt
********************************************************************************
py5 encountered an error in your code:

File "live_coding_documentation.py", line 19, in draw
    16   def draw():
    17       rand_x = py5.width * np.random.rand()
    18       rand_y = py5.height * np.random.rand()
--> 19       py5.circle(rand_x, rand_y, 20, "fourth parameter")
    ..................................................
     rand_x = 93.56332115800896
     rand_y = 324.43421014753284
    ..................................................

TypeError: circle() takes 3 positional arguments but 4 were given
********************************************************************************
```

The Sketch will pause while it is in this error state. You can then correct the error and update the Sketch code. When the error is resolved, Sketch execution will resume.

Properly hangled Exceptions need not be related to py5 methods or functions. Live Coding will also handle syntax errors and code parsing problems such as incorrect indentation. In all cases, it should pause and give you a chance to correct the problem before resuming Sketch execution.

### Changes Live Coding Cannot Handle

Here are changes that Live Coding cannot handle:

* Changes to [](/reference/sketch_size) or [](/reference/sketch_full_screen) are not possible. The Sketch window cannot change size and the renderer cannot be changed. If you were to modify those calls in your code, the changes would be ignored. You'd need to exit the Sketch and restart Live Coding if you want the changes to take effect.
* Changes to [](/reference/sketch_smooth), [](/reference/sketch_no_smooth), and [](/reference/sketch_pixel_density) are not possible. If you were to modify those calls in your code, the changes would be ignored. You'd again need to exit the Sketch and restart Live Coding.
* If you write a `settings()` function, don't make changes to it. There is some [](content-user_functions-settings-magic) that allows you to write just a `setup()` function instead of needing to write both `settings()` and `setup()`. The magic behind that could get tripped up if you fiddle with this while using Live Coding.
* Any calls to [](/reference/py5tools_add_classpath), [](/reference/py5tools_add_jars), and [](/reference/py5tools_add_options) are not possible and will throw an exception. These functions can only be called before the Java Virtual Machine starts. The Live Coding feature will start the Java Virtual Machine before even looking at your code for the first time. Therefore, they are not compatible with Live Coding.
* Use of py5's [](/content/hybrid_programming) is possible, but you recompile any Jar files, you'll need to exit the Sketch and restart Live Coding to see the changes.

There are probably a few other edge cases that Live Coding cannot handle. If you find something, please [open an issue on GitHub](https://github.com/py5coding/py5generator/issues). We will either look for a fix or document the limitation here.

## Live Coding in a *.py File

The standard way of using the Live Coding feature is to write your code using your favorite editor. In a terminal, run the code with the `py5-live-coding` command line tool, like so:

```bash
py5-live-coding experiment.py
```

Every time you save to the file `experiment.py`, `py5-live-coding` will read the new file and replace the running Sketch's code. Live Coding will monitor the file `experiment.py` and wait for the file's timestamp to change.

Your code should be written as if you were running it from the terminal with the `python` interpreter, so remember to include `import py5` and the call to `py5.run_sketch()`. The goal is for you to do your development and experimenting with `py5-live-coding`. Once your Sketch works as you would like, you should be able to run the same exact code from the terminal with the `python` interpreter, with no further code changes needed.

Live Coding works very well with editors such as VSCode. You'll want to use a keyboard shortcut `Control-S` or `Cmd-S` to save your code and trigger an update. Use of an editor's "Auto Save" functionality probably wouldn't work very well as it would constantly attempt to execute incomplete lines of code.

If you like, you can monitor the entire directory and not just one file. This is useful if you are editing code in multiple files, such as shader code. Live Coding will also work correctly if you are editing locally imported Python modules. It uses import hooks to detect imported modules so they can be removed and re-imported when the Sketch is reset.

Use the optional `-d` argument to monitor an entire directory, like so:

```bash
py5-live-coding -d experiment.py
```

The `py5-live-coding` command has other optional arguments, explained below.

### Optional Arguments

View the optional arguments with the `-h` argument.

```bash
$ py5-live-coding -h
usage: py5-live-coding [-h] [-a ARCHIVE_DIR] [-d] [-f] [-k] [-s] [-t] sketch_path

Live coding for module mode py5 sketches

positional arguments:
  sketch_path           path to py5 sketch

optional arguments:
  -h, --help            show this help message and exit
  -a ARCHIVE_DIR, --archive-dir ARCHIVE_DIR
                        directory to save screenshots and code backups
  -d, --watch-dir       watch all files in a directory or subdirectory for changes
  -f, --show-framerate  show framerate
  -k, --activate-keyboard-shortcuts
                        activate keyboard shortcuts
  -s, --not-always-rerun-setup
                        don't always rerun setup function when file is updated
  -t, --not-always-on-top
                        don't keep sketch on top of other windows
```

By default, Live Coding will use [](/reference/py5surface_set_always_on_top) to keep the Sketch window on top of other windows. This is useful when you want to write code in your editor without forcing the Sketch to move behind the editor. This is particularly useful if you are coding on a laptop and your editor is in fullscreen mode. If for some reason you don't want the Sketch window to always be on top, use the `-t` argument.

Similarly, Live Coding will re-execute your `setup()` function every time the Sketch is reset. If you don't need or want it to do that, use the `-s` argument.

It might be useful to you to monitor the Sketch's frame rate. This will show you how your code changes are impacting the Sketch's performance. To use this feature, use the `-f` argument. The Sketch's running frame rate will then appear in the terminal.

You may also want to quickly create screenshots of your Sketch or create copies of the current code. The optional keyboard shortcuts, activated with the `-k` argument, can help you with this. When activated, you can type `Shift-S` in the Sketch window to save a current screenshot to the archive directory. Create a backup copy of your code in the archive directory with the keyboard shortcut `Shift-C`. If you have used the `-d` argument to instruct Live Coding to watch all files in a directory for changes, the backup copy of your code will be a zip file of all of the files in the directory. If you want to create both a screenshot and a backup copy of the code, use the keyboard shortcut `Shift-A`.

By default the archive directory is in an `archive` subdirectory. Change this to something else with the `-a` parameter.

If the Sketch is in an error state, it will not create any screenshots or backups of the code.

Finally, the `-k` keyboard shortcuts argument also enables the keyboard shortcut `Shift-R` to instruct the Sketch to immediately re-execute the `setup()` function. This could be especially useful if you've used the `-s` argument to disable automatic execution of the `setup()` function when the Sketch is reset due to a code change.

## Live Coding in a Jupyter Notebook

Very similar to above

Launch with py5_tools.live_coding.activate()...

Re-execute cells

Optional parameters from activate function

## Options

Why have this section?

### Screenshots

### Code Archives

### Backups
