from manimlib.imports import *
from thD7.video_scenes import *


class SS_1_Preamble(Preamble):
    CONFIG = {
        'c_title': '系统时变性质的判断',
        'e_title': 'Time-Invariant Property of Systems',
        'series': r'\scriptsize Signals and Systems Series\\ \# \sz{1}',
    }


class SS_1_Epilogue(Epilogue):
    CONFIG = {
        'bgm': [
            r'Arryo Seco~-~Curtis Schweitzer\\',
            r'Winter I- First Snow~-~Curtis Schweitzer\\',
        ],
        'acknowledgement': None,
    }


class Introduction(Scene):
    def construct(self):
        set_gpus([0, 1])

        que = TextMobject(r'How do you judge whether a \\ system is time-invariant or not?')\
            .scale(1.5).set_color(BLUE)
        self.play(Write(que))
        self.wait(2)

        system = TexMobject(r'y(t)=f(-t) \cdot f(t-1)').scale(1.5)
        self.play(
            FadeOut(que),
            Write(system)
        )
        self.wait()
        self.play(system.shift, UP*2.5)
        self.wait()

        sys = TexMobject(r'y(t-t_0)=f[-(t-t_0)] \cdot f(t-t_0-1)')
        f = TexMobject(r'f(t-t_0) \rightarrow y_1(t)=f(-t-t_0) \cdot f(t-t_0-1)')\
            .shift(0.5*DOWN)
        eq = TexMobject(r'=').scale(1.5)\
            .shift(2.5*DOWN)\
            .set_x(0.5)
        wh = TextMobject('?')\
            .scale(1.5)\
            .set_x(eq.get_x())\
            .next_to(eq, UP, buff=0.1)\
            .set_color(YELLOW)

        self.play(Write(sys))
        self.wait()
        self.play(
            sys.shift, UP*0.5,
            Write(f)
        )
        self.wait()

        sys2 = sys.copy()[0][0:7]
        f2 = f.copy()[0][8:13]
        self.play(
            sys2.move_to, eq.get_center()+LEFT*2,
            sys2.scale, 1.5,
            f2.move_to, eq.get_center()+RIGHT*1.4,
            f2.scale, 1.5,
            Write(eq),
            Write(wh)
        )
        self.wait()

        neq = Line(eq.get_corner(UR)+0.1*UP, eq.get_corner(DL)+0.1*DOWN)\
            .set_color(RED)
        self.play(Transform(wh, neq))

        self.wait()
        self.play(
            *[FadeOut(i) for i in self.mobjects]
        )

        ans = TextMobject(
            r'$y(t)$ is a time-variant system.').scale(1.5).set_color(BLUE)
        self.play(Write(ans))
        self.wait(4)

        but = TextMobject(r'BUT!').scale(3).set_color(YELLOW)
        self.remove(ans)
        self.add(but)

        why = TextMobject(r'WHY?').scale(3).set_color(YELLOW)\
            .shift(UP*1)
        fourmalls = Group(sys, f).shift(DOWN)

        self.wait()
        self.play(
            Transform(but, why),
            FadeIn(fourmalls)
        )
        self.play(
            FadeToColor(sys[0][8:18], RED),
            FadeToColor(f[0][14:22], RED),
        )
        self.wait()
        self.play(Flash(f[0][18]))
        self.wait()

        text = TextMobject('That is what we are going to talk about.')\
            .set_color(BLUE).scale(1.5)
        self.play(
            *[FadeOut(i) for i in self.mobjects],
            Write(text)
        )
        self.wait()


