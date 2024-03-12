# py5 Reference Summary

## Drawing Shapes

### Basic Elements

* [arc()](/reference/sketch_arc) - Draws an arc to the screen.
* [circle()](/reference/sketch_circle) - Draws a circle to the screen.
* [ellipse()](/reference/sketch_ellipse) - Draws an ellipse (oval) - to the screen.
* [ellipse_mode()](/reference/sketch_ellipse_mode) - Modifies the location from which ellipses and circles are drawn by changing the way in which values given are interpreted.
* [line()](/reference/sketch_line) - Draws a line (a direct path between two points) - to the screen.
* [lines()](/reference/sketch_lines) - Draw a collection of lines to the screen.
* [point()](/reference/sketch_point) - Draws a point, a coordinate in space at the dimension of one pixel.
* [points()](/reference/sketch_points) - Draw a collection of points, each a coordinate in space at the dimension of one pixel.
* [quad()](/reference/sketch_quad) - A quad is a quadrilateral, a four sided polygon.
* [rect()](/reference/sketch_rect) - Draws a rectangle to the screen.
* [rect_mode()](/reference/sketch_rect_mode) - Modifies the location from which rectangles and squares are drawn by changing the way in which values given are interpreted.
* [square()](/reference/sketch_square) - Draws a square to the screen.
* [triangle()](/reference/sketch_triangle) - A triangle is a plane created by connecting three points.

### 3D Shapes

* [box()](/reference/sketch_box) - A box is an extruded rectangle. You'll need to set the `P3D` renderer in `size()` to use it.
* [sphere()](/reference/sketch_sphere) - A sphere is a hollow ball made from tessellated triangles. You'll need the `P3D` renderer.
* [sphere_detail()](/reference/sketch_sphere_detail) - Controls the detail used to render a sphere by adjusting the number of vertices of the sphere mesh.

### Vertex Based Shapes

* [begin_closed_shape()](/reference/sketch_begin_closed_shape) - This method is used to start a custom closed shape.
* [begin_contour()](/reference/sketch_begin_contour) - Use the `begin_contour()` and `end_contour()` methods to create negative shapes within shapes such as the center of the letter ‘O’.
* [begin_shape()](/reference/sketch_begin_shape) - Using the `begin_shape()` and `end_shape()` functions allow creating more complex forms.
* [bezier_vertex()](/reference/sketch_bezier_vertex) - Specifies vertex coordinates for Bezier curves.
* [bezier_vertices()](/reference/sketch_bezier_vertices) - Create a collection of bezier vertices.
* [curve_vertex()](/reference/sketch_curve_vertex) - Specifies vertex coordinates for curves.
* [curve_vertices()](/reference/sketch_curve_vertices) - Create a collection of curve vertices.
* [end_contour()](/reference/sketch_end_contour) - Use the `begin_contour()` and `end_contour()` methods to create negative shapes within shapes such as the center of the letter ‘O’.
* [end_shape()](/reference/sketch_end_shape) - The `end_shape()` function is the companion to `begin_shape()` and may only be called after `begin_shape()`.
* [quadratic_vertex()](/reference/sketch_quadratic_vertex) - Specifies vertex coordinates for quadratic Bezier curves.
* [quadratic_vertices()](/reference/sketch_quadratic_vertices) - Add a collection of quadratic vertices.
* [vertex()](/reference/sketch_vertex) - Add a new vertex to a shape.
* [vertices()](/reference/sketch_vertices) - Add a collection of vertices to a shape.

### Standalone Curves

* [bezier()](/reference/sketch_bezier) - Draws a Bezier curve on the screen.
* [bezier_detail()](/reference/sketch_bezier_detail) - Sets the resolution at which Beziers display.
* [bezier_point()](/reference/sketch_bezier_point) - Evaluates the Bezier at point t for points a, b, c, d.
* [bezier_tangent()](/reference/sketch_bezier_tangent) - Calculates the tangent of a point on a Bezier curve.
* [curve()](/reference/sketch_curve) - Draws a curved line (*Catmull-Rom spline*) on the screen.
* [curve_detail()](/reference/sketch_curve_detail) - Sets the resolution at which curves display.
* [curve_point()](/reference/sketch_curve_point) - Evaluates the curve at point t for points a, b, c, d.
* [curve_tangent()](/reference/sketch_curve_tangent) - Calculates the tangent of a point on a curve.
* [curve_tightness()](/reference/sketch_curve_tightness) - Modifies the quality of forms created with `curve()` and `curve_vertex()`.

### Creating and Displaying Shape Objects

