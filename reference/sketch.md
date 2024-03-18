# Sketch

Core py5 class for leveraging py5's functionality.

## Description

Core py5 class for leveraging py5's functionality. This is analogous to the PApplet class in Processing. Launch the Sketch with the [](sketch_run_sketch) method.

The core functions to be implemented by the py5 coder are `setup` and `draw`. The first will be run once at Sketch initialization and the second will be run in an animation thread, once per frame. The following event functions are also supported:

* `exiting`
* `key_pressed`
* `key_released`
* `key_typed`
* `mouse_clicked`
* `mouse_dragged`
* `mouse_entered`
* `mouse_exited`
* `mouse_moved`
* `mouse_pressed`
* `mouse_released`
* `mouse_wheel`
* `movie_event`
* `predraw_update`
* `post_draw`
* `pre_draw`

When coding in [class mode](content-py5-modes-class-mode), all of the above functions should be instance methods. When coding in [module mode](content-py5-modes-module-mode) or [imported mode](content-py5-modes-imported-mode), the above functions should be stand-alone functions available in the local namespace in which [](sketch_run_sketch) was called.

For more information, look at the online ["User Functions"](/content/user_functions) documentation.

Underlying Processing class: PApplet

The following methods and fields are provided:

```{include} include_sketch.md
```

Updated on March 18, 2024 05:08:14am UTC