class Definition(Scene):
    def construct(self):
        set_gpus([0, 1])

        self.title = Title(r'\LARGE Time Invariant').set_color(GREEN)

        self.defination()
        self.system()
        self.graph()
        self.wait(3)
        self.play(*[Uncreate(i) for i in self.mobjects], run_time=2)
        self.wait()

    def defination(self):
        defin = TextMobject(r"""
            \parbox[c][][c]{20em}{
                If a system is initially in its zero state and an arbitrary input signal $f(t)$ causes
                a response $y(t)$ and an input signal $f(t-t_0)$ causes a response $y(t-t_0)$ for any
                arbitrary $t_0$, the system is said to be \emph{time invariant}.
            }
        """).shift(0.5*DOWN)

        self.play(
            Write(self.title)
        )
        self.wait()
        self.play(
            Write(defin),
            run_time=7
        )
        self.wait(5)
        self.play(FadeOut(defin))

    def system(self):
        self.add(self.title)

        system = TexMobject(r'System').set_color(BLUE)\
            .shift(DOWN*0.5)
        rect = Rectangle().surround(system).set_color(BLUE)
        self.signal_text = TextMobject(r'Signal $f(t)$')\
            .shift(DOWN*0.5).next_to(rect, direction=LEFT, buff=1.5)
        self.response_text = TextMobject(r'Response $y(t)$')\
            .shift(DOWN*0.5).next_to(rect, direction=RIGHT, buff=1.5)

        arrow1 = Arrow(self.signal_text.get_right(), rect.get_left())\
            .set_color(BLUE)
        arrow2 = Arrow(rect.get_right(), self.response_text.get_left())\
            .set_color(BLUE)

        self.play(Write(system))
        self.wait()
        self.play(Write(self.signal_text))
        for i in [arrow1, rect, arrow2]:
            self.play(ShowCreation(i))
        self.play(Write(self.response_text))
        self.wait()
        self.play(*[FadeOut(i) for i in self.mobjects[1:2]+self.mobjects[3:6]])

    def graph(self):
        self.add(self.title, self.signal_text, self.response_text)

        axes1 = Axes(
            x_min=0,
            x_max=6,
            y_min=0,
            y_max=4,
            center_point=LEFT*6+DOWN*3
        )
        axes2 = Axes(
            x_min=0,
            x_max=6,
            y_min=0,
            y_max=4,
            center_point=RIGHT*0.5+DOWN*3
        )

        def signal(dx=0):
            return FunctionGraph(
                lambda x: 5.5*(x-dx)*np.exp(-x+dx)*(x > dx),
                x_min=0,
                x_max=5.65,
            ).align_to(axes1.c2p(0, 0), DL)

        def response(dx=3):
            return FunctionGraph(
                lambda x: 2*np.exp(-2 * (x - dx) ** 2),
                x_min=0,
                x_max=5.65,
                color=RED
            ).align_to(axes2.c2p(0, 0), DL)

        def signal_update_fuction(f, alpha):
            dx = interpolate(0, 3, alpha)
            f.become(signal(dx))

        def response_update_fuction(f, alpha):
            dx = interpolate(3, 6, alpha)
            f.become(response(dx))

        s = signal()
        r = response()

        self.play(
            self.signal_text.set_color, YELLOW,
            self.signal_text.move_to, axes1.c2p(3, 4),
            self.response_text.set_color, RED,
            self.response_text.move_to, axes2.c2p(3, 4),
            ShowCreation(axes1),
            ShowCreation(axes2),
        )
        self.wait()
        self.play(
            ShowCreation(s),
            ShowCreation(r),
            run_time=2
        )
        self.wait()

        st0 = TexMobject('+\ t_0')\
            .next_to(self.signal_text[0][-2], RIGHT, buff=0.2)\
            .align_to(self.signal_text[0][-2], UP)\
            .set_color(YELLOW)
        rt0 = TexMobject('+\ t_0')\
            .next_to(self.response_text[0][-1], LEFT, buff=0.1)\
            .align_to(self.response_text[0][-2], UP)\
            .set_color(RED)

        self.play(
            UpdateFromAlphaFunc(s, signal_update_fuction),
            UpdateFromAlphaFunc(r, response_update_fuction),
            FadeIn(st0),
            self.signal_text[0][-1].shift, RIGHT*1.1,
            FadeIn(rt0),
            self.response_text[0][-2::-1].shift, LEFT*1.1,
            rate_func=there_and_back,
            run_time=6
        )
        self.wait(2)

        right = TextMobject('\checkmark').set_color(GREEN)\
            .next_to(self.title, RIGHT, buff=-3)\
            .shift(UP*0.1)
        right_rect = Square().surround(right).set_color(GREEN).set_height(0.6)

        self.play(ShowCreation(right_rect))
        self.play(Write(right))

# preparing scene


class TwoGraphScene(Scene):
    CONFIG = {
        'axes1_x_min': -3,
        'axes1_x_max': 3,
        'axes1_y_min': -2,
        'axes1_y_max': 2,
        'axes1_center_point': LEFT*3.5,
        'graph1_function': None,
        'axes2_x_min': -3,
        'axes2_x_max': 3,
        'axes2_y_min': -2,
        'axes2_y_max': 2,
        'axes2_center_point': RIGHT*3.5,
        'graph2_function': None,
    }

    def axes(self):
        self.axes1 = Axes(
            x_min=self.axes1_x_min,
            x_max=self.axes1_x_max,
            y_min=self.axes1_y_min,
            y_max=self.axes1_y_max,
            center_point=self.axes1_center_point,
        )
        self.axes2 = Axes(
            x_min=self.axes2_x_min,
            x_max=self.axes2_x_max,
            y_min=self.axes2_y_min,
            y_max=self.axes2_y_max,
            center_point=self.axes2_center_point,
        )

    def graph1(self, dx=0):
        return FunctionGraph(
            self.graph1_function,
            x_min=self.axes1_x_min,
            x_max=self.axes1_x_max,
        ).move_to(self.axes1.c2p(0, 0))
        # There is a problem about the alignment.

    def graph2(self, dx=0):
        return FunctionGraph(
            self.graph2_function,
            x_min=self.axes2_x_min,
            x_max=self.axes2_x_max,
            color=RED
        ).move_to(self.axes2.c2p(0, 0))


class Interval(NumberLine):
    CONFIG = {
        "x_min": -2,
        "x_max": 2,
        "unit_size": 1.5,
        "tick_frequency": 0.2,
        "numbers_with_elongated_ticks": [-2, 2],
        "include_numbers": True,
        "numbers_to_show": [-2.0, -1.0, 0.0, 1.0, 2.0],
        "number_at_center": 0,
        "decimal_number_config": {
            "num_decimal_places": 1,
        }
    }

#


