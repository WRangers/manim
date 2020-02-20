# MIT License
#
# Copyright (C) <2020> <Rangers>
#
# The animations were generated using the engine manim based on 3B1B's opensource
# module: https://github.com/3b1b/manim.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from manimlib.imports import *
from scipy import signal, fftpack
from sympy import symbols
from sympy.utilities.lambdify import lambdify, implemented_function
from sympy.abc import x


class MRText(Text):
    CONFIG = {
        'font': 'MR CANFIELDS',
        'size': 0.7
    }


class Rangers(Scene):
    def construct(self):
        eng = TextMobject('Animation Engine')
        man = MRText('Manim')
        man.next_to(eng, DOWN)
        manim = VGroup(eng, man)
        manim.move_to(RIGHT*3.5)

        l = Line(np.array([0, 1, 0]), np.array([0, -1, 0]))

        ma = TextMobject('Maker')
        me = MRText('Rangers')
        me.next_to(ma, DOWN)
        rangers = VGroup(ma, me)
        rangers.move_to(LEFT*3.5)

        self.play(Write(rangers), Write(manim))
        self.play(ShowCreation(l))
        self.wait(2)

# 1 系统时变性质的判断


class TIS_S(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 7,
        "y_min": 0,
        "y_max": 2,
        "y_tick_frequency": 1,
        "x_tick_frequency": 1,
        "x_axis_label": "$t$",
        "y_axis_label": "$f(t)$",
        "x_labeled_nums": range(0, 7, 1),
        "y_labeled_nums": range(1, 2, 1),
        "exclude_zero_label": False,
        "axes_color": GREEN,
    }

    def construct(self):
        self.setup_axes(animate=True)

        signal = self.get_graph(lambda x: 1,
                                color=BLUE,
                                x_min=1,
                                x_max=3)

        vert_line = self.get_vertical_lines_to_graph(signal,
                                                     x_min=1,
                                                     x_max=3,
                                                     num_lines=2)

        Signal = VGroup(signal, vert_line)

        self.play(ShowCreation(Signal), run_time=1)
        self.wait(1)
        self.play(ApplyMethod(Signal.shift, 2 *
                              np.array([self.space_unit_to_x, 0, 0])), run_time=1)
        self.wait(1)


class TIS_R(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 7,
        "y_min": 0,
        "y_max": 2,
        "y_tick_frequency": 1,
        "x_tick_frequency": 1,
        "x_axis_label": "$t$",
        "y_axis_label": "$y_s(t)$",
        "x_labeled_nums": range(0, 7, 1),
        "y_labeled_nums": range(1, 2, 1),
        "exclude_zero_label": False,
        "axes_color": GREEN,
    }

    def construct(self):
        self.setup_axes(animate=True)

        system_respnse = self.get_graph(lambda x: 14*(x-2)*np.exp(-3*(x-2)),
                                        color=RED,
                                        x_min=2,
                                        x_max=4)

        self.play(ShowCreation(system_respnse), run_time=1)
        self.wait(1)
        self.play(ApplyMethod(system_respnse.shift, 2 *
                              np.array([self.space_unit_to_x, 0, 0])), run_time=1)
        self.wait(1)


class SystemResponeseText(Scene):
    def construct(self):
        sys = TextMobject("System")
        res = TextMobject("Response")
        arrow = Arrow(LEFT, RIGHT, buff=0.05)

        sys.next_to(arrow, UP)
        res.next_to(arrow, DOWN)

        text = VGroup(sys, res, arrow)

        self.play(Write(text), run_time=1)

# 2 理解卷积