* [create_shape()](/reference/sketch_create_shape) - Used to define a new empty Py5Shape object.
* [load_shape()](/reference/sketch_load_shape) - Loads SVG or OBJ geometry making it available as a Py5Shape object.
* [convert_shape()](/reference/sketch_convert_shape) - Converts Python objects into Py5Shape objects.
* [shape()](/reference/sketch_shape) - Draws shapes to the display window.
* [shape_mode()](/reference/sketch_shape_mode) - Modifies the location from which shapes draw.
* [Py5Shape class](/reference/py5shape) - Datatype for storing shapes. Allows loading and displaying SVG and OBJ shapes.

## Color and Other Graphic Attributes

### Creating and Setting Colors

* [background()](/reference/sketch_background) - Sets the color for the sketch background, also, paints over any previous drawing.
* [clear()](/reference/sketch_clear) - Clear the drawing surface by setting every pixel to black.
* [color_mode()](/reference/sketch_color_mode) - Changes the way py5 interprets color data, using the constants `HSB`, `RGB` and the range of the values to be used.
* [fill()](/reference/sketch_fill) - Sets the color used to fill shapes.
* [no_fill()](/reference/sketch_no_fill) - Disables filling geometry.
* [no_stroke()](/reference/sketch_no_stroke) - Disables drawing the stroke (outline).
* [stroke()](/reference/sketch_stroke) - Sets the color used to draw lines and borders around shapes.
* [color()](/reference/sketch_color) - Creates colors for storing in variables of the color datatype (a 32 bit integer).
* [lerp_color()](/reference/sketch_lerp_color) - Calculates a color between two colors at a specific increment.

### Analyzing Colors

* [hex_color()](/reference/sketch_hex_color) - Convert a color value to a hex color string.
* [alpha()](/reference/sketch_alpha) - Extracts the alpha value from a color, scaled to match current `color_mode()`.
* [blue()](/reference/sketch_blue) - Extracts the blue value from a color, scaled to match current `color_mode()`.
* [brightness()](/reference/sketch_brightness) - Extracts the brightness value from a color.
* [green()](/reference/sketch_green) - Extracts the green value from a color, scaled to match current `color_mode()`.
* [hue()](/reference/sketch_hue) - Extracts the hue value from a color.
* [red()](/reference/sketch_red) - Extracts the red value from a color, scaled to match current `color_mode()`.
* [saturation()](/reference/sketch_saturation) - Extracts the saturation value from a color.

### Stroke Attributes and Style Control

* [stroke_weight()](/reference/sketch_stroke_weight) -  Sets the width of the stroke used for lines, points, and the border around shapes.
* [stroke_cap()](/reference/sketch_stroke_cap) - Sets the style for rendering line endings.
* [stroke_join()](/reference/sketch_stroke_join) - Sets the style of the joints which connect line segments.
* [pop_style()](/reference/sketch_pop_style) - The `push_style()` function saves the current style settings and `pop_style()` restores the prior settings; these functions are always used together.
* [push_style()](/reference/sketch_push_style) - The `push_style()` function saves the current style settings and `pop_style()` restores the prior settings.
* [push()](/reference/sketch_push) - combines `push_style()` and `push_matrix()` The `push()` function saves the current drawing style settings and transformations, while `pop()` restores these settings.
* [pop()](/reference/sketch_pop) - combines `pop_style()` and `pop_matrix()` The `pop()` function restores the previous drawing style settings and transformations after `push()` has changed them.

## Inputs

### Reading Files

* [load_bytes()](/reference/sketch_load_bytes) - Load byte data from a file or URL.
* [load_json()](/reference/sketch_load_json) - Load a JSON data file from a file or URL.
* [load_pickle()](/reference/sketch_load_pickle) - Load a pickled Python object from a file.
* [load_strings()](/reference/sketch_load_strings) - Load a list of strings from a file or URL.
* [parse_json()](/reference/sketch_parse_json) - Parse serialized JSON data from a string.
* [select_folder()](/reference/sketch_select_folder) - Opens a file chooser dialog to select a folder.
* [select_input()](/reference/sketch_select_input) - Open a file chooser dialog to select a file for input.

### Keyboard Variables

* [is_key_pressed](/reference/sketch_is_key_pressed) - The `is_key_pressed` variable stores whether or not a keyboard button is currently being pressed.
* [key](/reference/sketch_key) - The system variable `key` always contains the value of the most recent key on the keyboard that was used (either pressed or released). It will contain the constant `CODED` if it was a special key that can then be discriminated with `key_code`.
* [key_code](/reference/sketch_key_code) - The variable `key_code` is used to detect special keys such as the arrow keys (`UP`, `DOWN`, `LEFT`, and `RIGHT`) - as well as `ALT`, `CONTROL`, and `SHIFT`.

