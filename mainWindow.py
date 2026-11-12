import glfw
import moderngl
import struct

class Triangle:
    def __init__(self, ctx):
        triangle = [    -0.5,   -0.5,
                         0.5,   -0.5,
                         0.0,    0.5    ]

        vertex_shader='''
        #version 330
        in vec2 in_vert;
        void main()
        {
            gl_Position = vec4(in_vert, 0.0, 1.0);
        }
        '''
        fragment_shader='''
        #version 330
        out vec4 f_color;
        void main()
        {
            f_color = vec4(0.0, 1.0, 0.0, 0.0);
        }
        '''

        self.prog   = ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        self.VBO    = ctx.buffer(struct.pack('6f', *triangle))  
        self.VAO    = ctx.vertex_array(self.prog, [(self.VBO, '2f', 'in_vert')])

    def render(self):
        self.VAO.render()

def init():
    if not glfw.init():
        raise RuntimeError('Отказ glfw')

def create_window(WIDTH, HEIGHT, title):
    window = glfw.create_window(WIDTH, HEIGHT, title, None, None)
    if not window:
        glfw.terminate()
        raise RuntimeError('Отказ window')
    return window

def run_loop(window, ctx, object_triangle):
    while not glfw.window_should_close(window):
        glfw.poll_events()
        ctx.clear(0.7, 0.0, 1.0, 0.1)
        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(window, True)
        object_triangle.render()
        glfw.swap_buffers(window)

def main():
    init()
    window = create_window(800, 600, "3D-engine")
    glfw.make_context_current(window)
    ctx = moderngl.create_context()
    triangle = Triangle(ctx)
    run_loop(window, ctx, triangle)
    glfw.terminate()

if __name__ == "__main__":
    main()