class PassagersTimeCurve(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 30,
        "y_min": 0,
        "y_max": 10,
        "y_tick_frequency": 1,
        "x_tick_frequency": 1,
        "x_axis_label": "$t$",
        "y_axis_label": "$y_p(t)$",
        "axes_color": GREEN,
    }

    def construct(self):
        self.setup_axes(animate=True)

        tp = self.coords_to_point(1, 0)
        tp_text = TexMobject("t_p")
        tp_text.next_to(tp, DOWN)
        arrow = Arrow(self.coords_to_point(1, 1),
                      self.coords_to_point(1, 0), buff=0.05)

        tg = self.coords_to_point(16, 0)
        tg_text = TexMobject("t_p+15")
        tg_text.next_to(tg, DOWN)
        passagers_graph = self.get_graph(lambda x: 10*(x-16)*np.exp(-0.5*(x-16)),
                                         color=RED,
                                         x_min=16, x_max=30)

        self.play(Write(tp_text), Write(arrow))
        self.play(ShowCreation(passagers_graph), Write(tg_text))
        self.wait(2)


class PassagersTimeCurve2(GraphScene, MovingCameraScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 30,
        "y_min": 0,
        "y_max": 10,
        "y_tick_frequency": 1,
        "x_tick_frequency": 1,
        "x_axis_label": "$t$",
        "y_axis_label": "$y_p(t)$",
        "axes_color": GREEN,
    }

    def construct(self):
        self.setup_axes(animate=True)

        passagers_graph = []
        for i in range(1, 6):
            tp = self.coords_to_point(i, 0)
            arrow = Arrow(self.coords_to_point(i, 1),
                          self.coords_to_point(i, 0), buff=0.05)

            tg = self.coords_to_point(i+15, 0)
            passagers_graph.append(self.get_graph(lambda x: 10*(x-i-15)*np.exp(-0.5*(x-i-15)),
                                                  color=RED,
                                                  x_min=i+15, x_max=30))

            self.play(ShowCreation(arrow))
            self.play(ShowCreation(passagers_graph[-1]))
            self.wait(0.5)

        total_function = self.get_graph(self.total_passagers,
                                        color=YELLOW,
                                        x_min=16,
                                        x_max=30)
        self.wait(1)
        independent_graphs = VGroup(*passagers_graph)
        self.play(
            Transform(independent_graphs, total_function),
            self.camera_frame.scale, 4
        )
        self.wait(2)

    def total_passagers(self, x):
        f = 0
        for i in range(1, 6):
            f += 10*(x-i-15)*np.exp(-0.5*(x-i-15))*(x >= i+15)
        return f

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)


class PassagersSignal(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 30,
        "y_min": 0,
        "y_max": 10,
        "y_tick_frequency": 1,
        "x_tick_frequency": 1,
        "x_axis_label": "$t$",
        "y_axis_label": "$f(t)$",
        "axes_color": GREEN,
    }

    def construct(self):
        self.setup_axes(animate=True)

        for i, k in zip(range(1, 6), [1, 2, 4, 1, 3]):
            n = self.coords_to_point(i, k)
            ponit = Dot().move_to(n)
            line = Line(self.coords_to_point(i, 0), n)
            point_line = VGroup(ponit, line)

            self.play(ShowCreation(point_line), run_time=1)
            self.wait(0.5)

        self.wait(3)


class PassagersResponse(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 30,
        "y_min": 0,
        "y_max": 100,
        "y_tick_frequency": 10,
        "x_tick_frequency": 1,
        "x_axis_label": "$t$",
        "y_axis_label": "$y_p(t)$",
        "axes_color": GREEN,
    }

    def construct(self):
        self.setup_axes(animate=True)

        passagers_graph = []
        for i, k in zip(range(1, 6), [1, 2, 4, 1, 3]):
            passagers_graph.append((self.get_graph(lambda x: 10*k*(x-i-15)*np.exp(-0.5*(x-i-15)),
                                                   color=RED,
                                                   x_min=i+15, x_max=30)))

            self.play(ShowCreation(passagers_graph[-1]), run_time=1)
            self.wait(0.5)

        independent_graphs = VGroup(*passagers_graph)
        total_function = self.get_graph(self.total_passagers,
                                        color=YELLOW,
                                        x_min=16,
                                        x_max=30)

        self.play(
            Transform(independent_graphs, total_function),
            run_time=1
        )
        self.wait(2)

    def total_passagers(self, x):
        f = 0
        for i, k in zip(range(1, 6), [1, 2, 4, 1, 3]):
            f += 10*k*(x-i-15)*np.exp(-0.5*(x-i-15))*(x >= i+15)
        return f