### Keyboard Event Functions

* `key_pressed()` - If defined, it will be called once when a keyboard key is pressed.
* `key_released()` - If defined, it will be called once when a keyboard key is released.
* `key_typed()` - If defined, it will be called once when a keyboard key is pressed and released.
* [Py5KeyEvent Class](/reference/py5keyevent) - A Py5KeyEvent object will be passed to user-defined keyboard event functions.

### Mouse Variables

* [is_mouse_pressed](/reference/sketch_is_mouse_pressed) - The `is_mouse_pressed` variable stores whether or not a mouse button is currently being pressed.
* [mouse_button](/reference/sketch_mouse_button) - When a mouse button is pressed, the value of the system variable `mouse_button` is set to either `LEFT`, `RIGHT`, or `CENTER`, depending on which button is pressed.
* [mouse_x](/reference/sketch_mouse_x) - The system variable `mouse_x` always contains the current horizontal coordinate of the mouse.
* [mouse_y](/reference/sketch_mouse_y) - The system variable `mouse_y` always contains the current vertical coordinate of the mouse.
* [pmouse_x](/reference/sketch_pmouse_x) - The system variable `pmouse_x` always contains the horizontal position of the mouse in the frame previous to the current frame.
* [pmouse_y](/reference/sketch_pmouse_y) - The system variable `pmouse_y` always contains the vertical position of the mouse in the frame previous to the current frame.
* [rmouse_x](/reference/sketch_rmouse_x) - The current horizontal coordinate of the mouse after activating scale invariant drawing.
* [rmouse_y](/reference/sketch_rmouse_y) - The current vertical coordinate of the mouse after activating scale invariant drawing.

### Mouse Event Functions

* `mouse_pressed()` - If defined, it will be called once when a mouse button is pressed.
* `mouse_released()` - If defined, it will be called once when a mouse button is pressed.
* `mouse_clicked()` - If defined, it will be called once when a mouse button is clicked.
* `mouse_dragged()` - If defined, it will be called many times as the mouse is moved while pressed.
* `mouse_wheel()` - If defined, it will be called as the mouse wheel is rolled.
* `mouse_moved()` - If defined, it will be called many times as the mouse is moved.
* `mouse_entered()` - If defined, it will be called when the mouse enters the sketch area.
* `mouse_exited()` - If defined, it will be called when the mouse leaves the sketch area.
* [Py5MouseEvent Class](/reference/py5mouseevent) - A Py5MouseEvent object will be passed to user-defined mouse event functions.

### Time & Date Helpers

* [day()](/reference/sketch_day) - Returns the current day as a value from 1 - 31 by consulting the clock on your computer.
* [hour()](/reference/sketch_hour) - Returns the current hour as a value from 0 to 23 by consulting the clock on your computer.
* [millis()](/reference/sketch_millis) - Returns the number of milliseconds (thousandths of a second) - since starting the program.
* [minute()](/reference/sketch_minute) - Returns the current minute as a value from 0 to 59 by consulting the clock on your computer.
* [month()](/reference/sketch_month) - Returns the current month as a value from 1 to 12 by consulting the clock on your computer.
* [second()](/reference/sketch_second) - Returns the current seconds as a value from 0 to 59 by consulting the clock on your computer.
* [year()](/reference/sketch_year) - Returns the current year by consulting the clock on your computer.

## Output

### Saving Files

* [begin_raw()](/reference/sketch_begin_raw) - To create vectors from 3D data, use the `begin_raw()` and `end_raw()` commands.
* [begin_record()](/reference/sketch_begin_record) - Opens a new file and all subsequent drawing functions are echoed to this file as well as the display window.
* [end_raw()](/reference/sketch_end_raw) - Complement to `begin_raw()`; they must always be used together.
* [end_record()](/reference/sketch_end_record) - Stops the recording process started by `begin_record()` and closes the file.
* [save_bytes()](/reference/sketch_save_bytes) - Save byte data to a file.
* [save_json()](/reference/sketch_save_json) - Save JSON data to a file.
* [save_pickle()](/reference/sketch_save_pickle) - Pickle a Python object to a file.
* [save_strings()](/reference/sketch_save_strings) - Save a list of strings to a file.
* [select_output()](/reference/sketch_select_output) - Opens a file chooser dialog to select a file for output.

### Image Output

* [save()](/reference/sketch_save) - Save the drawing surface to an image file.
* [save_frame()](/reference/sketch_save_frame) - Save the current frame as an image.

### Text Area (Console)

* [println()](/reference/sketch_println) - Print text or other values to the console (not the sketch drawing area). Similar to Python's `print()`.
* [set_println_stream()](/reference/sketch_set_println_stream) - Customize where the output of `println()` goes.

