# Live Coding

Live Coding is a useful feature to help facilitate the rapid prototyping of ideas. It will enable you to repeatedly change the code of a running Sketch without needing to repeatedly exit and call [](/reference/sketch_run_sketch).

The intended purpose of this is to help you quickly write py5 code. In particular, the py5 folks who have daily coding practices would benefit from Live Coding. It is useful for making small adjustments to working py5 code. It could also be used for Live Coding performances.

This feature is available for coders who use `*.py` files and coders who use Jupyter Notebooks.

## Live Coding in a *.py File

The standard way of using the Live Coding feature is to write your code using your favorite editor. In a terminal, run the code with the `py5-live-coding` command line tool, like so:

```bash
py5-live-coding experiment.py
```

Every time you save to the file `experiment.py`, `py5-live-coding` will read the new file and replace the running Sketch's code. Live Coding will monitor the file `experiment.py` and wait for the file's timestamp to change.

Your code should be written as if you were running it from the terminal with the `python` interpreter, so remember to include `import py5` and the call to `py5.run_sketch()`. The goal is for you to do your development and experimenting with `py5-live-coding`. Once your Sketch works as you would like, you should be able to run the same exact code from the terminal with the `python` interpreter, with no further code changes needed.

Live Coding works very well with editors such as VSCode. You'll want to use a keyboard shortcut `Control-S` or `Cmd-S` to save your code and trigger an update. Use of an editor's "Auto Save" functionality probably wouldn't work very well as it would constantly attempt to execute incomplete lines of code.

If you like, you can monitor the entire directory and not just one file. This is useful if you are editing code in multiple files, such as shader code. Live Coding will also work correctly if you are editing locally imported Python modules. It uses import hooks to detect imported modules so they can be removed when the Sketch is reset.

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

By default, Live Coding will use [](/reference/py5surface_set_always_on_top) to keep the Sketch window on top of other windows. This is useful when you want to type in your editor without forcing the Sketch to move behind the editor. This is particularly useful if you are coding on a laptop and your editor is in fullscreen mode. If for some reason you don't want the Sketch window to always be on top, use the `-t` argument.

Similarly, Live Coding will re-execute your `setup()` function every time the Sketch is reset. If you don't need or want it to do that, use the `-s` argument.

## Live Coding in a Jupyter Notebook

Very similar to above

Launch with py5_tools.live_coding.activate()...

Re-execute cells

Optional parameters from activate function

## Options

Why have this?

### Screenshots

### Code Archives

### Backups
