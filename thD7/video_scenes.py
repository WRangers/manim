from manimlib.imports import *
from thD7.from_others.fourier_series import FourierOfPiSymbol

'''
    Scenes for the series of signals and systems.
'''

class Preamble(Scene):
    CONFIG = {
        'c_title': '',
        'e_title': '',
        'series': None,
    }

    def construct(self):
        set_gpus([0, 1])

        # video title
        ctext = TextMobject(r'\sf '+self.c_title).scale(1.5)
        etext = TextMobject(self.e_title).scale(1.5)
        text = VGroup(ctext, etext)\
            .arrange_submobjects(DOWN, buff=0.5)

        p = Dot()
        cw = ctext.get_width()
        ew = etext.get_width()
        length = cw/2 if cw > ew else ew/2
        line1 = Line(ORIGIN, np.array([-length, 0, 0]))
        line2 = Line(ORIGIN, np.array([length, 0, 0]))

        # series name
        if self.series:
            text.shift(0.5*UP)
            p.shift(0.5*UP)
            line1.shift(0.5*UP)
            line2.shift(0.5*UP)

            sn = TextMobject(self.series).\
                to_edge(DOWN, buff=1.7)

        self.play(
            FadeIn(p),
            ShowCreation(line1),
            ShowCreation(line2),
        )
        if self.series:
            self.play(
                Write(sn),
                Write(text)
            )
        else:
            self.play(Write(text))
        self.wait(2)

        mgroup = [FadeOut(i) for i in self.mobjects]

        self.play(*mgroup)


class QuoteScene(Scene):
    CONFIG = {
        'quotation': None,
        'author': None,
        'statement': None,
    }

    def construct(self):
        quote_text = TextMobject(self.quotation)
        author_text = TextMobject(self.author)\
            .move_to(quote_text.get_corner(DR)+np.array([0, -0.8, 0]))

        statement_text = TextMobject(self.statement)\
            .to_edge(UP, buff=0.1)

        self.add(statement_text)
        self.play(Write(quote_text), run_time=3)
        self.play(Write(author_text),run_time=2)
        self.wait(5)


class Epilogue(Scene):
    CONFIG = {
        'producer': r'\large ${\sf{7}}^{\sf th}$ \sf Dimension',
        'anim_engine':
        r'{\scriptsize by}\\{\sf Grant Sanderson}\\「3Blue1Brown」',
        'bgm': None,
        'cfonts': [
            r'\bf 思源黑体',
            r'思源宋体',
        ],
        'efonts': [
            r'Palatino',
            r'\sf Zapfino',
        ],
        'acknowledgement': False,
    }

    def construct(self):
        set_gpus([0, 1])

        # producer
        prod = TextMobject(r'\huge Producer')\
            .to_edge(UP, buff=2)
        producer_text = TextMobject(r''+self.producer)\
            .next_to(prod, DOWN, buff=1)

        self.play(
            Write(prod),
            FadeIn(producer_text)
        )
        self.wait()
        self.play(
            FadeOut(prod),
            FadeOut(producer_text)
        )
        self.wait(0.1)

        # anmimation engine
        anima = TextMobject(r'\huge Anmimation Engine')\
            .to_edge(UP, buff=2)
        logo = ImageMobject('manim').scale(1.5)
        a_e = TextMobject(self.anim_engine)
        a_e[0][-2:-7:-1].set_color('#8d6135')
        a_e[0][-8:-12:-1].set_color('#74c1e4')
        a_e_group = Group(logo, a_e)\
            .arrange(DOWN, buff=-0.6)\
            .to_edge(DOWN, buff=1)

        self.play(
            FadeIn(a_e_group),
            Write(anima),
        )
        self.wait()
        self.play(
            FadeOut(a_e_group),
            FadeOut(anima)
        )
        self.wait(0.1)

        # background music
        bgm_text = TextMobject(r'\huge Background Music')\
            .to_edge(UP, buff=2)
        bgms = TextMobject(*self.bgm)\
            .to_edge(DOWN, buff=3)

        self.play(
            Write(bgm_text),
            FadeIn(bgms)
        )
        self.wait()
        self.play(
            FadeOut(bgm_text),
            FadeOut(bgms)
        )
        self.wait(0.1)

        # fonts
        fonts = TextMobject(r'\huge Fonts')\
            .to_edge(UP, buff=2)
        cfont_text = Group(*[TextMobject(i)
                             for i in self.cfonts]
                           ).arrange(DOWN)
        efont_text = Group(*[TextMobject(i)
                             for i in self.efonts]
                           ).arrange(DOWN)
        font_text = Group(cfont_text, efont_text)\
            .arrange(DOWN)\
            .to_edge(DOWN, buff=1)

        self.play(
            Write(fonts),
            FadeIn(font_text),
        )
        self.wait()
        self.play(
            FadeOut(fonts),
            FadeOut(font_text)
        )
        self.wait(0.1)

        # acknowledgement
        if self.acknowledgement:
            ack = TextMobject(r'\huge Acknowledgement')\
                .to_edge(UP, buff=2)
            ack_text = TextMobject(
                r"Particularly acknowledging Prof.Guangqian Ren's\\" +
                r'authorization and supporting.\\ \vspace{0.7em}' +
                r'特别鸣谢任广千教授对此系列视频的授权与支持。'
            ).next_to(ack, DOWN, buff=1)

            self.play(Write(ack))
            self.play(Write(ack_text), run_time=5)
            self.wait(2)
            self.play(
                FadeOut(ack),
                FadeOut(ack_text)
            )
            self.wait(0.1)

        # nothing
        jtext = TextMobject(r'\sf Just  making  for\\NOTHING!')

        self.play(
            Write(jtext),
            run_time=5
        )
        self.wait(2)


