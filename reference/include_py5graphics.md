<table style="width:100%"><tr><td style="vertical-align:top">


### Pgraphics

#### Method

* [begin_draw()](py5graphics_begin_draw)
* [clear()](py5graphics_clear)
* [end_draw()](py5graphics_end_draw)

### Pimage

* [mask()](py5graphics_mask)

### Color

#### Creating / Reading

* [alpha()](py5graphics_alpha)
* [blue()](py5graphics_blue)
* [brightness()](py5graphics_brightness)
* [color()](py5graphics_color)
* [green()](py5graphics_green)
* [hue()](py5graphics_hue)
* [lerp_color()](py5graphics_lerp_color)
* [red()](py5graphics_red)
* [saturation()](py5graphics_saturation)

#### Setting

* [background()](py5graphics_background)
* [color_mode()](py5graphics_color_mode)
* [fill()](py5graphics_fill)
* [no_fill()](py5graphics_no_fill)
* [no_stroke()](py5graphics_no_stroke)
* [stroke()](py5graphics_stroke)

### Environment

* [height](py5graphics_height)
* [next_page()](py5graphics_next_page)
* [no_smooth()](py5graphics_no_smooth)
* [pixel_density](py5graphics_pixel_density)
* [pixel_height](py5graphics_pixel_height)
* [pixel_width](py5graphics_pixel_width)
* [smooth()](py5graphics_smooth)
* [width](py5graphics_width)

### Image

#### Loading / Displaying

* [image()](py5graphics_image)
* [image_mode()](py5graphics_image_mode)
* [no_tint()](py5graphics_no_tint)
* [tint()](py5graphics_tint)

#### Pixels

* [apply_filter()](py5graphics_apply_filter)
* [blend()](py5graphics_blend)
* [copy()](py5graphics_copy)
* [get()](py5graphics_get)
* [load_np_pixels()](py5graphics_load_np_pixels)
* [load_pixels()](py5graphics_load_pixels)
* [np_pixels[]](py5graphics_np_pixels)
* [pixels[]](py5graphics_pixels)
* [set_np_pixels()](py5graphics_set_np_pixels)
* [update_np_pixels()](py5graphics_update_np_pixels)
* [update_pixels()](py5graphics_update_pixels)

#### Textures

* [texture()](py5graphics_texture)
* [texture_mode()](py5graphics_texture_mode)
* [texture_wrap()](py5graphics_texture_wrap)


    </td><td style="vertical-align:top">


### Lights & Camera

#### Camera

* [begin_camera()](py5graphics_begin_camera)
* [camera()](py5graphics_camera)
* [end_camera()](py5graphics_end_camera)
* [frustum()](py5graphics_frustum)
* [ortho()](py5graphics_ortho)
* [perspective()](py5graphics_perspective)
* [print_camera()](py5graphics_print_camera)
* [print_projection()](py5graphics_print_projection)

#### Coordinates

* [model_x()](py5graphics_model_x)
* [model_y()](py5graphics_model_y)
* [model_z()](py5graphics_model_z)
* [screen_x()](py5graphics_screen_x)
* [screen_y()](py5graphics_screen_y)
* [screen_z()](py5graphics_screen_z)

#### Lights

* [ambient_light()](py5graphics_ambient_light)
* [directional_light()](py5graphics_directional_light)
* [light_falloff()](py5graphics_light_falloff)
* [light_specular()](py5graphics_light_specular)
* [lights()](py5graphics_lights)
* [no_lights()](py5graphics_no_lights)
* [normal()](py5graphics_normal)
* [point_light()](py5graphics_point_light)
* [spot_light()](py5graphics_spot_light)

#### Material Properties

* [ambient()](py5graphics_ambient)
* [emissive()](py5graphics_emissive)
* [shininess()](py5graphics_shininess)
* [specular()](py5graphics_specular)

### Output

#### Files

* [begin_raw()](py5graphics_begin_raw)
* [end_raw()](py5graphics_end_raw)

#### Image

* [save()](py5graphics_save)

### Rendering

* [blend_mode()](py5graphics_blend_mode)
* [clip()](py5graphics_clip)
* [flush()](py5graphics_flush)
* [hint()](py5graphics_hint)
* [no_clip()](py5graphics_no_clip)