## Typography

### Drawing Text

* [text()](/reference/sketch_text) - Draws text on the screen, that is, the sketch drawing area.
* [text_align()](/reference/sketch_text_align) - Sets the current alignment for drawing text.
* [text_leading()](/reference/sketch_text_leading) - Sets the spacing between lines of text in units of pixels.
* [text_mode()](/reference/sketch_text_mode) - Sets the way text draws to the screen, either as texture maps or as vector geometry.
* [text_size()](/reference/sketch_text_size) - Sets the current font size.

### Loading & Selecting Fonts

* [create_font()](/reference/sketch_create_font) - Dynamically converts a font to the format used by py5 from a .ttf or .otf file inside the Sketch’s “data” folder or a font that’s installed elsewhere on the computer.
* [load_font()](/reference/sketch_load_font) - Loads a .vlw formatted font into a Py5Font object.
* [text_font()](/reference/sketch_text_font) - Sets the current font that will be drawn with the `text()` function.
* [Py5Font](/reference/py5font) - Py5Font is the font class for py5, stores font information in a way py5 can use.

### Text Metrics

* [text_width()](/reference/sketch_text_width) - Calculates and returns the width of any character or text string.
* [text_ascent()](/reference/sketch_text_ascent) - Returns ascent of the current font at its current size.
* [text_descent()](/reference/sketch_text_descent) - Returns descent of the current font at its current size.

## Coordinate System Transformations

### Basic Operations

* [push_matrix()](/reference/sketch_push_matrix) - Saves the transformation matrix that describes the current coordinate system in the matrix stack so that it can be restored later with `pop_matrix()`.
* [pop_matrix()](/reference/sketch_pop_matrix) - Retrieves the last transformation matrix stored in the matrix stack restoring a previous coordinate system state.
* [translate()](/reference/sketch_translate) - Specifies an amount to displace the coordinate system origin, displacing objects drawn within the display window. Can be used in 2D, `translate(x, y)`, or 3D, `translate(x, y, z)`.
* [rotate()](/reference/sketch_rotate) - Rotates the coordinate system the amount specified by the angle parameter.
* [scale()](/reference/sketch_scale) - Increases or decreases the size of shapes by expanding and contracting the coordinate system.
* [shear_x()](/reference/sketch_shear_x) - Shears shapes around the x-axis the amount specified by the angle parameter.
* [shear_y()](/reference/sketch_shear_y) - Shears shapes around the y-axis the amount specified by the angle parameter.

### 3D Rotations

* [rotate_x()](/reference/sketch_rotate_x) - Rotates around the x-axis the amount specified by the angle parameter.
* [rotate_y()](/reference/sketch_rotate_y) - Rotates around the y-axis the amount specified by the angle parameter.
* [rotate_z()](/reference/sketch_rotate_z) - Rotates around the z-axis the amount specified by the angle parameter.

### Matrix Operations

* [apply_matrix()](/reference/sketch_apply_matrix) - Multiplies the current matrix by the one specified through the parameters.
* [get_matrix()](/reference/sketch_get_matrix) - Get the current matrix as a numpy array.
* [print_matrix()](/reference/sketch_print_matrix) - Prints the current matrix to standard output.
* [reset_matrix()](/reference/sketch_reset_matrix) - Replaces the current matrix with the identity matrix.
* [set_matrix()](/reference/sketch_set_matrix) - Set the current matrix to the one specified through the parameter source.

## Sketch Environment

### Setup and Variables

* [size()](/reference/sketch_size) - Must be called only once to define the sketch dimensions, width and height, in pixel units. Other than in static mode, it must be used inside `setup()` or `settings()`.
* [full_screen()](/reference/sketch_full_screen) - Make the sketch use the full size of the computer’s display. Replaces `size()`.
* [width](/reference/sketch_width) - System variable that stores the width of the display window.
* [height](/reference/sketch_height) - System variable that stores the height of the display window.
* [smooth()](/reference/sketch_smooth) - Draws all geometry with smooth (anti-aliased) - edges. Must be used just after `size()`.
* [no_smooth()](/reference/sketch_no_smooth) - Draws all geometry and fonts with jagged (aliased) - edges and images with hard edges between the pixels when enlarged rather than interpolating pixels.
* [cursor()](/reference/sketch_cursor) - Sets the cursor to a predefined symbol or an image, or makes it visible if already hidden.
* [no_cursor()](/reference/sketch_no_cursor) - Hides the cursor from view.
* [frame_count](/reference/sketch_frame_count) - The system variable frame_count contains the number of frames that have been displayed since the program started.
* [frame_rate()](/reference/sketch_frame_rate) - Specifies the target number of frames to be displayed every second. If drawing a frame gets slow the target will not be met!
* [get_frame_rate()](/reference/sketch_get_frame_rate) - Get the running Sketch’s current frame rate.
* [display_density()](/reference/sketch_display_density) - This function returns the number “2” if the screen is a high-density screen (called a Retina display on macOS or high-dpi on Windows and Linux) - and a “1” if not.
* [pixel_density()](/reference/sketch_pixel_density) - This function makes it possible for py5 to render using all of the pixels on high resolutions screens like Apple Retina displays and Windows High-DPI displays.
* [display_height](/reference/sketch_display_height) - System variable that stores the height of the entire screen display.
* [display_width](/reference/sketch_display_width) - System variable that stores the width of the entire screen display.
* [focused](/reference/sketch_focused) - Confirms if a py5 program is "focused", meaning that it is active and will accept mouse or keyboard input.
* [sketch_path()](/reference/sketch_sketch_path) - The Sketch’s current path.