class UnderstandingTI(TwoGraphScene):
    CONFIG = {
        'axes1_center_point': LEFT*3.5+DOWN,
        'axes2_center_point': RIGHT*3.5+DOWN,
    }

    def construct(self):
        set_gpus([0, 1])

        self.setuptext()
        self.showtext()
        self.showgraph()
        self.numberlines()
        self.numberpoints()
        self.graphmoving(2)
        # geometry explanation
        self.compare()

    #
    def setuptext(self):
        self.signal = TextMobject('Signal ', r'$f(t)=\sin (t)$')
        self.system = TextMobject('System ', r'$y(t)=f(t) \cdot f(t)$')\
            .shift(3*RIGHT)

        self.response = TextMobject(r'Response\\', r'$f(t+t_0)\longrightarrow y_f(t)=f(t+t_0) \cdot f(t+t_0)$')\
            .shift(1.8*DOWN).scale(0.7)
        self.response[1].set_color(BLUE)

        self.signal_t0 = TextMobject(r'Signal\\', r'$f(t+t_0)=\sin (t+t_0)$')
        self.system_t0 = TextMobject(
            r'System\\', r'$y(t+t_0)=f(t+t_0) \cdot f(t+t_0)$')
        self.signal_t0[1].set_color(YELLOW)
        self.system_t0[1].set_color(RED)

    #
    def showtext(self):
        self.signal.generate_target()
        self.signal.target.shift(3*LEFT)

        self.play(Write(self.signal))
        self.wait()
        self.play(
            MoveToTarget(self.signal),
            Write(self.system)
        )
        self.wait()
        self.play(Indicate(self.system[0][0:6]))
        self.wait(7)

    #
    def showgraph(self):
        self.play(
            self.signal.shift, UP*3,
            self.system.shift, UP*3,
        )

        self.axes()
        self.play(ShowCreation(self.axes1),
                  ShowCreation(self.axes2), run_time=2)
        self.wait()

        self.signal_t0.move_to(self.axes1.c2p(0, 4))
        self.system_t0.move_to(self.axes2.c2p(0, 4))

        self.set_graph()

        self.play(
            ShowCreation(self.signal_graph),
            ShowCreation(self.system_graph),
            self.signal[1].set_color, YELLOW,
            self.system[1].set_color, RED,
            run_time=2
        )
        self.wait()
        self.play(
            Transform(self.signal, self.signal_t0),
            Transform(self.system, self.system_t0),
            Write(self.response)
        )
        self.wait()
        self.play(ShowCreation(self.response_graph))
        self.wait()

    def set_graph(self):
        self.signal_graph = self.graph1().set_color(YELLOW)
        self.system_graph = self.graph2().set_color(RED_E)
        self.response_graph = self.graph3().set_color(BLUE)

    def graph1(self, dx=0):
        return FunctionGraph(
            lambda x: np.sin(x+dx),
            x_min=self.axes1_x_min,
            x_max=self.axes1_x_max,
        ).move_to(self.axes1.c2p(0, 0))

    def graph2(self, dx=0):
        f = FunctionGraph(
            lambda x: np.sin(x+dx)**2,
            # lambda x: np.sin(x-dx)*np.sin(x),
            x_min=self.axes2_x_min,
            x_max=self.axes2_x_max,
            color=RED
        ).move_to(self.axes2.c2p(0, 0))
        f.shift(UP*f.get_height()/2)
        return f

    def graph3(self, dx=0):
        f = FunctionGraph(
            lambda x: np.sin(x+dx)**2,
            # lambda x: np.sin(x-dx)*np.sin(x),
            x_min=self.axes2_x_min,
            x_max=self.axes2_x_max,
            color=BLUE
        ).move_to(self.axes1.c2p(0, 0))
        f.shift(UP*f.get_height()/2)
        return f
    #

    def numberlines(self):
        self.sig_numline = Interval().shift(3.5*LEFT+UP*2)
        self.sys_numline = self.sig_numline.deepcopy().shift(RIGHT*7)
        self.res_numline = self.sig_numline.deepcopy().next_to(
            self.response, DOWN, buff=0.2)

        self.play(
            ShowCreation(self.sig_numline),
            ShowCreation(self.sys_numline),
            ShowCreation(self.res_numline),
            run_time=2
        )
        self.wait()

        self.sig_offset = TextMobject('|offset of the signal graph|').scale(0.6)\
            .next_to(self.sig_numline, DOWN, buff=0.1)
        self.sys_offset = TextMobject('|offset of the system graph|').scale(0.6)\
            .next_to(self.sys_numline, DOWN, buff=0.1)
        self.res_offset = TextMobject('|offset of the response graph|').scale(0.6)\
            .next_to(self.res_numline, DOWN, buff=0.1)

        self.play(
            Write(self.sig_offset),
            Write(self.sys_offset),
            Write(self.res_offset)
        )
        self.wait()

    def numberpoints(self):
        self.t0_text = TexMobject('t_0 = ')

        self.t0 = ValueTracker(0)
        self.t0_num = DecimalNumber(self.t0.get_value())\
            .add_updater(lambda v: v.set_value(self.t0.get_value()))

        self.t0_group = VGroup(self.t0_text, self.t0_num)\
            .arrange(RIGHT, buff=0.2).shift(0.5*UP)

        self.sig_point = Dot(self.sig_numline.n2p(self.t0.get_value())).set_color(YELLOW)\
            .add_updater(lambda m: m.move_to(self.sig_numline.n2p(self.t0.get_value())))
        self.sys_point = Dot(self.sys_numline.n2p(self.t0.get_value())).set_color(RED)\
            .add_updater(lambda m: m.move_to(self.sys_numline.n2p(self.t0.get_value())))
        self.res_point = Dot(self.res_numline.n2p(self.t0.get_value())).set_color(BLUE)\
            .add_updater(lambda m: m.move_to(self.res_numline.n2p(self.t0.get_value())))

        zero_point = self.sig_numline.n2p(0)
        self.sig_line = Line(self.sig_numline.n2p(0), self.sig_numline.n2p(self.t0.get_value())).set_color(YELLOW)\
            .add_updater(
                lambda m: m.become(Line(self.sig_numline.n2p(0), self.sig_numline.n2p(self.t0.get_value()))
                                   .set_color(YELLOW)))
        self.sys_line = Line(self.sys_numline.n2p(0), self.sys_numline.n2p(self.t0.get_value())).set_color(RED)\
            .add_updater(
                lambda m: m.become(Line(self.sys_numline.n2p(0), self.sys_numline.n2p(self.t0.get_value()))
                                   .set_color(RED)))
        self.res_line = Line(self.res_numline.n2p(0), self.res_numline.n2p(self.t0.get_value())).set_color(BLUE)\
            .add_updater(
                lambda m: m.become(Line(self.res_numline.n2p(0), self.res_numline.n2p(self.t0.get_value()))
                                   .set_color(BLUE)))

        self.play(
            Write(self.t0_group),
            ShowCreation(self.sig_point),
            ShowCreation(self.sys_point),
            ShowCreation(self.res_point),
            ShowCreation(self.sys_line),
            ShowCreation(self.sig_line),
            ShowCreation(self.res_line),
        )
        self.wait()

    #
    def graphmoving(self, value=2):
        self.shift_num = value
        self.play(
            self.t0.increment_value, value,
            UpdateFromAlphaFunc(self.signal_graph,
                                self.signal_graph_update_fuction),
            UpdateFromAlphaFunc(self.system_graph,
                                self.system_graph_update_fuction),
            UpdateFromAlphaFunc(self.response_graph,
                                self.response_graph_update_fuction),
            run_time=6
        )
        self.wait(2)

    def signal_graph_update_fuction(self, f, alpha):
        dx = interpolate(0, self.shift_num, alpha)
        f.become(self.graph1(dx))

    def system_graph_update_fuction(self, f, alpha):
        dx = interpolate(0, self.shift_num, alpha)
        f.become(self.graph2(dx))

    def response_graph_update_fuction(self, f, alpha):
        dx = interpolate(0, self.shift_num, alpha)
        f.become(self.graph3(dx))
    #

    def compare(self):
        self.play(
            *[FadeOut(i)
              for i in [self.t0_group, self.axes1, self.axes2,
                        self.signal_graph, self.system_graph, self.response_graph,
                        self.sig_offset, self.sys_offset, self.res_offset]]
        )

        sig_group = VGroup(
            self.signal, self.sig_numline, self.sig_line, self.sig_point
        )
        sys_group = VGroup(
            self.system, self.sys_numline, self.sys_line, self.sys_point
        )

        self.play(
            sig_group.shift, 3.5*RIGHT,
            sys_group.move_to, ORIGIN,
            self.response.scale, 10/7
        )
        self.wait()
        self.play(
            Indicate(self.signal[0]),
            Indicate(self.response[0])
        )
        self.wait()
        self.play(
            Indicate(self.system[0], color=RED),
            Indicate(self.response[0], color=RED)
        )


