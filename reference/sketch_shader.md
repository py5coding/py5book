# shader()

Applies the shader specified by the parameters.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global edges
    global img
    py5.size(640, 360, py5.P2D)
    img = py5.load_image("leaves.jpg")
    edges = py5.load_shader("edges.glsl")


def draw():
    py5.shader(edges)
    py5.image(img, 0, 0)
```
From  the `data` folder, the sketch will load the `edges.glsl` file below.

```glsl
#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_TEXTURE_SHADER

uniform sampler2D texture;
uniform vec2 texOffset;

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main(void) {
  // Grouping texcoord variables in order to make it work in the GMA 950. See post #13
  // in this thread:
  // http://www.idevgames.com/forums/thread-3467.html
  vec2 tc0 = vertTexCoord.st + vec2(-texOffset.s, -texOffset.t);
  vec2 tc1 = vertTexCoord.st + vec2(         0.0, -texOffset.t);
  vec2 tc2 = vertTexCoord.st + vec2(+texOffset.s, -texOffset.t);
  vec2 tc3 = vertTexCoord.st + vec2(-texOffset.s,          0.0);
  vec2 tc4 = vertTexCoord.st + vec2(         0.0,          0.0);
  vec2 tc5 = vertTexCoord.st + vec2(+texOffset.s,          0.0);
  vec2 tc6 = vertTexCoord.st + vec2(-texOffset.s, +texOffset.t);
  vec2 tc7 = vertTexCoord.st + vec2(         0.0, +texOffset.t);
  vec2 tc8 = vertTexCoord.st + vec2(+texOffset.s, +texOffset.t);
  
  vec4 col0 = texture2D(texture, tc0);
  vec4 col1 = texture2D(texture, tc1);
  vec4 col2 = texture2D(texture, tc2);
  vec4 col3 = texture2D(texture, tc3);
  vec4 col4 = texture2D(texture, tc4);
  vec4 col5 = texture2D(texture, tc5);
  vec4 col6 = texture2D(texture, tc6);
  vec4 col7 = texture2D(texture, tc7);
  vec4 col8 = texture2D(texture, tc8);

  vec4 sum = 8.0 * col4 - (col0 + col1 + col2 + col3 + col5 + col6 + col7 + col8); 
  gl_FragColor = vec4(sum.rgb, 1.0) * vertColor;
}
```

</div></div>

</div>

## Description

Applies the shader specified by the parameters. It's compatible with the `P2D` and `P3D` renderers, but not with the default renderer.

Underlying Processing method: [shader](https://processing.org/reference/shader_.html)

## Signatures

```python
shader(
    shader: Py5Shader,  # name of shader file
    /,
) -> None

shader(
    shader: Py5Shader,  # name of shader file
    kind: int,  # type of shader, either POINTS, LINES, or TRIANGLES
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