### Other Window Controls

* [get_surface()](/reference/sketch_get_surface) - Get the Py5Surface object used for the Sketch window.
* [pixel_height](/reference/sketch_pixel_height) - Height of the display window in pixels.
* [pixel_width](/reference/sketch_pixel_width) - Width of the display window in pixels.
* [ratio_left](/reference/sketch_ratio_left) - Width of the left section of the window that does not fit the desired aspect ratio of a scale invariant Sketch.
* [ratio_scale](/reference/sketch_ratio_scale) - Scaling factor used to maintain scale invariant drawing.
* [ratio_top](/reference/sketch_ratio_top) - Height of the top section of the window that does not fit the desired aspect ratio of a scale invariant Sketch.
* [rheight](/reference/sketch_rheight) - The height of the scale invariant display window.
* [rwidth](/reference/sketch_rwidth) - The width of the scale invariant display window.
* [window_move()](/reference/sketch_window_move) - Set the Sketch’s window location.
* [window_ratio()](/reference/sketch_window_ratio) - Set a window ratio to enable scale invariant drawing.
* [window_resizable()](/reference/sketch_window_resizable) - Set the Sketch window as resizable by the user.
* [window_resize()](/reference/sketch_window_resize) - Set a new width and height for the Sketch window.
* [window_title()](/reference/sketch_window_title) - Set the Sketch window’s title.
* [window_x](/reference/sketch_window_x) - The x-coordinate of the current window location.
* [window_y](/reference/sketch_window_y) - The y-coordinate of the current window location.

## Math Related

### Calculation

* [ceil()](/reference/sketch_ceil) - Calculates the closest int value that is greater than or equal to the value of the parameter.
* [constrain()](/reference/sketch_constrain) - Constrains a value to not exceed a maximum and minimum value.
* [dist()](/reference/sketch_dist) - Calculates the distance between two points.
* [exp()](/reference/sketch_exp) - Returns Euler’s number e (2.71828…) - raised to the power of the n parameter.
* [floor()](/reference/sketch_floor) - Calculates the closest int value that is less than or equal to the value of the parameter.
* [lerp()](/reference/sketch_lerp) - Calculates a number between two numbers at a specific increment.
* [log()](/reference/sketch_log) - Calculates the natural logarithm (the base-e logarithm) - of a number.
* [mag()](/reference/sketch_mag) - Calculates the magnitude (or length) - of a vector.
* [norm()](/reference/sketch_norm) - Normalizes a number from another range into a value between 0 and 1.
* [remap()](/reference/sketch_remap) - Re-maps a number from one range to another.
* [sq()](/reference/sketch_sq) - Squares a number (multiplies a number by itself).
* [sqrt()](/reference/sketch_sqrt) - Calculates the square root of a number.
* [Py5Vector class](/reference/py5vector) - Class to describe a 2D, 3D, or 4D vector.

### Random

* [noise()](/reference/sketch_noise) - Generate pseudo-random noise values for specific coordinates using Processing’s noise algorithm.
* [noise_detail()](/reference/sketch_noise_detail) - Adjusts the character and level of detail of Processing’s noise algorithm, produced by the `noise()` function.
* [noise_seed()](/reference/sketch_noise_seed) - Sets the seed value for `noise()`.
* [np_random](/reference/sketch_np_random) - Access the numpy random number generator that py5 uses to provide random number functionality.
* [os_noise()](/reference/sketch_os_noise) - Generate pseudo-random noise values for specific coordinates using the OpenSimplex 2 algorithm (smooth version / SuperSimplex).
* [os_noise_seed()](/reference/sketch_os_noise_seed) - Sets the seed value for `os_noise()`.
* [random()](/reference/sketch_random) - Generates random numbers.
* [random_choice()](/reference/sketch_random_choice) - Select a random item from a list.
* [random_gaussian()](/reference/sketch_random_gaussian) - Generates random gaussian values.
* [random_int()](/reference/sketch_random_int) - Generates random integers.
* [random_sample()](/reference/sketch_random_sample) - Select random items from a list.
* [random_seed()](/reference/sketch_random_seed) - Sets the seed value for py5’s random functions.