class PassagersContiniousSignal(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 30,
        "y_min": 0,
        "y_max": 10,
        "y_tick_frequency": 1,
        "x_tick_frequency": 1,
        "x_axis_label": "$t$",
        "y_axis_label": "$f(t)$",
        "axes_color": GREEN,
    }

    def construct(self):
        self.setup_axes(animate=True)
        signal = self.get_graph(lambda x: 0.5*x*np.cos(x)+2,
                                color=WHITE,
                                x_min=0,
                                x_max=7)

        self.play(ShowCreation(signal), run_time=7)
        self.wait(2)


class PassagersContiniousResponse(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 30,
        "y_min": 0,
        "y_max": 100,
        "y_tick_frequency": 10,
        "x_tick_frequency": 1,
        "x_axis_label": "$t$",
        "y_axis_label": "$f(t)$",
        "axes_color": GREEN,
    }

    def construct(self):
        self.setup_axes(animate=True)
        graphs = []
        for i in np.arange(0, 7.01, 0.01):
            graphs.append(self.get_graph(lambda x: (0.5*x*np.cos(x)+2)*10*(x-i)*np.exp(-0.5*(x-i)),
                                         color=RED,
                                         x_min=0,
                                         x_max=7))
            self.play(ShowCreation(graphs[-1]), run_time=0.01)


class UnitResponse(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 17,
        "y_min": 0,
        "y_max": 10,
        "y_tick_frequency": 1,
        "x_tick_frequency": 1,
        "x_axis_label": "$t$",
        "y_axis_label": "$f(t)/y_s(t)$",
        "axes_color": GREEN,
    }

    def construct(self):
        self.setup_axes(animate=True)

        unit = Arrow(self.graph_origin, self.coords_to_point(0, 1), buff=0.05)

        response = []
        for i, k in zip(range(3, 8), [2, 3, 3, 1, 5]):
            line = Line(self.coords_to_point(i, 0),
                        self.coords_to_point(i, k), buff=0.05)
            point = Dot(self.coords_to_point(i, k))
            line_point = VGroup(line, point)
            line_point.set_color(RED)
            response.append(line_point)
        responses = VGroup(*response)

        self.play(ShowCreation(unit))
        self.wait(0.2)
        self.play(ShowCreation(responses))
        self.wait(2)


class ReverseConv(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 17,
        "y_min": 0,
        "y_max": 11,
        "y_tick_frequency": 1,
        "x_tick_frequency": 1,
        "x_axis_label": "$t$",
        "y_axis_label": "$f(t)/y_s(t)$",
        "axes_color": GREEN,
    }

    def construct(self):
        self.setup_axes(animate=True)

        signal = []
        for i, k in zip(range(0, 5), [1, 2, 2, 1, 3]):
            line = Line(self.coords_to_point(i, 0),
                        self.coords_to_point(i, k), buff=0.05)
            point = Dot(self.coords_to_point(i, k))
            line_point = VGroup(line, point)
            signal.append(line_point)
        signals = VGroup(*signal)

        self.play(ShowCreation(signals))
        self.wait(1)
        self.play(ApplyMethod(signals.shift, -5 *
                              np.array([self.space_unit_to_x, 0, 0])))

        unit = Arrow(self.graph_origin, self.coords_to_point(0, 1), buff=0.05)
        self.play(ShowCreation(unit))

        responses = []
        for n in range(0, 5):
            res = []
            for i, k in zip(range(3+n, 8+n), [2, 3, 3, 1, 5]):
                line = Line(self.coords_to_point(i, 0),
                            self.coords_to_point(i, k), buff=0.05)
                point = Dot(self.coords_to_point(i, k))
                line_point = VGroup(line, point)
                line_point.set_color(RED)
                res.append(line_point)
            response = VGroup(*res)
            responses.append(response)
        independent_res = VGroup(*responses)

        for i in range(0, 5):
            self.play(ApplyMethod(
                signals[i].shift, (5-i)*np.array([self.space_unit_to_x, 0, 0])))
            self.play(ShowCreation(responses[i]))
            self.play(FadeOut(signals[i]))
            self.wait(0.5)
        self.play(FadeOut(unit))

        total_response = []
        for i, k in zip(range(3, 12), [2, 5, 5, 6, 11, 9, 6, 5]):
            line = Line(self.coords_to_point(i, 0),
                        self.coords_to_point(i, k), buff=0.05)
            point = Dot(self.coords_to_point(i, k))
            line_point = VGroup(line, point)
            line_point.set_color(RED)
            total_response.append(line_point)
        total_responses = VGroup(*total_response)

        self.play(Transform(independent_res, total_responses))
        self.wait(2)