#### Shaders

* [load_shader()](py5graphics_load_shader)
* [reset_shader()](py5graphics_reset_shader)
* [shader()](py5graphics_shader)


    </td><td style="vertical-align:top">


### Shape

* [create_shape()](py5graphics_create_shape)
* [load_shape()](py5graphics_load_shape)

#### 2D Primitives

* [arc()](py5graphics_arc)
* [circle()](py5graphics_circle)
* [ellipse()](py5graphics_ellipse)
* [line()](py5graphics_line)
* [lines()](py5graphics_lines)
* [point()](py5graphics_point)
* [points()](py5graphics_points)
* [quad()](py5graphics_quad)
* [rect()](py5graphics_rect)
* [square()](py5graphics_square)
* [triangle()](py5graphics_triangle)

#### 3D Primitives

* [box()](py5graphics_box)
* [sphere()](py5graphics_sphere)
* [sphere_detail()](py5graphics_sphere_detail)

#### Attributes

* [ellipse_mode()](py5graphics_ellipse_mode)
* [rect_mode()](py5graphics_rect_mode)
* [stroke_cap()](py5graphics_stroke_cap)
* [stroke_join()](py5graphics_stroke_join)
* [stroke_weight()](py5graphics_stroke_weight)

#### Curves

* [bezier()](py5graphics_bezier)
* [bezier_detail()](py5graphics_bezier_detail)
* [bezier_point()](py5graphics_bezier_point)
* [bezier_tangent()](py5graphics_bezier_tangent)
* [curve()](py5graphics_curve)
* [curve_detail()](py5graphics_curve_detail)
* [curve_point()](py5graphics_curve_point)
* [curve_tangent()](py5graphics_curve_tangent)
* [curve_tightness()](py5graphics_curve_tightness)

#### Loading / Displaying

* [shape()](py5graphics_shape)
* [shape_mode()](py5graphics_shape_mode)

#### Vertex

* [begin_closed_shape()](py5graphics_begin_closed_shape)
* [begin_contour()](py5graphics_begin_contour)
* [begin_shape()](py5graphics_begin_shape)
* [bezier_vertex()](py5graphics_bezier_vertex)
* [bezier_vertices()](py5graphics_bezier_vertices)
* [curve_vertex()](py5graphics_curve_vertex)
* [curve_vertices()](py5graphics_curve_vertices)
* [end_contour()](py5graphics_end_contour)
* [end_shape()](py5graphics_end_shape)
* [quadratic_vertex()](py5graphics_quadratic_vertex)
* [quadratic_vertices()](py5graphics_quadratic_vertices)
* [vertex()](py5graphics_vertex)
* [vertices()](py5graphics_vertices)

### Structure

* [pop()](py5graphics_pop)
* [pop_style()](py5graphics_pop_style)
* [push()](py5graphics_push)
* [push_style()](py5graphics_push_style)

### Transform

* [apply_matrix()](py5graphics_apply_matrix)
* [get_matrix()](py5graphics_get_matrix)
* [pop_matrix()](py5graphics_pop_matrix)
* [print_matrix()](py5graphics_print_matrix)
* [push_matrix()](py5graphics_push_matrix)
* [reset_matrix()](py5graphics_reset_matrix)
* [rotate()](py5graphics_rotate)
* [rotate_x()](py5graphics_rotate_x)
* [rotate_y()](py5graphics_rotate_y)
* [rotate_z()](py5graphics_rotate_z)
* [scale()](py5graphics_scale)
* [set_matrix()](py5graphics_set_matrix)
* [shear_x()](py5graphics_shear_x)
* [shear_y()](py5graphics_shear_y)
* [translate()](py5graphics_translate)

### Typography

#### Attributes

* [text_align()](py5graphics_text_align)
* [text_leading()](py5graphics_text_leading)
* [text_mode()](py5graphics_text_mode)
* [text_size()](py5graphics_text_size)
* [text_width()](py5graphics_text_width)

#### Loading / Displaying

* [text()](py5graphics_text)
* [text_font()](py5graphics_text_font)

#### Metrics

* [text_ascent()](py5graphics_text_ascent)
* [text_descent()](py5graphics_text_descent)


    </td></tr></table>