### Trigonometry

* [acos()](/reference/sketch_acos) - The inverse of `cos()`, returns the arc cosine of a value.
* [asin()](/reference/sketch_asin) - The inverse of `sin()`, returns the arc sine of a value.
* [atan()](/reference/sketch_atan) - The inverse of `tan()`, returns the arc tangent of a value.
* [atan2()](/reference/sketch_atan2) - Calculates the angle (in radians) - from a specified point to the coordinate origin as measured from the positive x-axis.
* [cos()](/reference/sketch_cos) - Calculates the cosine of an angle.
* [degrees()](/reference/sketch_degrees) - Converts a radian measurement to its corresponding value in degrees.
* [radians()](/reference/sketch_radians) - Converts a degree measurement to its corresponding value in radians.
* [sin()](/reference/sketch_sin) - Calculates the sine of an angle.
* [tan()](/reference/sketch_tan) - Calculates the ratio of the sine and cosine of an angle.

## Working with Images

### Loading and Displaying

* [image()](/reference/sketch_image) - The `image()` function draws an image to the display window.
* [image_mode()](/reference/sketch_image_mode) - Modifies the location from which images are drawn by changing the way in which parameters given to `image()` are interpreted.
* [load_image()](/reference/sketch_load_image) - Load an image into a variable of type Py5Image.
* [no_tint()](/reference/sketch_no_tint) - Removes the current fill value for displaying images and reverts to displaying images with their original hues.
* [tint()](/reference/sketch_tint) - Sets the fill value for displaying images.

### Pixels

* [apply_filter()](/reference/sketch_apply_filter) - Filters the display window using a preset filter or with a custom shader.
* [blend()](/reference/sketch_blend) - Blends a region of pixels from one image into another (or in itself again) - with full alpha channel support.
* [copy()](/reference/sketch_copy) - Copies a region of pixels from the display window to another area of the display window and copies a region of pixels from an image used as the src_img parameter into the display window.
* [get_np_pixels()](/reference/sketch_get_np_pixels) - Returns the contents of `np_pixels[]` as a numpy array.
* [get_pixels()](/reference/sketch_get_pixels) - Reads the color of any pixel or grabs a section of the drawing surface.
* [load_np_pixels()](/reference/sketch_load_np_pixels) - Loads the pixel data of the current display window into the `np_pixels[]` array.
* [load_pixels()](/reference/sketch_load_pixels) - Loads the pixel data of the current display window into the `pixels[]` array.
* [np_pixels[]](/reference/sketch_np_pixels) - The `np_pixels[]` array contains the values for all the pixels in the display window.
* [pixels[]](/reference/sketch_pixels) - The `pixels[]` array contains the values for all the pixels in the display window.
* [set_np_pixels()](/reference/sketch_set_np_pixels) - Set the entire contents of `np_pixels[]` to the contents of another properly sized and typed numpy array.
* [set_pixels()](/reference/sketch_set_pixels) - Changes the color of any pixel or writes an image directly into the drawing surface.
* [to_pil()](/reference/sketch_to_pil) - Returns the drawing surface as a PIL Image object.
* [update_np_pixels()](/reference/sketch_update_np_pixels) - Updates the display window with the data in the `np_pixels[]` array.
* [update_pixels()](/reference/sketch_update_pixels) - Updates the display window with the data in the `pixels[]` array.

### Textures

* [texture()](/reference/sketch_texture) - Sets a texture to be applied to vertex points.
* [texture_mode()](/reference/sketch_texture_mode) - Sets the coordinate space for texture mapping.
* [texture_wrap()](/reference/sketch_texture_wrap) - Defines if textures repeat or draw once within a texture map.

### Image Objects

