from manimlib.imports import *
from thD7.video_scenes import *


class SS_1_Preamble(Preamble):
    CONFIG = {
        'c_title': '理解卷积',
        'e_title': 'Understanding Convolution',
        'series': r'\scriptsize Signals and Systems Series\\ \# \sz{2}',
    }


class SS_1_Epilogue(Epilogue):
    CONFIG = {
        'bgm': [
            r'Arryo Seco~-~Curtis Schweitzer\\',
        ],
        'acknowledgement': None,
    }

class IntroductionAndDefinition(Scene):
    def construct(self):
        set_gpus([0,1])

        self.intro()
        self.definition()
        self.graph_conv()

    def intro(self):
        self.conv= TextMobject('CONVOLUTION').set_color(BLUE).scale(1.2)
        subjects=[
            'Probability',
            'Signal Process',
            'Image Process',
            'Computer Vision',
            'Computer Graph',
            'Deep Learning',
            r'$\cdots \cdots$'
        ]
        self.sub_g=VGroup(
            *[TextMobject(i) for i in subjects]
        ).arrange(DOWN).shift(RIGHT*3)

        self.play(Write(self.conv))
        self.wait()
        self.play(self.conv.shift,LEFT*3)
        for i in self.sub_g:
            self.wait()
            self.play(Write(i))
        self.wait()
        self.play(Indicate(self.sub_g[-2]))
        self.wait()

    def definition(self):
        title= Title('\LARGE CONVOLUTION').set_color(GREEN)
        self.play(
            FadeOutAndShift(self.sub_g,direction=RIGHT),
            FadeOutAndShift(self.conv,direction=LEFT),
            Write(title)
        )
        self.wait()

        definition=TexMobject(r'f_{1}(t) * f_{2}(t)=\int_{-\infty}^{\infty} f_{1}(\tau) f_{2}(t-\tau) \mathrm{d} \tau')\
            .scale(1.5)
        self.play(Write(definition),run_time=4)
        self.wait()
        self.play(definition.shift,UP*1.5)

    def graph_conv(self):
        axes=Axes(
            
        )