class ReverseConv2(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 17,
        "y_min": 0,
        "y_max": 11,
        "y_tick_frequency": 1,
        "x_tick_frequency": 1,
        "x_axis_label": "$t$",
        "y_axis_label": "$f(t)/y_s(t)$",
        "axes_color": GREEN,
    }

    def construct(self):
        self.setup_axes(animate=True)

        signal = []
        for i, k in zip(range(0, 5), [1, 2, 2, 1, 3]):
            line = Line(self.coords_to_point(i, 0),
                        self.coords_to_point(i, k), buff=0.05)
            point = Dot(self.coords_to_point(i, k))
            line_point = VGroup(line, point)
            signal.append(line_point)
        signals = VGroup(*signal)

        # signal2=[]
        # for i,k in zip(range(0,5),[3,1,2,2,1]):
        #     line=Line(self.coords_to_point(i,0),self.coords_to_point(i,k),buff=0.05)
        #     point=Dot(self.coords_to_point(i,k))
        #     line_point=VGroup(line,point)
        #     signal2.append(line_point)
        # signals2=VGroup(*signal2)
        # signals2.shift(-5*np.array([self.space_unit_to_x, 0, 0]))

        self.play(ShowCreation(signals))
        self.wait(1)
        self.play(
            ApplyMethod(signal[4].shift, -9 *
                        np.array([self.space_unit_to_x, 0, 0])),
            ApplyMethod(signal[3].shift, -7 *
                        np.array([self.space_unit_to_x, 0, 0])),
            ApplyMethod(signal[2].shift, -5 *
                        np.array([self.space_unit_to_x, 0, 0])),
            ApplyMethod(signal[1].shift, -3 *
                        np.array([self.space_unit_to_x, 0, 0])),
            ApplyMethod(signal[0].shift, -1 *
                        np.array([self.space_unit_to_x, 0, 0])),
        )

        unit = Arrow(self.graph_origin, self.coords_to_point(0, 1), buff=0.05)
        self.play(ShowCreation(unit))

        total_response = []
        for i, k in zip(range(3, 12), [2, 5, 5, 6, 11, 9, 6, 5]):
            line = Line(self.coords_to_point(i, 0),
                        self.coords_to_point(i, k), buff=0.05)
            point = Dot(self.coords_to_point(i, k))
            line_point = VGroup(line, point)
            line_point.set_color(RED)
            total_response.append(line_point)
        total_responses = VGroup(*total_response)

        self.play(ApplyMethod(signals.shift, 5 *
                              np.array([self.space_unit_to_x, 0, 0])), ShowCreation(total_responses))
        self.play(FadeOut(signals), FadeOut(unit))
        self.wait(2)


class GraphDot(Dot):
    CONFIG = {
        "radius": 0.02,
    }