* [Py5Image class](https://py5coding.org/reference/py5image) - Datatype for storing images.
* [create_image()](/reference/sketch_create_image) - Creates a new Py5Image (the datatype for storing images).
* [convert_image()](/reference/sketch_convert_image) - Convert non-py5 image objects into Py5Image objects.
* [create_image_from_numpy()](/reference/sketch_create_image_from_numpy) - Convert a numpy array into a Py5Image object.
* [request_image()](/reference/sketch_request_image) - Use a Py5Promise object to load an image into a variable of type Py5Image.

## 3D Scene

### Camera

* [begin_camera()](/reference/sketch_begin_camera) - The `begin_camera()` and `end_camera()` functions enable advanced customization of the camera space.
* [camera()](/reference/sketch_camera) - Sets the position of the camera through setting the eye position, the center of the scene, and which axis is facing upward.
* [end_camera()](/reference/sketch_end_camera) - The `begin_camera()` and `end_camera()` methods enable advanced customization of the camera space.
* [frustum()](/reference/sketch_frustum) - Sets a perspective matrix as defined by the parameters.
* [ortho()](/reference/sketch_ortho) - Sets an orthographic projection and defines a parallel clipping volume.
* [perspective()](/reference/sketch_perspective) - Sets a perspective projection applying foreshortening, making distant objects appear smaller than closer ones.
* [print_camera()](/reference/sketch_print_camera) - Prints the current camera matrix to standard output.
* [print_projection()](/reference/sketch_print_projection) - Prints the current projection matrix to standard output.

### Coordinates

* [model_x()](/reference/sketch_model_x) - Returns the three-dimensional X, Y, Z position in model space.
* [model_y()](/reference/sketch_model_y) - Returns the three-dimensional X, Y, Z position in model space.
* [model_z()](/reference/sketch_model_z) - Returns the three-dimensional X, Y, Z position in model space.
* [screen_x()](/reference/sketch_screen_x) - Takes a three-dimensional X, Y, Z position and returns the X value for where it will appear on a (two-dimensional) - screen.
* [screen_y()](/reference/sketch_screen_y) - Takes a three-dimensional X, Y, Z position and returns the Y value for where it will appear on a (two-dimensional) - screen.
* [screen_z()](/reference/sketch_screen_z) - Takes a three-dimensional X, Y, Z position and returns the Z value for where it will appear on a (two-dimensional) - screen.

### Lights

* [ambient_light()](/reference/sketch_ambient_light) - Adds an ambient light.
* [directional_light()](/reference/sketch_directional_light) - Adds a directional light.
* [light_falloff()](/reference/sketch_light_falloff) - Sets the falloff rates for point lights, spot lights, and ambient lights.
* [light_specular()](/reference/sketch_light_specular) - Sets the specular color for lights.
* [lights()](/reference/sketch_lights) - Sets the default ambient light, directional light, falloff, and specular values.
* [no_lights()](/reference/sketch_no_lights) - Disable all lighting.
* [normal()](/reference/sketch_normal) - Sets the current normal vector.
* [point_light()](/reference/sketch_point_light) - Adds a point light.
* [spot_light()](/reference/sketch_spot_light) - Adds a spot light.

### Material Properties

* [ambient()](/reference/sketch_ambient) - Sets the ambient reflectance for shapes drawn to the screen.
* [emissive()](/reference/sketch_emissive) - Sets the emissive color of the material used for drawing shapes drawn to the screen.
* [shininess()](/reference/sketch_shininess) - Sets the amount of gloss in the surface of shapes.
* [specular()](/reference/sketch_specular) - Sets the specular color of the materials used for shapes drawn to the screen, which sets the color of highlights.

## Rendering

### Graphics Context

* [blend_mode()](/reference/sketch_blend_mode) - Blends the pixels in the display window according to a defined mode.
* [clip()](/reference/sketch_clip) - Limits the rendering to the boundaries of a rectangle defined by the parameters.
* [create_graphics()](/reference/sketch_create_graphics) - Creates and returns a new Py5Graphics object.
* [flush()](/reference/sketch_flush) - Flush drawing commands to the renderer.
* [get_graphics()](/reference/sketch_get_graphics) - Get the Py5Graphics object used by the Sketch.
* [hint()](/reference/sketch_hint) - This function is used to enable or disable special features that control how graphics are drawn.
* [no_clip()](/reference/sketch_no_clip) - Disables the clipping previously started by the `clip()` function.

### Shaders

* [load_shader()](/reference/sketch_load_shader) - Loads a shader into a Py5Shader object.
* [reset_shader()](/reference/sketch_reset_shader) - Restores the default shaders.
* [shader()](/reference/sketch_shader) - Applies the shader specified by the parameters.

## Sketch Execution

### Draw Loop Control

* [loop()](/reference/sketch_loop) - By default, py5 loops through `draw()` continuously, executing the code within it.
* [no_loop()](/reference/sketch_no_loop) - Stops py5 from continuously executing the code within `draw()`.
* [redraw()](/reference/sketch_redraw) - Executes the code within `draw()` one time.
* [exit_sketch()](/reference/sketch_exit_sketch) - Quits/stops/exits the program.
* `exiting()` - A function that, if defined by the user, will be called to be executed after the sketch stops.

### Advanced Execution Control

* [finished](/reference/sketch_finished) - Boolean variable reflecting if the Sketch has stopped permanently.
* [hot_reload_draw()](/reference/sketch_hot_reload_draw) - Perform a hot reload of the Sketch’s draw function.
* [is_dead](/reference/sketch_is_dead) - Boolean value reflecting if the Sketch has been run and has now stopped.
* [is_dead_from_error](/reference/sketch_is_dead_from_error) - Boolean value reflecting if the Sketch has been run and has now stopped because of an error.
* [is_ready](/reference/sketch_is_ready) - Boolean value reflecting if the Sketch is in the ready state.
* [is_running](/reference/sketch_is_running) - Boolean value reflecting if the Sketch is in the running state.
* [pargs](/reference/sketch_pargs) - List of strings passed to the Sketch through the call to `run_sketch()`.

### Performance Profiling

* [print_line_profiler_stats()](/reference/sketch_print_line_profiler_stats) - Print the line profiler stats initiated with `profile_draw()` or `profile_functions()`.
* [profile_draw()](/reference/sketch_profile_draw) - Profile the execution times of the draw function with a line profiler.
* [profile_functions()](/reference/sketch_profile_functions) - Profile the execution times of the Sketch’s functions with a line profiler.

### Threading

* [has_thread()](/reference/sketch_has_thread) - Determine if a thread of a given name exists and is currently running.
* [join_thread()](/reference/sketch_join_thread) - Join the Python thread associated with the given thread name.
* [launch_promise_thread()](/reference/sketch_launch_promise_thread) - Create a Py5Promise object that will store the returned result of a function when that function completes.
* [launch_repeating_thread()](/reference/sketch_launch_repeating_thread) - Launch a new thread that will repeatedly execute a function in parallel with your Sketch code.
* [launch_thread()](/reference/sketch_launch_thread) - Launch a new thread to execute a function in parallel with your Sketch code.
* [list_threads()](/reference/sketch_list_threads) - List the names of all of the currently running threads.
* [stop_all_threads()](/reference/sketch_stop_all_threads) - Stop all running threads.
* [stop_thread()](/reference/sketch_stop_thread) - Stop a thread of a given name.

### JVM Constants

* [java_platform](/reference/sketch_java_platform) - Version of Java currently being used by py5.
* [java_version_name](/reference/sketch_java_version_name) - Version name of Java currently being used by py5.

## py5 Classes and Other Tools

### Classes

* [Py5Graphics](/reference/py5graphics) - Main graphics and rendering context, as well as the base API implementation for Processing's “core”.
* [Py5Image](/reference/py5image) - A Datatype for storing images. Allows loading, converting and displaying external image formats as well as efficient manipulation of pixels as NumPy arrays.
* [Py5Shape](/reference/py5shape) - Datatype for storing shapes. Allows loading and displaying SVG (Scalable Vector Graphics) and OBJ shapes.
* [Py5Shader](/reference/py5shader) - This class encapsulates a GLSL shader program, including a vertex and a fragment shader.
* [Py5Surface](/reference/py5surface) - The Py5Surface object is the actual window py5 draws animations to. You can use this to interact with the window and change some of its characteristics, such as the window title or location.
* [Py5Font](/reference/py5font) - Py5Font is the font class for py5. To create a font to use with py5, use `create_font_file()`. This will create a font in the format py5 requires.
* [Py5MouseEvent](/reference/py5mouseevent) - A Py5MouseEvent object will be passed to user-defined mouse event functions. Useful for capturing all of a user’s mouse activity.
* [Py5KeyEvent](/reference/py5keyevent) - A Py5MouseEvent object will be passed to user-defined mouse event functions. Useful for capturing all of a user’s keyboard activity.
* [Py5Vector](/reference/py5vector) - Class to describe a 2D, 3D, or 4D vector. A vector is an entity that has both a magnitude and a direction. This datatype stores the components of the vector as a set of coordinates.

### Tools

* [Py5 Magics](/reference/py5magics) - The py5 Magics are Jupyter Notebook “meta-commands” that can be within Jupyter Notebooks to enhance py5’s ability to work within the notebook. The py5 magics will enable users to create Sketches and embed the results in the Notebook without defining any functions or calling the `size()` function.
* [Py5 Tools](/reference/py5tools) - The py5 Tools are extra utility functions not directly related to creating Sketches that help facilitate the use of py5. For example, you can use these to add jar files to the Java classpath before importing py5.
* [Py5 Functions](/reference/py5functions) - The py5 Functions are extra utility functions that make py5 easier to use. For example, you can use these to Processing’s vlw font files without having to use Processing’s IDE.