class UnderstandingTV(UnderstandingTI):
    def construct(self):
        set_gpus([0, 1])

        self.changesystem()
        self.setuptext(0.7)
        self.setupgraph()
        self.setupnumberlines()
        self.setupnumberpoints(1/2)
        self.showup()
        self.graphmoving(2)
        # geometry explanation
        self.compare(10/7)

    #
    def changesystem(self):
        signal = TextMobject(r'Signal $f(t)=\sin (t)$').shift(3*LEFT)
        system = TextMobject(r'System $y(t)=f(t) \cdot f(t)$')\
            .shift(3*RIGHT)
        system2 = TextMobject(r'System $y(t)=f(t) \cdot \sin(t)$')\
            .shift(3*RIGHT)
        text = TextMobject('What is the difference?').scale(1.5)\
            .set_color(YELLOW)

        self.add(signal, system)
        self.wait()
        self.play(Transform(system, system2))
        self.wait()
        self.play(*[FadeOut(i) for i in self.mobjects], Write(text))
        self.wait()
        self.play(FadeOut(text))
        self.wait()

    #
    def setuptext(self, scale=0.7):
        self.response = TextMobject(r'Response\\', r'$f(t+t_0)\longrightarrow y_f(t)=f(t+t_0) \cdot \sin (t)$')\
            .shift(1.8*DOWN).scale(scale)
        self.response[1].set_color(BLUE)

        self.signal = TextMobject(r'Signal\\', r'$f(t+t_0)=\sin (t+t_0)$')
        self.system = TextMobject(
            r'System\\', r'$y(t+t_0)=f(t+t_0) \cdot \sin(t+t_0)$')
        self.signal[1].set_color(YELLOW)
        self.system[1].set_color(RED)

    #
    def setupgraph(self):
        self.axes()
        self.signal.shift(3*UP).set_x(self.axes1.c2p(0, 0)[0])
        self.system.shift(3*UP).set_x(self.axes2.c2p(0, 0)[0])

        self.set_graph()

    def set_graph(self):
        self.signal_graph = self.graph1()
        self.system_graph = self.graph2()
        self.response_graph = self.graph3()

    def graph3(self, dx=0):
        f = FunctionGraph(
            # lambda x: np.sin(x-dx)**2,
            lambda x: np.sin(x+dx)*np.sin(x),
            x_min=self.axes2_x_min,
            x_max=self.axes2_x_max,
            color=BLUE
        ).move_to(self.axes1.c2p(0, 0))
        f.shift(UP*f.get_height()/2)
        return f

    #
    def setupnumberlines(self):
        self.sig_numline = Interval().shift(3.5*LEFT+UP*2)
        self.sys_numline = self.sig_numline.deepcopy().shift(RIGHT*7)
        self.res_numline = self.sig_numline.deepcopy().next_to(
            self.response, DOWN, buff=0.2)

        self.sig_offset = TextMobject('|offset of the signal graph|').scale(0.6)\
            .next_to(self.sig_numline, DOWN, buff=0.1)
        self.sys_offset = TextMobject('|offset of the system graph|').scale(0.6)\
            .next_to(self.sys_numline, DOWN, buff=0.1)
        self.res_offset = TextMobject('|offset of the response graph|').scale(0.6)\
            .next_to(self.res_numline, DOWN, buff=0.1)

    #
    def setupnumberpoints(self, offset=1/2):
        self.t0_text = TexMobject('t_0 = ')

        self.t0 = ValueTracker(0)
        self.t0_num = DecimalNumber(self.t0.get_value())\
            .add_updater(lambda v: v.set_value(self.t0.get_value()))

        self.t0_group = VGroup(self.t0_text, self.t0_num)\
            .arrange(RIGHT, buff=0.2).shift(0.5*UP)

        self.sig_point = Dot(self.sig_numline.n2p(self.t0.get_value())).set_color(YELLOW)\
            .add_updater(lambda m: m.move_to(self.sig_numline.n2p(self.t0.get_value())))
        self.sys_point = Dot(self.sys_numline.n2p(self.t0.get_value())).set_color(RED)\
            .add_updater(lambda m: m.move_to(self.sys_numline.n2p(self.t0.get_value())))
        self.res_point = Dot(self.res_numline.n2p(self.t0.get_value())).set_color(BLUE)\
            .add_updater(lambda m: m.move_to(self.res_numline.n2p(self.t0.get_value()*offset)))

        zero_point = self.sig_numline.n2p(0)
        self.sig_line = Line(self.sig_numline.n2p(0), self.sig_numline.n2p(self.t0.get_value())).set_color(YELLOW)\
            .add_updater(
                lambda m: m.become(Line(self.sig_numline.n2p(0), self.sig_numline.n2p(self.t0.get_value()))
                                   .set_color(YELLOW)))
        self.sys_line = Line(self.sys_numline.n2p(0), self.sys_numline.n2p(self.t0.get_value())).set_color(RED)\
            .add_updater(
                lambda m: m.become(Line(self.sys_numline.n2p(0), self.sys_numline.n2p(self.t0.get_value()))
                                   .set_color(RED)))
        self.res_line = Line(self.res_numline.n2p(0), self.res_numline.n2p(self.t0.get_value())).set_color(BLUE)\
            .add_updater(
                lambda m: m.become(Line(self.res_numline.n2p(0), self.res_numline.n2p(self.t0.get_value()*offset))
                                   .set_color(BLUE)))

    #
    def showup(self):
        self.play(
            *[ShowCreation(i) for i in [self.t0_group, self.axes1, self.axes2,
                                        self.signal_graph, self.system_graph, self.response_graph,
                                        self.sig_offset, self.sys_offset, self.res_offset,
                                        self.signal, self.system, self.response,
                                        self.sig_numline, self.sys_numline, self.res_numline,
                                        self.sig_point, self.sys_point, self.res_point,
                                        self.sig_line, self.sys_line, self.res_line]],
            run_time=2
        )
        self.wait()

    #
    def graphmoving(self, value=2):
        self.shift_num = value
        self.play(
            self.t0.increment_value, value,
            UpdateFromAlphaFunc(self.signal_graph,
                                self.signal_graph_update_fuction),
            UpdateFromAlphaFunc(self.system_graph,
                                self.system_graph_update_fuction),
            UpdateFromAlphaFunc(self.response_graph,
                                self.response_graph_update_fuction),
            run_time=6
        )
        self.wait()

    #
    def compare(self, scale=10/7):
        self.play(
            *[FadeOut(i)
              for i in [self.t0_group, self.axes1, self.axes2,
                        self.signal_graph, self.system_graph, self.response_graph,
                        self.sig_offset, self.sys_offset, self.res_offset]]
        )

        sig_group = VGroup(
            self.signal, self.sig_numline, self.sig_line, self.sig_point
        )
        sys_group = VGroup(
            self.system, self.sys_numline, self.sys_line, self.sys_point
        )

        self.play(
            sig_group.shift, 3.5*RIGHT,
            sys_group.move_to, ORIGIN,
            self.response.scale, scale
        )
        self.wait()
        self.play(
            Indicate(self.signal[0]),
            Indicate(self.response[0])
        )
        self.wait()
        self.play(
            Indicate(self.system[0], color=RED),
            Indicate(self.response[0], color=RED)
        )
        self.wait()