class ConvolutionExample(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 12,
        "y_min": 0,
        "y_max": 300,
        "y_tick_frequency": 25,
        "x_tick_frequency": 1,
        "x_axis_label": "$t$",
        "y_axis_label": "$f(t)/y_s(t)$",
        "axes_color": GREEN,
    }

    def func1(self, x):
        return 1

    def func2(self, x):
        return 2

    def get_conv(self, func1, a, b, func2, c, d):
        x1 = np.arange(a, b, 0.01)
        x2 = np.arange(c, d, 0.01)
        x3 = np.arange(a+c, b+d-0.01, 0.01)

        y1 = [1] * x1.size
        y2 = [2] * x2.size

        conv = signal.fftconvolve(y1, y2)
        # print(conv)
        # print(conv.size)
        # print(x3.size)
        return x3, conv

    def construct(self):
        self.setup_axes()

        fun1_graph1 = self.get_graph(
            lambda x: 40,
            x_min=2,
            x_max=5
        )
        fun1_line1 = self.get_vertical_line_to_graph(2, fun1_graph1)
        fun1_line2 = self.get_vertical_line_to_graph(5, fun1_graph1)
        fun1_graph = VGroup(fun1_graph1, fun1_line1, fun1_line2)
        fun1_graph.set_color(BLUE)

        fun2_graph1 = self.get_graph(
            lambda x: 80,
            x_min=6,
            x_max=7
        )
        fun2_line1 = self.get_vertical_line_to_graph(6, fun2_graph1)
        fun2_line2 = self.get_vertical_line_to_graph(7, fun2_graph1)
        fun2_graph = VGroup(fun2_graph1, fun2_line1, fun2_line2)
        fun2_graph.set_color(RED)

        x, y = self.get_conv(self.func1, 2, 5, self.func2, 6, 7)

        conv = []
        for i, k in zip(x, y):
            conv.append(GraphDot(self.coords_to_point(i, k)))
        conv_graph = VGroup(*conv)
        conv_graph.set_color(YELLOW)

        self.add(fun1_graph, fun2_graph)
        self.wait(1)
        self.play(ApplyMethod(fun2_graph.shift,
                              -8*np.array([self.space_unit_to_x, 0, 0])))
        self.play(Rotate(
            fun2_graph,
            PI,
            axis=UP
        ))
        self.play(ApplyMethod(
            fun2_graph.shift,
            3*np.array([self.space_unit_to_x, 0, 0])
        ),
            rate_func=linear
        )
        self.play(
            ShowCreation(conv_graph),
            ApplyMethod(
                fun2_graph.shift,
                4*np.array([self.space_unit_to_x, 0, 0])
            ),
            rate_func=lingering
        )
        self.wait(2)


# 4 傅里叶级数-变换

class FourierTest(GraphScene):
    CONFIG = {
        "x_min": -7,
        "x_max": 7,
        "y_min": -1.5,
        "y_max": 1.5,
        "y_tick_frequency": 0.5,
        "x_tick_frequency": 1,
        "x_axis_label": "$t$",
        "y_axis_label": "$f(t)$",
        "graph_origin": ORIGIN,
        "axes_color": GREEN,
    }

    def construct(self):
        self.setup_axes(animate=True)

        semi_sin = self.get_graph(
            lambda x: np.cos(2*x)*(np.cos(2*x) > 0),
            x_min=-2*PI,
            x_max=2*PI
        )
        self.play(ShowCreation(semi_sin))

        an_graph = []
        f0 = lambdify(x, 1/PI)
        a0_graph = self.get_graph(
            lambda x: 1/PI+(1/2)*np.cos(x)+(-2/(3*PI))*np.cos(2*x)+
                        
                        (2/PI)*(1/-15)*np.cos(4*x),
            x_min=-2*PI,
            x_max=2*PI
        )
        a0_graph.set_color(RED)
        an_graph.append(a0_graph)
        self.play(ShowCreation(a0_graph))

        func = implemented_function('func', lambda x: (1/2)*np.cos(x))
        f = lambdify(x, func(x))
        a1_graph = self.get_graph(
            lambda x: f(x),
            x_min=-2*PI,
            x_max=2*PI
        )
        a1_graph.set_color(RED)
        an_graph.append(a1_graph)
        self.play(ShowCreation(a1_graph))

        self.play(Transform(an_graph[0].deepcopy(), an_graph[1]),
                  ApplyMethod(an_graph[0].fade, 0.7))


