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


class Defination(Scene):

    def construct(self):
        set_gpus([0, 1])

        self.title = Title(r'\LARGE Time Invariant').set_color(GREEN)

        self.defination()
        self.system()
        self.graph()

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
        self.play(FadeOutAndShiftDown(defin))

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
            ).align_to(axes1.c2p(0.0), DL)

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