class SignalWithScaleUp(UnderstandingTV):
    def construct(self):
        set_gpus([0, 1])

        self.statement()
        self.setuptext(0.7)
        self.setupgraph()
        self.setupnumberlines()
        self.setupnumberpoints(1/2)
        self.showup()
        # algebra explain
        self.graphmoving(-2)

    #
    def statement(self):
        text = TextMobject('Systems consists of the signals with scaling.')

        systems = []
        for i in ['y(t)=f(2t)',
                  'y(t)=f(\\frac{1}{7}t)',
                  'y(t)=f(t) \\cdot f(2t)',
                  'y(t)=f(2t-7)']:
            systems.append(TexMobject(i).scale(1.2))

        systems[0].move_to(np.array([5, 2, 0]))
        systems[1].move_to(np.array([2, -2, 0]))
        systems[2].move_to(np.array([-3, 3, 0]))
        systems[3].move_to(np.array([-4, -3, 0]))

        self.play(Write(text))
        self.wait()
        self.play(
            *[WriteRandom(i[0]) for i in systems]
        )
        self.wait()
        self.play(
            Indicate(systems[0][0][-3]),
            Indicate(systems[1][0][-5:-2]),
            Indicate(systems[2][0][-3]),
            Indicate(systems[3][0][-5]),
        )
        self.wait()
        self.play(
            *[UnWriteRandom(i[0]) for i in systems]
        )
        self.wait()

        signal = TextMobject(r'Signal $f(t)=\sin (t)$').shift(LEFT*3+DOWN)
        system = TextMobject(r'System $y(t)=f(2t)$').shift(RIGHT*3+DOWN)

        self.play(
            text.shift, UP,
            Write(system),
            Write(signal),
        )
        self.wait()
        self.play(
            *[FadeOut(i) for i in self.mobjects]
        )

    #
    def setuptext(self, scale=0.7):
        self.response = TextMobject(r'Response\\', r'$f(t+t_0)\longrightarrow y_f(t)=f(2t+t_0)$')\
            .shift(1.8*DOWN).scale(scale)
        self.response[1].set_color(BLUE)

        self.signal = TextMobject(r'Signal\\', r'$f(t+t_0)=\sin (t+t_0)$')
        self.system = TextMobject(
            r'System\\', r'$y(t+t_0)=f[2(t+t_0)]$')
        self.signal[1].set_color(YELLOW)
        self.system[1].set_color(RED)

    def graph2(self, dx=0):
        f = FunctionGraph(
            lambda x: np.sin(2*(x+dx)),
            x_min=self.axes2_x_min,
            x_max=self.axes2_x_max,
            color=RED
        ).move_to(self.axes2.c2p(0, 0))
        return f

    def graph3(self, dx=0):
        f = FunctionGraph(
            lambda x: np.sin(2*x+dx),
            x_min=self.axes2_x_min,
            x_max=self.axes2_x_max,
            color=BLUE
        ).move_to(self.axes1.c2p(0, 0))
        return f


