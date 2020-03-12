from manimlib.imports import *
from thD7.video_scenes import *

class SS_0_Preamble(Preamble):
    CONFIG={
        'c_title': '序言',
        'e_title': 'Introduction',
        'series': r'\scriptsize Signals and Systems Series\\ \# \sz{0}',        
    }

class SS_1_Epilogue(Epilogue):
    CONFIG = {
        'bgm': [
            r'Arryo Seco~-~Curtis Schweitzer\\',
        ],
        'acknowledgement': None,
    }

class Series(Scene):
    def construct(self):
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