class ForFun(Scene):
    def construct(self):
        text = TextMobject(r'\sf Just  making  for\\NOTHING!')

        self.play(
            Write(text),
            run_time=5
        )
        self.wait(2)

# this class is based on https://github.com/3b1b/manim/blob
# /master/from_3b1b/active/diffyq/part2/fourier_series.py
# class FourierOfPiSymbol


class Show7thD(FourierOfPiSymbol, MovingCameraScene):
    CONFIG = {
        "n_vectors": 300,
        "name_color": WHITE,
        "animated_name": r"\sf 7",
        "time_per_symbol": 5,
        "slow_factor": 1 / 5,
        "parametric_function_step_size": 0.01,
        "logo": r'\large ${\sf{7}}^{\sf th}$ \sf D',
    }

    def construct(self):
        set_gpus([0, 1])

        sthd = TextMobject(self.logo).scale(3)

        name = TextMobject(self.animated_name)
        max_width = FRAME_WIDTH - 2
        max_height = FRAME_HEIGHT - 2
        name.set_width(max_width)
        if name.get_height() > max_height:
            name.set_height(max_height)

        frame = self.camera.frame
        frame.save_state()

        vectors = VGroup(VectorizedPoint())
        circles = VGroup(VectorizedPoint())
        for path in name.family_members_with_points():
            for subpath in path.get_subpaths():
                sp_mob = VMobject()
                sp_mob.set_points(subpath)
                coefs = self.get_coefficients_of_path(sp_mob)
                new_vectors = self.get_rotating_vectors(
                    coefficients=coefs
                )
                new_circles = self.get_circles(new_vectors)
                self.set_decreasing_stroke_widths(new_circles)

                drawn_path = self.get_drawn_path(new_vectors)
                drawn_path.clear_updaters()
                drawn_path.set_stroke(self.name_color, 3)

                static_vectors = VMobject().become(new_vectors)
                static_circles = VMobject().become(new_circles)
                # static_circles = new_circles.deepcopy()
                # static_vectors.clear_updaters()
                # static_circles.clear_updaters()

                self.play(
                    Transform(vectors, static_vectors, remover=True),
                    Transform(circles, static_circles, remover=True),
                    frame.set_height, 1.5 * name.get_height(),
                    frame.move_to, path,
                )

                self.add(new_vectors, new_circles)
                self.vector_clock.set_value(0)
                self.play(
                    ShowCreation(drawn_path),
                    rate_func=linear,
                    run_time=self.time_per_symbol
                )
                self.remove(new_vectors, new_circles)
                self.add(static_vectors, static_circles)

                vectors = static_vectors
                circles = static_circles
        self.play(
            FadeOut(vectors),
            FadeOut(circles),
            run_time=2
        )
        self.wait(0.2)

        drawn_path.generate_target()
        drawn_path.target.set_width(sthd[0][0].get_width())
        drawn_path.target.move_to(sthd.get_corner(DL), aligned_edge=DL)
        drawn_path.target.fade(1)

        self.play(LaggedStart(
            *[MoveToTarget(drawn_path), Write(sthd)],
            lag_ratio=0.5),
            run_time=2,
        )
        self.wait(3)