class AlgebraExplain(SignalWithScaleUp):
    def construct(self):
        set_gpus([0, 1])

        self.setuptext(0.7)
        self.setupgraph()
        self.setupnumberlines()
        self.setupnumberpoints(1/2)
        self.showup()
        self.explain()

    def showup(self):
        self.add(
            *[i for i in [self.t0_group, self.axes1, self.axes2,
                          self.signal_graph, self.system_graph, self.response_graph,
                          self.sig_offset, self.sys_offset, self.res_offset,
                          self.signal, self.system, self.response,
                          self.sig_numline, self.sys_numline, self.res_numline,
                          self.sig_point, self.sys_point, self.res_point,
                          self.sig_line, self.sys_line, self.res_line]],
        )
        self.wait()

    def explain(self):
        title = Title(r'\LARGE Algebra Explanation').set_color(GREEN)

        signal = TextMobject(
            r'Signal\\', r'$f(t)=\sin (t)$').move_to(3.5*LEFT+UP)
        system = TextMobject(
            r'System\\', r'$y(t)=f(2t)$').move_to(3.5*RIGHT+UP)
        signal[1].set_color(YELLOW)
        system[1].set_color(RED)
        response = self.response.deepcopy()

        self.play(
            Transform(self.signal, signal),
            Transform(self.system, system),
            *[FadeOut(i)
              for i in self.mobjects if i not in [self.signal, self.system]],
            Write(title)
        )
        self.wait()

        t1 = TexMobject('f(t)', '\\longrightarrow y_f(t)').shift(DOWN)
        self.play(Write(t1))
        self.wait()
        self.play(Indicate(self.system[1]))
        self.wait()

        t2 = TexMobject('f(t)', '\\longrightarrow y_f(t)',
                        '=f(2t)').shift(DOWN)
        self.play(
            t1.align_to, t2, LEFT,
            Write(t2[2])
        )
        self.wait()

        t3 = TexMobject('f_1(t)', '=f(t+t_0)').next_to(t2, DOWN)
        self.play(Write(t3))
        self.wait()
        self.play(Indicate(t1))
        self.wait()

        t4 = TexMobject(
            'f_1(t)', r'\longrightarrow y_{f_1}(t)').next_to(t3, DOWN)
        t4_0 = t3[0].deepcopy()
        t4_1 = t1[1].deepcopy()
        self.play(Transform(t4_1, t4[1]),
                  t4_0.move_to, t4[0])
        self.wait()
        self.play(Indicate(t1), Indicate(t2[2]))
        self.wait()
        t4_g = VGroup(t4_0, t4_1)

        t5 = TexMobject(
            'f_1(t)', r'\longrightarrow y_{f_1}(t)', '=f_1(2t)').next_to(t3, DOWN)
        t5_2 = t2[2].deepcopy()
        self.play(
            t4_g.align_to, t5, LEFT,
            Transform(t5_2, t5[2])
        )
        self.wait()
        self.play(Indicate(t3))
        self.wait()
        t5_g = VGroup(t4_g, t5_2)

        t6 = TexMobject(
            'f_1(t)', r'\longrightarrow y_{f_1}(t)', '=f_1(2t)', '=f(2t+t_0)').next_to(t3, DOWN)
        t6_3 = t3[1].deepcopy()
        self.play(
            Transform(t6_3, t6[3]),
            t5_g.align_to, t6, LEFT
        )
        self.wait()

        self.response.scale(10/7).shift(UP*2)
        self.play(Write(self.response))
        self.wait()


class BackToBeginning(Scene):
    def construct(self):
        set_gpus([0, 1])

        self.tobegin()
        self.tonow()
        self.explain()

    def tobegin(self):
        pass  # 后期

    def tonow(self):
        pass  # 后期

    def explain(self):
        title = Title(r'\LARGE Algebra Explanation').set_color(GREEN)

        signal = TextMobject(
            r'Signal\\', r'$f(t)=\sin (t)$').move_to(3.5*LEFT+UP)
        system = TextMobject(
            r'System\\', r'$y(t)=f(-2t+1)\cdot \sin (t)$').move_to(3.5*RIGHT+UP)
        signal[1].set_color(YELLOW)
        system[1].set_color(RED)

        self.add(title, system, signal)

        t1 = TexMobject('f(t)\\longrightarrow y_f(t)').shift(DOWN)
        t2 = TexMobject('f_1(t)', '=f(t+t_0)').next_to(t1, DOWN)
        t3 = TextMobject(r"""
            $$
            \begin{aligned}
            f_{1}(t) \longrightarrow y_{f_1}(t) & =f_1(-2 t+1) \cdot \sin (t) \\
                                                & =f\left(-2 t+1+t_{0}\right) \cdot \sin (t)
            \end{aligned}
            $$
        """).next_to(t1, DOWN).shift(RIGHT*0.4)
        self.play(Write(t1))
        self.wait()
        self.play(Write(t2))
        self.wait()

        t_g = VGroup(t1, t2)
        self.play(Write(t3),
                  t_g.shift, UP*0.7)
        self.wait()

        self.play(
            Indicate(t3[0][-16:-11]),
            Indicate(t3[0][-32:-27])
        )
        self.wait()


