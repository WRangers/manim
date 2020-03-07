from manimlib.imports import *
from thD7.video_scenes import *

class CycloidPreamble(Preamble):
    CONFIG = {
        'c_title': '摆线',
        'e_title': 'Diving into Cycloids',
    }

class CycloidEpilogue(Epilogue):
    CONFIG={
        'bgm': [
            r'Arryo Seco~-~Curtis Schweitzer\\',
        ],
    }

class Cycloid(Scene):
    def construct(self):
        set_gpus([0,1])

        radius = 1.2

        c1,c2,dot=self.epy(radius,1)

    def epy(self,r1,k):
        r2=r1/k
        # Manim circle
        c1 = Circle(radius=r1,color=RED)
        # Small circle
        c2 = Circle(radius=r2,color=BLUE).rotate(PI)
        c2.next_to(c1,RIGHT,buff=0)
        c2.start = c2.copy()
        # Dot
        dot = Dot(c2.points[0],color=YELLOW)
        # Line
        line = Line(c2.get_center(),dot.get_center()).set_stroke(BLACK,2.5)
        # Path
        path = VMobject(color=RED)
        path.set_points_as_corners([dot.get_center(),dot.get_center()+UP*0.001])
        # Path group
        path_group = VGroup(line,dot,path)
        
        self.play(ShowCreation(line),ShowCreation(c1),ShowCreation(c2),GrowFromCenter(dot))

        # update function of path_group
        def update_group(group):
            l,mob,previus_path = group
            mob.move_to(c2.points[0])
            old_path = path.copy()
            old_path.append_vectorized_mobject(Line(old_path.points[-1],dot.get_center()))
            old_path.make_smooth()
            l.put_start_and_end_on(c2.get_center(),dot.get_center())
            path.become(old_path)

        # update function of small circle
        def update_c2(c,alpha):
            c.become(c.start)
            c.rotate(TAU*alpha,about_point=c1.get_center())
            c.rotate(TAU*(r1/r2)*alpha,about_point=c.get_center())

        path_group.add_updater(update_group)
        self.add(path_group)
        
        self.play(
                UpdateFromAlphaFunc(c2,update_c2,rate_func=linear,run_time=6)
                )
        self.play(FadeOut(VGroup(c1,c2,dot)))
        self.wait()

        return c1,c2,dot

    def ratio(self,c1,c2,dot):
        arrow1=Arrow(c1.get_center,c1.point[0])
        arrow2=Arrow(c2.get_center,c2.point[0])
        


class Epicycloid(Cardioid):
    def construct(self):
        set_gpus([0,1])

        epi_text=TextMobject(r'\huge More')

        radius = 1

        self.play(Write(epi_text))
        self.wait()
        self.play(FadeOut(epi_text))

        self.epy1(radius,2)