from manimlib.imports import *
from Rangers.projects.utils import set_gpus
from Rangers.from_others.fourier_series import FourierOfPiSymbol


class ForFun(Scene):
    def construct(self):
        text = TextMobject(r'\sf Just  making  for\\NOTHING!')

        self.play(
            Write(text),
            run_time=5
        )
        self.wait(2)


class LogoShow(FourierOfPiSymbol, MovingCameraScene):
    CONFIG = {
        "n_vectors": 270,
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


class Preamble(Scene):
    CONFIG = {
        'c_title': '我的第一个视频',
        'e_title': 'My First Video',
        'series': r'\scriptsize The Geometry Meaning of Linear Algebra\\ \# \sz{0}',
        # 'episode': '#',
        'saying': r'数缺形时少直观，形少数时难入微；\\数形结合百般好，割裂分家万事休。',
        'saying_author': '——华罗庚',
        'statement': r'\scriptsize 本视频内容主要根据《线性代数的几何意义》制作'
    }

    def construct(self):
        set_gpus([0, 1])

        # logo

        # video title
        ctext = TextMobject(r'\sf '+self.c_title).scale(1.5)
        etext = TextMobject(self.e_title).scale(1.5)
        text = VGroup(ctext, etext)\
            .arrange_submobjects(DOWN, buff=0.5)\
            .shift(0.5*UP)

        p = Dot(0.5*UP)
        cw = ctext.get_width()
        ew = etext.get_width()
        length = cw/2 if cw > ew else ew/2
        line1 = Line(0.5*UP, np.array([-length, 0.5, 0]))
        line2 = Line(0.5*UP, np.array([length, 0.5, 0]))

        self.play(
            FadeIn(p),
            ShowCreation(line1),
            ShowCreation(line2),
        )

        # series name
        sn = TextMobject(self.series).\
            to_edge(DOWN, buff=1.7)

        self.play(
            Write(sn),
            Write(text)
        )
        self.wait(2)

        mgroup = [FadeOut(i) for i in self.mobjects]

        self.play(*mgroup)

        # saying and statement
        saying_text = TextMobject(self.saying)
        author = TextMobject(self.saying_author)\
            .move_to(saying_text.get_corner(DR)+np.array([0, -0.8, 0]))

        stat = TextMobject(self.statement)\
            .to_edge(UP, buff=0.1)

        self.add(stat)
        self.play(Write(saying_text), run_time=3)
        self.play(Write(author))
        self.wait(7)


class Epilogue(Scene):
    CONFIG = {
        'producer': r'\large ${\sf{7}}^{\sf th}$ \sf Dimension',
        'anim_engine':
        r'{\scriptsize by}\\{\sf Grant Sanderson}\\「3Blue1Brown」',
        'bgm': [
            r'Arryo Seco\\',
        ],
        'cfonts': [
            r'\bf 思源黑体',
            r'思源宋体',
            # r'\sf 方正粗金陵简体\\ \tiny (非商业个人授权)',
        ],
        'efonts': [
            r'Palatino',
            r'\sf Zapfino',
            # r'\sz{\LaTeX{} coding}: \tt OT1-pplj-m',
            # r'\gt{\LaTeX{} coding}: \tt OT1-pgoth-m',
        ],
        'refs': [
            r'',
        ]
    }

    def construct(self):
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

        # references
        refs = TextMobject(r'\huge Bibliography')

        # acknowledgement
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