class SignalWithScaleDown(SignalWithScaleUp):
    def construct(self):
        set_gpus([0, 1])

        self.statement()
        self.setuptext(0.7)
        self.setupgraph()
        self.setupnumberlines()
        self.setupnumberpoints(2)
        self.showup()
        self.graphmoving(1)

    def statement(self):
        text = TextMobject(r'What about the system $y(t)=f(\frac{1}{2}t)$ ?').scale(1.5)\
            .set_color(YELLOW)

        self.play(
            Write(text)
        )
        self.wait()
        self.play(FadeOut(text))

    def setuptext(self, scale=0.7):
        self.response = TextMobject(r'Response\\', r'$f(t+t_0)\longrightarrow y_f(t)=f(\frac{1}{2}t+t_0)$')\
            .shift(1.8*DOWN).scale(scale)
        self.response[1].set_color(BLUE)

        self.signal = TextMobject(r'Signal\\', r'$f(t+t_0)=\sin (t+t_0)$')
        self.system = TextMobject(
            r'System\\', r'$y(t+t_0)=f[\frac{1}{2}(t+t_0)]$')
        self.signal[1].set_color(YELLOW)
        self.system[1].set_color(RED)

    def graph2(self, dx=0):  # alignment
        f = FunctionGraph(
            lambda x: np.sin(0.5*(x+dx)),
            x_min=self.axes2_x_min,
            x_max=self.axes2_x_max,
            color=RED
        ).align_to(self.axes2.c2p(0, 1), UP).shift(RIGHT*3.5)
        return f

    def graph3(self, dx=0):  # alignment
        f = FunctionGraph(
            lambda x: np.sin(0.5*x+dx),
            x_min=self.axes2_x_min,
            x_max=self.axes2_x_max,
            color=BLUE
        ).align_to(self.axes1.c2p(0, 1), UP).shift(LEFT*3.5)
        return f

    def system_graph_update_fuction(self, f, alpha):
        dx = interpolate(0, self.shift_num, alpha)
        f.become(self.graph2(dx))

    def response_graph_update_fuction(self, f, alpha):
        dx = interpolate(0, self.shift_num, alpha)
        f.become(self.graph3(dx))


class SignalWithShifting(SignalWithScaleUp):
    def construct(self):
        set_gpus([0, 1])

        self.statement()
        self.setuptext(0.7)
        self.setupgraph()
        self.setupnumberlines()
        self.setupnumberpoints(1)
        self.showup()
        self.graphmoving(-2)

    def statement(self):
        text = TextMobject('Systems consists of the signals with shift.')

        signal = TextMobject(r'Signal $f(t)=\sin (t)$').shift(LEFT*3+DOWN)
        system = TextMobject(r'System $y(t)=f(t-1)$').shift(RIGHT*3+DOWN)

        self.play(Write(text))
        self.wait()
        self.play(
            text.shift, UP,
            Write(system),
            Write(signal),
        )
        self.wait()
        self.play(
            *[FadeOut(i) for i in self.mobjects]
        )

    def setuptext(self, scale=0.7):
        self.response = TextMobject(r'Response\\', r'$f(t+t_0)\longrightarrow y_f(t)=f(t-1+t_0)$')\
            .shift(1.8*DOWN).scale(scale)
        self.response[1].set_color(BLUE)

        self.signal = TextMobject(r'Signal\\', r'$f(t+t_0)=\sin (t+t_0)$')
        self.system = TextMobject(
            r'System\\', r'$y(t+t_0)=f(t+t_0-1)$')
        self.signal[1].set_color(YELLOW)
        self.system[1].set_color(RED)

    def graph2(self, dx=0):
        f = FunctionGraph(
            lambda x: np.sin(x-1+dx),
            x_min=self.axes2_x_min,
            x_max=self.axes2_x_max,
            color=RED
        ).move_to(self.axes2.c2p(0, 0))
        return f

    def graph3(self, dx=0):
        f = FunctionGraph(
            lambda x: np.sin(x-1+dx),
            x_min=self.axes2_x_min,
            x_max=self.axes2_x_max,
            color=BLUE
        ).move_to(self.axes1.c2p(0, 0))
        return f


class ComprehansiveSystem(SignalWithScaleUp):
    def construct(self):
        set_gpus([0, 1])

        self.statement()
        self.setuptext(0.7)
        self.setupgraph()
        self.setupnumberlines()
        self.setupnumberpoints(-1/2)
        self.showup()
        self.graphmoving(-2)

    def statement(self):
        text = TextMobject('A comprehensive system.')

        signal = TextMobject(r'Signal $f(t)=\sin (t)$').shift(LEFT*3+DOWN)
        system = TextMobject(
            r'System $y(t)=f(-2t+1)\cdot \sin(t)$').shift(RIGHT*3+DOWN)

        self.play(Write(text))
        self.wait()
        self.play(
            text.shift, UP,
            Write(system),
            Write(signal),
        )
        self.wait()
        self.play(
            *[FadeOut(i) for i in self.mobjects]
        )

    def setuptext(self, scale=0.7):
        self.response = TextMobject(r'Response\\', r'$f(t+t_0)\longrightarrow y_f(t)=f\left(-2 t+1+t_{0}\right) \cdot \sin (t)$')\
            .shift(1.8*DOWN).scale(scale)
        self.response[1].set_color(BLUE)

        self.signal = TextMobject(r'Signal\\', r'$f(t+t_0)=\sin (t+t_0)$')
        self.system = TextMobject(
            r'System\\', r'$y(t+t_0)=f\left[-2 \left( t+t_{0} \right) +1\right] \cdot \sin (t)$')
        self.signal[1].set_color(YELLOW)
        self.system[1].set_color(RED).scale(0.9)

    def graph2(self, dx=0):
        f = FunctionGraph(
            lambda x: np.sin(-2*x+1-2*dx),
            x_min=self.axes2_x_min,
            x_max=self.axes2_x_max,
            color=RED
        ).move_to(self.axes2.c2p(0, 0))
        return f

    def graph3(self, dx=0):
        f = FunctionGraph(
            lambda x: np.sin(-2*x+1+dx),
            x_min=self.axes2_x_min,
            x_max=self.axes2_x_max,
            color=BLUE
        ).move_to(self.axes1.c2p(0, 0))
        return f