class SemiSinFourier(GraphScene):
    CONFIG = {
        "x_min": -14,
        "x_max": 14,
        "y_min": -1.5,
        "y_max": 1.5,
        "y_tick_frequency": 0.5,
        "x_tick_frequency": 2,
        "x_axis_label": "$t$",
        "y_axis_label": "$f(t)$",
        "graph_origin": ORIGIN,
        "axes_color": GREEN,
        "fourier":[
            lambda x: 1/PI+(1/2)*np.cos(x),
            lambda x: 1/PI+(1/2)*np.cos(x)+
                        (2/(3*PI))*np.cos(2*x),
            lambda x: 1/PI+(1/2)*np.cos(x)+
                        (2/(3*PI))*np.cos(2*x),
            lambda x: 1/PI+(1/2)*np.cos(x)+
                        (2/(3*PI))*np.cos(2*x)+
                        (-2/(15*PI))*np.cos(4*x),
            lambda x: 1/PI+(1/2)*np.cos(x)+
                        (2/(3*PI))*np.cos(2*x)+
                        (-2/(15*PI))*np.cos(4*x),
            lambda x: 1/PI+(1/2)*np.cos(x)+
                        (2/(3*PI))*np.cos(2*x)+
                        (-2/(15*PI))*np.cos(4*x)+
                        (2/(35*PI))*np.cos(6*x),
            lambda x: 1/PI+(1/2)*np.cos(x)+
                        (2/(3*PI))*np.cos(2*x)+
                        (-2/(15*PI))*np.cos(4*x)+
                        (2/(35*PI))*np.cos(6*x)
        ]
    }

    def construct(self):
        self.setup_axes(animate=True)

        semi_sin = self.get_graph(
            lambda x: np.cos(x)*(np.cos(x) > 0)
        )
        semi_sin.set_color(BLUE)
        self.play(ShowCreation(semi_sin))

        an_graph = []
        f0 = lambdify(x, 1/PI)
        a0_graph = self.get_graph(
            lambda x: f0(x),
            # x_min=-4*PI,
            # x_max=4*PI,
            color=RED
        )

        func = implemented_function('func', lambda x: (1/2)*np.cos(x))
        f = lambdify(x, func(x))
        a1_graph = self.get_graph(
            lambda x: f(x),
            # x_min=-4*PI,
            # x_max=4*PI,
            color=RED
        )
        an_graph.append(a1_graph)

        for i in range(2, 8):
            a_graph = self.get_graph(
                lambda x: (2/PI)*(1/(1-i ^ 2))*np.cos(i*PI/2)*np.cos(i*x),
                # x_min=-4*PI,
                # x_max=4*PI,
                color=RED
            )
            an_graph.append(a_graph)

        fourier_graph=[
            self.get_graph(
                f,
                # x_min=-4*PI,
                # x_max=4*PI,
                color=RED
            )
            for f in self.fourier
        ]

        combine=[]
        self.play(ShowCreation(a0_graph))
        for i in range(0,7):
            self.wait(0.3)
            self.play(ShowCreation(an_graph[i]))
            self.wait(0.3)
            if i==0:
                combine.append(VGroup(a0_graph.deepcopy(),an_graph[i].deepcopy()))
                self.play(Transform(combine[-1],
                    fourier_graph[i]
                    ),
                    ApplyMethod(a0_graph.fade,0.9),
                    ApplyMethod(an_graph[i].fade,0.9))
            else:
                combine.append(VGroup(fourier_graph[i-1],an_graph[i].deepcopy()))
                self.play(Transform(combine[-1],
                    fourier_graph[i]
                    ),
                    ApplyMethod(an_graph[i].fade,0.9),
                    ApplyMethod(combine[i-1].fade,1))
        self.wait(2)


# 5 周期傅里叶变换与抽样


# 6 拉普拉斯变换


# 7 零极图与频率响应
