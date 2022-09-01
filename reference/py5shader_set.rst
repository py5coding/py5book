Py5Shader.set()
===============

Sets the uniform variables inside the shader to modify the effect while the program is running.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global tex
        global deform
        py5.size(640, 360, py5.P2D)
        tex = py5.load_image("tex1.jpg")
        deform = py5.load_shader("deform.glsl")
        deform.set("resolution", float(py5.width), float(py5.height))


    def draw():
        deform.set("time", py5.millis() / 1000.0)
        deform.set("mouse", float(py5.mouse_x), float(py5.mouse_y))
        py5.shader(deform)
        py5.image(tex, 0, 0, py5.width, py5.height)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the uniform variables inside the shader to modify the effect while the program is running.

Underlying Processing method: `PShader.set <https://processing.org/reference/PShader_set_.html>`_

Signatures
----------

.. code:: python

    set(
        name: str,  # the name of the uniform variable to modify
        boolvec: JArray(JBoolean),  # modifies all the components of an array/vector uniform variable
        ncoords: int,  # number of coordinates per element, max 4
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        mat: npt.NDArray[np.floating],  # 2D numpy array of values with shape 2x3 for 2D matrices or 4x4 for 3D matrices
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        mat: npt.NDArray[np.floating],  # 2D numpy array of values with shape 2x3 for 2D matrices or 4x4 for 3D matrices
        use3x3: bool,  # enforces the numpy array is 3 x 3
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        tex: Py5Image,  # sets the sampler uniform variable to read from this image texture
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        vec: JArray(JBoolean),  # modifies all the components of an array/vector uniform variable
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        vec: Py5Vector,  # vector of values to modify all the components of an array/vector uniform variable
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        vec: npt.NDArray[np.floating],  # 1D numpy array of values to modify all the components of an array/vector uniform variable
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        vec: npt.NDArray[np.floating],  # 1D numpy array of values to modify all the components of an array/vector uniform variable
        ncoords: int,  # number of coordinates per element, max 4
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        vec: npt.NDArray[np.integer],  # 1D numpy array of values to modify all the components of an array/vector uniform variable
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        vec: npt.NDArray[np.integer],  # 1D numpy array of values to modify all the components of an array/vector uniform variable
        ncoords: int,  # number of coordinates per element, max 4
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        x: bool,  # first component of the variable to modify
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        x: bool,  # first component of the variable to modify
        y: bool,  # second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        x: bool,  # first component of the variable to modify
        y: bool,  # second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)
        z: bool,  # third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        x: bool,  # first component of the variable to modify
        y: bool,  # second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)
        z: bool,  # third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)
        w: bool,  # fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        x: float,  # first component of the variable to modify
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        x: float,  # first component of the variable to modify
        y: float,  # second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        x: float,  # first component of the variable to modify
        y: float,  # second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)
        z: float,  # third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        x: float,  # first component of the variable to modify
        y: float,  # second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)
        z: float,  # third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)
        w: float,  # fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        x: int,  # first component of the variable to modify
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        x: int,  # first component of the variable to modify
        y: int,  # second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        x: int,  # first component of the variable to modify
        y: int,  # second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)
        z: int,  # third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)
        /,
    ) -> None

    set(
        name: str,  # the name of the uniform variable to modify
        x: int,  # first component of the variable to modify
        y: int,  # second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)
        z: int,  # third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)
        w: int,  # fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

