from manimlib.imports import *
from thD7.video_scenes import *


class SS_1_Preamble(Preamble):
    CONFIG = {
        'c_title': '系统时变性质的判断',
        'e_title': 'Time-Invariant Property of Systems',
        'series': r'\scriptsize Signals and Systems Series\\ \# \sz{1}',
        'saying': None,
    }


class SS_1_Epilogue(Epilogue):
    CONFIG = {
        'bgm': [
            r'Arryo Seco~-~Curtis Schweitzer\\',
        ],
        'refs': [
            r'',
        ],
        'acknowledgement': False,
    }


class Introduction(Scene):
    def construct(self):
        set_gpus([0, 1])

        que = TextMobject(r'How do you judge whether a \\ system is time-invirant or not?')\
            .scale(1.5).set_color(YELLOW)
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
        wh=TextMobject('?')\
            .scale(1.5)\
                .set_x(eq.get_x())\
                    .next_to(eq,UP,buff=0.1)\
                        .set_color(YELLOW)

        self.play(Write(sys))
        self.wait()
        self.play(
            sys.shift, UP*0.5,
            Write(f)
        )
        self.wait()

        sys2 = sys.copy()[0][0:7]
        f2=f.copy()[0][8:13]
        self.play(
            sys2.move_to, eq.get_center()+LEFT*2,
            sys2.scale, 1.5,
            f2.move_to, eq.get_center()+RIGHT*1.4,
            f2.scale, 1.5,
            Write(eq),
            Write(wh)
        )
        self.wait()
        
        neq=Line(eq.get_corner(UR)+0.1*UP,eq.get_corner(DL)+0.1*DOWN)\
            .set_color(RED)
        self.play(Transform(wh,neq))

        self.wait()
        self.play(
            *[FadeOut(i) for i in self.mobjects]
        )

        ans=TextMobject(r'$y(t)$ is a time-variant system.').scale(1.5).set_color(YELLOW)
        self.play(Write(ans))
        self.wait(4)

        but=TextMobject(r'BUT!').scale(3).set_color(YELLOW)
        self.play(Transform(ans,but))

        why=TextMobject(r'WHY?').scale(3).set_color(YELLOW)\
            .shift(UP*1)
        fourmalls=Group(sys,f).shift(DOWN)

        self.wait()
        self.play(
            Transform(ans,why),
            FadeIn(fourmalls)
        )
        self.play(
            FadeToColor(sys[0][8:18],RED),
            FadeToColor(f[0][14:22],RED),
        )
        self.wait()
        self.play(Flash(f[0][18]))
        self.wait()

        text=TextMobject('That is what we are going to talk about.')\
            .set_color(YELLOW).scale(1.5)
        self.play(
            *[FadeOut(i) for i in self.mobjects],
            Write(text)
        )
        self.wait()

class Defination(Scene):
    def construct(self):
        title=Title(r'\LARGE Time Invariant')
        defin=TextMobject(r"""
            \parbox[c][][c]{20em}{
                If a system is initially in its zero state and an arbitrary input signal $f(t)$ causes
                a response $y(t)$ and an input signal $f(t-t_0)$ causes a response $y(t-t_0)$ for any
                arbitrary $t_0$, the system is said to be \emph{time invariant}.
            }
        """).shift(0.5*DOWN)

        self.play(
            ShowCreation(title)
        )
        self.wait()
        self.play(
            Write(defin),
            run_time=7
        )
        self.wait()
        


