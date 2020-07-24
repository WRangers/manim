from manimlib.imports import *

# Time control functions


def custom_time(t, partitions, start, end, func):
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


def Custom(partitions, start, end, func=smooth):
    return lambda t: custom_time(t, partitions, start, end, func)

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
        title = VGroup(text, p, line1, line2)

        # group name
        gn = TextMobject(self.group)

        # group members
        gm = TextMobject(r"""
        \begin{table}[h]
            \small
            \centering
            \begin{tabular}{ccc}
            18308183  & 18308190  & 18308193 \\
             王君旭    &  翁海松   &   吴康喜  \\[3mm]
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
            ApplyMethod(title.shift, 1.5*UP, rate_func=Custom(6, 0, 4)),
            Write(gn, rate_func=Custom(6, 2, 5)),
            FadeIn(gm, rate_func=Custom(6, 4, 6)),
            run_time=2
        )
        self.wait(2)

        mgroup = [FadeOut(i) for i in self.mobjects]
        self.play(*mgroup)

# Quote

class Quote(Scene):
    def construct(self):
        set_gpus([0,1])

        quote_text=TextMobject(r"""
            \parbox[c][][c]{20em}{
            Since Newton, mankind has come to realize that the laws of physics are always expressed in the language of differential equations.
            \par \hfill ——Steven Strogatz}
            """).shift(UP*2)
        
        self.play(Write(quote_text),run_time=3)

        self.lorzen()  # add at late period

    def lorzen(self):
        pass


# Introduction to Chua's circuit

class Circuit(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)

    def construct(self):
        set_gpus([0,1])

        cir=ImageMobject('circuit').scale(2)
        G=TexMobject('G').set_color(RED).move_to(np.array([0,2.4,0]))
        L=TexMobject('L').set_color(BLUE).move_to(np.array([-2.3,-0.1,0]))
        R=TexMobject('R').set_color(GREEN).move_to(np.array([4.4,-0.1,0]))
        C1=TexMobject('C_1').set_color(YELLOW).move_to(np.array([2.8,-0.1,0]))
        C2=TexMobject('C_2').set_color(ORANGE).move_to(np.array([-4.5,-0.1,0]))

        circuit=Group(cir,G,L,R,C1,C2)

        self.play(
            FadeIn(circuit)
        )
        self.wait(2)

        self.camera_frame.save_state()
        self.play(
            self.camera_frame.scale,.3,
            self.camera_frame.move_to,np.array([4,-0.1,0])
        )
        self.wait(1)
        self.play(Restore(self.camera_frame))

# Analyzing and solving Chua's circuit equations


# Analysis of stability of solution


# Epilogue

class Epilogue(Scene):
    def construct(self):
        set_gpus([0, 1])

        # Acknowledgement
        ak_title = TextMobject(r'\huge Acknowledgements').to_edge(UP, buff=1)

        ak_text1 = TextMobject(r"""
            \parbox[c][][c]{20em}{
                Special gratitude to Prof.Liang Wang and all the TAs for your instruction and insightful explanation!}
            """).shift(DOWN)
        ak_text2 = TextMobject(r"""
            \parbox[c][][c]{20em}{
                Thanks to Grant Sanderson (3Blue1Brown) who made up the \texttt{manim} with which this video was made.}
            """).shift(UP*0.5)

        manim = TextMobject('Manim')\
            .scale(2.5)\
            .shift(2.5*DOWN)\
            .shift(2.2*RIGHT)

        pic_manim = ImageMobject('manim_graph').scale(
            1.5).move_to(np.array([-1.8, -2, 0]))

        self.play(
            FadeIn(ak_title),
            Write(ak_text1)
        )
        self.wait(4)
        self.play(
            FadeOut(ak_text1)
        )
        self.play(
            Write(ak_text2),
            Write(manim),
            run_time=3
            # Show the logo at the same time
        )
        self.wait(4)
        self.add(pic_manim)

        # Tools
        tool_title = TextMobject(r'\huge Tools').to_edge(UP, buff=1)

        pic_python = ImageMobject('python_logo').shift(LEFT*4).scale(0.6)
        pic_pr = ImageMobject('pr_logo').shift(RIGHT*4)

        tool_python = TextMobject('Python').shift(LEFT*4).shift(2*DOWN)
        tool_pr = TextMobject('Premiere').shift(RIGHT*4).shift(2*DOWN)

        python = Group(pic_python, tool_python)
        pr = Group(pic_pr, tool_pr)

        self.play(
            FadeOut(ak_title),
            FadeOut(ak_text2),
            FadeIn(tool_title),
            manim.scale, 0.4,
            manim.move_to, np.array([0, -2, 0]),
            FadeIn(python),
            FadeIn(pr),
            pic_manim.move_to, np.array([0.2, 0, 0])
        )
        self.wait(2)

        tools = Group(
            tool_title, python, pr, manim, pic_manim
        )

        # Background Music
        bgm_title = TextMobject(r'\huge Background Music').to_edge(UP, buff=1)
        bgm_text = TextMobject(
            'Reflections - Vincent Rubinetti').shift(DOWN*0.5)

        self.play(
            *[FadeOut(i) for i in tools],
            FadeIn(bgm_title),
            Write(bgm_text)
        )
        self.wait(1)
        self.play(Indicate(bgm_text[0][0:11]))
        self.wait(1)

        bgm = Group(bgm_title, bgm_text)

        # Last Frame
        tyfw = TextMobject(r'\sf Thank you for watching!').scale(1.2)
        cr = TextMobject('2020 © 甜甜的数值计算').scale(0.5).shift(DOWN*2)

        self.play(
            FadeOut(bgm),
            Write(tyfw),
            FadeIn(cr),
            run_time=2
        )

# Logo Animation


NEW_BLUE = "#68a8e1"


class Thumbnail(GraphScene):
    CONFIG = {
        "y_max": 8,
        "y_axis_height": 5,
    }

    def construct(self):
        self.show_function_graph()

    def show_function_graph(self):
        self.setup_axes(animate=False)

        def func(x):
            return 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5

        def rect(x):
            return 2.775*(x-1.5)+3.862
        recta = self.get_graph(rect, x_min=-1, x_max=5)
        graph = self.get_graph(func, x_min=0.2, x_max=9)
        graph.set_color(NEW_BLUE)
        input_tracker_p1 = ValueTracker(1.5)
        input_tracker_p2 = ValueTracker(3.5)

        def get_x_value(input_tracker):
            return input_tracker.get_value()

        def get_y_value(input_tracker):
            return graph.underlying_function(get_x_value(input_tracker))

        def get_x_point(input_tracker):
            return self.coords_to_point(get_x_value(input_tracker), 0)

        def get_y_point(input_tracker):
            return self.coords_to_point(0, get_y_value(input_tracker))

        def get_graph_point(input_tracker):
            return self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker))

        def get_v_line(input_tracker):
            return DashedLine(get_x_point(input_tracker), get_graph_point(input_tracker), stroke_width=2)

        def get_h_line(input_tracker):
            return DashedLine(get_graph_point(input_tracker), get_y_point(input_tracker), stroke_width=2)
        #
        input_triangle_p1 = RegularPolygon(n=3, start_angle=TAU / 4)
        output_triangle_p1 = RegularPolygon(n=3, start_angle=0)
        for triangle in input_triangle_p1, output_triangle_p1:
            triangle.set_fill(WHITE, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        #
        input_triangle_p2 = RegularPolygon(n=3, start_angle=TAU / 4)
        output_triangle_p2 = RegularPolygon(n=3, start_angle=0)
        for triangle in input_triangle_p2, output_triangle_p2:
            triangle.set_fill(WHITE, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)

        #
        x_label_p1 = TexMobject("a")
        output_label_p1 = TexMobject("f(a)")
        x_label_p2 = TexMobject("b")
        output_label_p2 = TexMobject("f(b)")
        v_line_p1 = get_v_line(input_tracker_p1)
        v_line_p2 = get_v_line(input_tracker_p2)
        h_line_p1 = get_h_line(input_tracker_p1)
        h_line_p2 = get_h_line(input_tracker_p2)
        graph_dot_p1 = Dot(color=WHITE)
        graph_dot_p2 = Dot(color=WHITE)

        # reposition mobjects
        x_label_p1.next_to(v_line_p1, DOWN)
        x_label_p2.next_to(v_line_p2, DOWN)
        output_label_p1.next_to(h_line_p1, LEFT)
        output_label_p2.next_to(h_line_p2, LEFT)
        input_triangle_p1.next_to(v_line_p1, DOWN, buff=0)
        input_triangle_p2.next_to(v_line_p2, DOWN, buff=0)
        output_triangle_p1.next_to(h_line_p1, LEFT, buff=0)
        output_triangle_p2.next_to(h_line_p2, LEFT, buff=0)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1))
        graph_dot_p2.move_to(get_graph_point(input_tracker_p2))

        #
        self.play(
            ShowCreation(graph),
        )
        # Animacion del punto a
        self.add_foreground_mobject(graph_dot_p1)
        self.add_foreground_mobject(graph_dot_p2)
        self.play(
            DrawBorderThenFill(input_triangle_p1),
            Write(x_label_p1),
            ShowCreation(v_line_p1),
            GrowFromCenter(graph_dot_p1),
            ShowCreation(h_line_p1),
            Write(output_label_p1),
            DrawBorderThenFill(output_triangle_p1),
            DrawBorderThenFill(input_triangle_p2),
            Write(x_label_p2),
            ShowCreation(v_line_p2),
            GrowFromCenter(graph_dot_p2),
            ShowCreation(h_line_p2),
            Write(output_label_p2),
            DrawBorderThenFill(output_triangle_p2),
            run_time=0.5
        )
        self.add(
            input_triangle_p2,
            x_label_p2,
            graph_dot_p2,
            v_line_p2,
            h_line_p2,
            output_triangle_p2,
            output_label_p2,
        )
        ###################
        pendiente_recta = self.get_secant_slope_group(
            1.9, recta, dx=1.4,
            df_label=None,
            dx_label=None,
            dx_line_color=PURPLE,
            df_line_color=ORANGE,
        )
        grupo_secante = self.get_secant_slope_group(
            1.5, graph, dx=2,
            df_label=None,
            dx_label=None,
            dx_line_color="#942357",
            df_line_color="#3f7d5c",
            secant_line_color=RED,
        )

        self.add(
            input_triangle_p2,
            graph_dot_p2,
            v_line_p2,
            h_line_p2,
            output_triangle_p2,
        )
        self.play(FadeIn(grupo_secante))

        kwargs = {
            "x_min": 4,
            "x_max": 9,
            "fill_opacity": 0.75,
            "stroke_width": 0.25,
        }
        self.graph = graph
        iteraciones = 6

        self.rect_list = self.get_riemann_rectangles_list(
            graph, iteraciones, start_color=PURPLE, end_color=ORANGE, **kwargs
        )
        flat_rects = self.get_riemann_rectangles(
            self.get_graph(lambda x: 0), dx=0.5, start_color=invert_color(PURPLE), end_color=invert_color(ORANGE), **kwargs
        )
        rects = self.rect_list[0]
        self.transform_between_riemann_rects(
            flat_rects, rects,
            replace_mobject_with_target_in_scene=True,
            run_time=0.9
        )

        # adding manim
        picture = Group(*self.mobjects)
        picture.scale(0.6).to_edge(LEFT, buff=SMALL_BUFF)
        manim = TextMobject("Manim").set_height(1.5) \
                                    .next_to(picture, RIGHT) \
                                    .shift(DOWN * 0.7)
        self.add(manim)
