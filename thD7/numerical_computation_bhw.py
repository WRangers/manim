from manimlib.imports import *

# Time control functions

def custom_time(t,partitions,start,end,func):
    duration = end - start
    fragment_time = 1 / partitions
    start_time = start * fragment_time
    end_time = end * fragment_time
    duration_time = duration * fragment_time
    def fix_time(x):
        return (x - start_time) / duration_time
    if t < start_time: 
        return func(fix_time(start_time))
    elif start_time <= t and t < end_time:
        return func(fix_time(t))
    else:
        return func(fix_time(end_time))

def Custom(partitions,start,end,func=smooth):
    return lambda t: custom_time(t,partitions,start,end,func)

# Preamble

class Preamble(Scene):
    CONFIG = {
        'c_title': '数值计算方法·期末大作业',
        'e_title': 'Numerical Computation Methods ·\ Final Project',
        'group': '\small 甜甜的数值计算' 
    }

    def construct(self):
        set_gpus([0, 1])

        # video title
        ctext = TextMobject(r'\sf '+self.c_title).scale(1.2)
        etext = TextMobject(self.e_title).scale(1.2)
        text = VGroup(ctext, etext)\
            .arrange_submobjects(DOWN, buff=0.5)

        p = Dot()
        cw = ctext.get_width()
        ew = etext.get_width()
        length = cw/2 if cw > ew else ew/2
        line1 = Line(ORIGIN, np.array([-length, 0, 0]))
        line2 = Line(ORIGIN, np.array([length, 0, 0]))
        title=VGroup(text,p,line1,line2)

        # group name
        gn = TextMobject(self.group)

        # group members
        gm = TextMobject(r"""
        \begin{table}[h]
            \small
            \centering
            \begin{tabular}{ccc}
            18308183  & 18308190  & 18308193 \\
             王君旭    &  翁海松   &   吴康喜  \\
        \\
            18308204  & 18308209  & 18308215  \\
             谢卓辰    &  徐仕炀   &   严雨新   \\
        \\
        \end{tabular}
        \end{table}
        """).shift(DOWN*2)

        self.play(
            FadeIn(p),
            ShowCreation(line1),
            ShowCreation(line2),
            Write(text),
            run_time=2
        )
        self.wait()
        self.play(
            ApplyMethod(title.shift,1.5*UP,rate_func=Custom(6,0,4)),
            Write(gn,rate_func=Custom(6,2,5)),
            FadeIn(gm,rate_func=Custom(6,4,6)),
            run_time=2
        )
        self.wait(2)

        mgroup = [FadeOut(i) for i in self.mobjects]
        self.play(*mgroup)