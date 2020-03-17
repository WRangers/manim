from manimlib.imports import *
from thD7.video_scenes import *

class SS_1_Epilogue(Epilogue):
    CONFIG = {
        'bgm': [
            r'Arryo Seco~-~Curtis Schweitzer\\',
        ],
        'acknowledgement': None,
    }

class Words(Scene):
    def construct(self):
        set_gpus([0,1])

        words=[
            '信号与系统',
            '是众多工科的基础课程',
            '其地位其实不亚于高数、概统和线代',
            '在最初没有学这门课的时候',
            '我是有一点点害怕的',
            '但事实上其实并没有想象的那么难',
            '但由于教材、老师等原因',
            '很多内容的实质被掩盖在公式和计算之下',
            '这也是我创作这个系列的原因',
            '系列内容是基于我之前的笔记和个人的理解',
            '当然了,还参考了很多优秀的资源',
            '仅仅希望对观者有所帮助',
            '这些视频是用Manim制作的',
            '在此要特别感谢3b1b大神的开源库!',
            '另外,与3b1b不同的是',
            '这不是科普视频',
            '我觉得还是挺硬核的',
            '不过我觉得',
            '与其说Grant Sanderson是数学的科普者',
            '他更像是数学的布道者!'
        ]

        words_g=VGroup(*[TextMobject(i) for i in words])

        self.play(Write(words_g[0]))
        for i,k in enumerate(words_g):
            if i == 0:
                continue
            self.wait(2)
            self.play(FadeOut(words_g[i-1]),Write(k))


class Series(Scene):
    def construct(self):
        set_gpus([0,1])

        title=Title('\\LARGE Signals and Systems Series')
        self.play(Write(title))

        series_titles=[
            '\\sz{1} Time-Invariant Property of Systems',
            '\\sz{2} Understanding Convolution',
            '\\sz{3} Calculating Convolution',
            '\\sz{4} From Fourier Series to Fourier Transformation',
            '\\sz{5} Periodic Fourier Transformation and Sampling',
            '\\sz{6} Laplace Transformation',
            '\\sz{7} Pole-zero Diagrams and Frequency Response'
        ]
        series=VGroup(
            *[TextMobject('\\# '+i) for i in series_titles]
        ).arrange(DOWN,buff=0.2)\
            .set_y((title.get_bottom()[1]-FRAME_Y_RADIUS)/2)
        left=series.get_left()
        for i in series:
            i.align_to(left,LEFT)

        self.play(LaggedStart(*[FadeIn(i) for i in series]),run_time=7)