class Capacitance(Scene):  
    # ctex=false
    def construct(self):
        set_gpus([0, 1])

        resistor = TextMobject(r"""
         \begin{circuitikz}[european]
         \draw (0,0) to[R] ++(3,0);
         \end{circuitikz} \\ Resistor
        """,
                               stroke_width=1,
                               fill_opacity=1,
                               stroke_opacity=1)

        capac = TextMobject(r"""
         \begin{circuitikz}[american]
         \draw (0,0) to[C] ++(3,0);
         \end{circuitikz} 
        """,
        stroke_width=1,
        fill_opacity=1,
        stroke_opacity=1)
        capac_text = TextMobject('Capacitor').next_to(capac, DOWN, buff=0.3)
        capacitor = VGroup(capac, capac_text)

        indu = TextMobject(r"""
         \begin{circuitikz}[american]
         \draw (0,0) to[L] ++(3,0);
         \end{circuitikz}
        """,
                           stroke_width=1,
                           fill_opacity=0,
                           stroke_opacity=1)
        inductor_text = TextMobject('Inductor').next_to(indu, DOWN, buff=0.3)
        inductor = VGroup(indu, inductor_text)

        group = VGroup(capacitor, resistor, inductor).arrange(DOWN, buff=0.7)

        self.play(ShowCreation(group), run_time=6)
        self.wait()

        circuit = TextMobject(r"""
        \begin{circuitikz}[american]
            \draw (0,0) to[isource, l=$I$] (4,0);
            \draw (0,0) to (0,2) to[C=$C$, f>_=$i$] ++(4,0) to ++(0,-2);
        \end{circuitikz}
        """,
                              stroke_width=1,
                              fill_opacity=0,
                              stroke_opacity=1
                              ).move_to(LEFT*3)
        ut = TexMobject(r'u(t)=\frac{1}{C} \int_{-\infty}^{t} i(\tau) \mathrm{d} \tau')\
            .move_to(RIGHT*3)

        self.play(
            capac.move_to, LEFT*3+UP*1.12,
            capac.set_opacity, 0,
            FadeOut(resistor),
            FadeOut(inductor),
            FadeOut(capac_text),
            Write(ut),
            Write(circuit)
        )
        self.wait()
        self.play(
            circuit.shift, UP*3,
            circuit.scale, 0.3,
            ut.move_to, UP*3+RIGHT*0.6,
            ut.scale, 0.8
        )

        fourmual = [TexMobject(i) for i in [r'i(t) \rightarrow u(t)=\frac{1}{C} \int_{-\infty}^{t} i(\tau) \mathrm{d} \tau',
                                            r'u\left(t-t_{0}\right)=\frac{1}{C} \int_{-\infty}^{t-t_{0}} i(\tau) \mathrm{d} \tau',
                                            r'i\left(t-t_{0}\right) \rightarrow u_{i}(t)=\frac{1}{C} \int_{-\infty}^{t} i\left(\tau-t_{0}\right) \mathrm{d} \tau',
                                            r'=\frac{1}{C} \int_{-\infty}^{t-t_{0}} i(v) \mathrm{d} v \quad \text{Let } v=\tau-t_0',
                                            r'=u\left(t-t_{0}\right)']]
        fourmuals = VGroup(*fourmual).arrange(DOWN).scale(0.8).shift(DOWN*0.5)
        fourmuals[1].shift(RIGHT*0.3)
        fourmuals[2].shift(LEFT*0.05)
        fourmuals[3].shift(RIGHT*2.5)
        fourmuals[4].shift(RIGHT*0.5)
        for i in fourmuals:
            self.play(Write(i))
            self.wait()


class Summary(Scene):
    def construct(self):
        set_gpus([0, 1])

        title = Title('\LARGE Summary').set_color(GREEN)
        text = [r'\parbox[c][][c]{20em}{Systems that consist of signal $f(\cdot)$ with inverse and scaling are all time-invariant systems.}',
                r'\parbox[c][][c]{20em}{Systems that consist of both signal $f(\cdot)$ and computation like timing $t \text{ or } \cos(t)$, ect. are time-invariant systems as well.}']
        summary = BulletedList(text).shift(DOWN)
        summary.fade_all_but(0, opacity=0.3)

        self.play(Write(title))
        self.wait()
        self.play(
            Write(summary),
            run_time=6
        )
        self.wait()
        self.play(summary.fade_all_but, 1, opacity=0.3)
        self.wait()


class Exercise(Scene):
    def construct(self):
        set_gpus([0, 1])

        title = Title(r'\LARGE Exercises').set_color(GREEN)

        e = [
            r"""
            y(t)=\frac{\mathrm{d} x(t)}{\mathrm{d} t}
            """,
            r"""
            y(t)=\int_{-\infty}^{2 \pi} x(\tau) \mathrm{d} \tau 
            """,
            r"""
            y(t)=\left\{\begin{array}{ll}
            0, & t<0 \\
            x(t)+x(t-2), & t \geqslant 0
            \end{array}\right.
            """,
            r"""
            y(t)=\left\{\begin{array}{ll}
            0, & x(t)<0 \\
            x(t)+x(t-2), & x(t) \geqslant 0
            \end{array}\right.
            """,
        ]

        eg = VGroup(
            *[TexMobject(i) for i in e]
        ).arrange(DOWN)\
            .scale(0.9).shift(DOWN*0.5)
        left = eg.get_left()
        for i in eg:
            i.align_to(left, LEFT)

        self.play(Write(title))
        self.wait()
        self.play(Write(eg))
        self.wait()
