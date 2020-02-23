from manimlib.imports import *
import os

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

##################### Tutorial ###################

class Shapes(Scene):
    #A few simple shapes
    def construct(self):
        circle = Circle()
        square = Square()
        line=Line(np.array([3,0,0]),np.array([5,0,0]))
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

        self.add(line)
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square,triangle))

class MoreShapes(Scene):
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse=Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)
        # ring.move_to(UP)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square),FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))

class AddingText(Scene):
    #Adding text on the screen
    def construct(self):
        my_first_text=TextMobject("Writing with manim is fun")
        second_line=TextMobject("and easy to do!")
        second_line.next_to(my_first_text,DOWN)
        third_line=TextMobject("for me and you!")
        third_line.next_to(my_first_text,DOWN)

        self.add(my_first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line,third_line))
        self.wait(2)
        second_line.shift(3*DOWN)
        self.play(ApplyMethod(my_first_text.shift,3*UP))
        self.play(ApplyMethod(my_first_text.move_to,DOWN*4))

class AddingMoreText(Scene):
    #Playing around with text properties
    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject("A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)
        author=TextMobject("-Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN+RIGHT),DOWN)

        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote,quote2),
          ApplyMethod(author.move_to,quote2.get_corner(DOWN+RIGHT)+DOWN+2*LEFT))
        
        self.play(ApplyMethod(author.scale,1.5))
        author.match_color(quote2)
        self.play(FadeOut(quote))

class RotateAndHighlight(Scene):
    #Rotation of text and highlighting with surrounding geometries
    def construct(self):
        square=Square(side_length=5,fill_color=YELLOW, fill_opacity=1)
        label=TextMobject("Text at an angle")
        label.bg=BackgroundRectangle(label,fill_opacity=1)
        label_group=VGroup(label.bg,label)  #Order matters
        label_group.rotate(TAU/8)
        label.bg.rotate(-TAU/8)
        label2=TextMobject("Boxed text",color=BLACK)
        label2.bg=SurroundingRectangle(label2,color=BLUE,fill_color=RED, fill_opacity=.5)
        label2_group=VGroup(label2,label2.bg)
        label2_group.next_to(label_group,DOWN)
        label3=TextMobject("Rainbow")
        label3.scale(2)
        label3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        label3.to_edge(DOWN)
        # lable4=TextMobject("你好")

        self.add(square)
        self.play(FadeIn(label_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))
        # self.play(FadeIn(label4))

class BasicEquations(Scene):
    #A short script showing how to use Latex commands
    def construct(self):
        eq1=TextMobject("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
        eq1_1=TextMobject(r"$\vec{X}_0 \cdot \vec{Y}_1 = 3$")
        eq1.shift(2*UP)
        eq2=TexMobject(r"\vec{F}_{net} = \sum_i \vec{F}_i")
        eq2.shift(2*DOWN)

        self.play(Write(eq1))
        self.play(Write(eq2))
        self.play(Write(eq1_1))

class ColoringEquations(Scene):
    #Grouping and coloring parts of equations
    def construct(self):
        line1=TexMobject(r"\text{The vector } \vec{F}_{net} \text{ is the net }",r"\text{force }",r"\text{on object of mass }")
        line1.set_color_by_tex("force", BLUE)
        line1.set_color_by_tex("F", RED)
        line2=TexMobject("m", "\\text{ and acceleration }", "\\vec{a}", ".  ")
        line2.set_color_by_tex_to_color_map({
            "m": YELLOW,
            "{a}": RED
        })
        line3=TexMobject("\color{red}WANG")
        line3.move_to(UP*3)

        sentence=VGroup(line1,line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(sentence))
        self.play(Write(line3))

class UsingBraces(Scene):
    #Using braces to group text together
    def construct(self):
        eq1A = TextMobject("4x + 3y")
        eq1B = TextMobject("=")
        eq1C = TextMobject("0")
        eq2A = TextMobject("5x -2y")
        eq2B = TextMobject("=")
        eq2C = TextMobject("3")
        eq1B.next_to(eq1A,RIGHT)
        eq1C.next_to(eq1B,RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A,LEFT)
        eq2B.align_to(eq1B,LEFT)
        eq2C.align_to(eq1C,LEFT)

        eq_group=VGroup(eq1A,eq2A)
        braces=Brace(eq_group,LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces),Write(eq_text))

class UsingBracesConcise(Scene):
    #A more concise block of code with all columns aligned
    def construct(self):
        eq1_text=["4","x","+","3","y","=","0"]
        eq2_text=["5","x","-","2","y","=","3"]
        eq1_mob=TexMobject(*eq1_text)
        eq2_mob=TexMobject(*eq2_text)
        eq1_mob.set_color_by_tex_to_color_map({
            "x":RED_B,
            "y":GREEN_C
            })
        eq2_mob.set_color_by_tex_to_color_map({
            "x":RED_B,
            "y":GREEN_C
            })
        for i,item in enumerate(eq2_mob):
            item.align_to(eq1_mob[i],LEFT)
        eq1=VGroup(*eq1_mob)
        eq2=VGroup(*eq2_mob)
        eq2.shift(DOWN)
        eq_group=VGroup(eq1,eq2)
        braces=Brace(eq_group,LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.play(Write(eq1),Write(eq2))
        self.play(GrowFromCenter(braces),Write(eq_text))

class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2),
    }   
    def construct(self):
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        func_graph2=self.get_graph(self.func_to_graph2)
        vert_line = self.get_vertical_line_to_graph(TAU,func_graph,color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label = "\\cos(x)")
        graph_lab2=self.get_graph_label(func_graph2,label = "\\sin(x)", x_val=-10, direction=UP/2)
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU,func_graph)
        two_pi.next_to(label_coord,RIGHT+UP)

        self.play(ShowCreation(func_graph),ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2),ShowCreation(two_pi))

    def func_to_graph(self,x):
        return np.cos(x)

    def func_to_graph2(self,x):
        return np.sin(x)

class ExampleApproximation(GraphScene):
    CONFIG = {
        "function" : lambda x : np.cos(x), 
        "function_color" : BLUE,
        "taylor" : [lambda x: 1, lambda x: 1-x**2/2, lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4), lambda x: 1-x**2/2+x**4/math.factorial(4)-x**6/math.factorial(6),
        lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8), lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8) - x**10/math.factorial(10)],
        "center_point" : 0,
        "approximation_color" : GREEN,
        "x_min" : -10,
        "x_max" : 10,
        "y_min" : -1,
        "y_max" : 1,
        "graph_origin" : ORIGIN ,
        "x_labeled_nums" :range(-10,12,2),

    }
    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(
            self.function,
            self.function_color,
        )
        approx_graphs = [
            self.get_graph(
                f,
                self.approximation_color
            )
            for f in self.taylor
        ]

        term_num = [
            TexMobject("n = " + str(n),aligned_edge=DOWN)
            for n in range(0,8)]
        #[t.to_edge(BOTTOM,buff=SMALL_BUFF) for t in term_num]


        #term = TexMobject("")
        #term.to_edge(BOTTOM,buff=SMALL_BUFF)
        term = VectorizedPoint(DOWN)

        approx_graph = VectorizedPoint(
            self.input_to_graph_point(self.center_point, func_graph)
        )

        self.play(
            ShowCreation(func_graph),
        )
        for n,graph in enumerate(approx_graphs):
            self.play(
                Transform(approx_graph, graph, run_time = 2),
                Transform(term,term_num[n])
            )
            self.wait()

class DrawAnAxis(Scene):
    CONFIG = { "plane_kwargs" : { 
        "x_line_frequency" : 2,
        "y_line_frequency" :2
        }
    }

    def construct(self):
        my_plane = NumberPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels())
        circle = Circle()

        self.add(my_plane)
        self.play(FadeIn(circle))
        self.play(FadeOut(circle))

class SimpleField(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED
        },
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)  # **把dictionary解包
        plane.add(plane.get_axis_labels()) 
        self.add(plane)  

        points = [x*RIGHT+y*UP
            for x in np.arange(-5,5,1)
            for y in np.arange(-5,5,1)
            ]     

        vec_field = []  
        for point in points:
            field = 0.5*RIGHT + 0.5*UP   
            result = Vector(field).shift(point)  
            vec_field.append(result)   

        draw_field = VGroup(*vec_field)  


        self.play(ShowCreation(draw_field)) 

class FieldWithAxes(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field = VGroup(*[self.calc_field(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])

        self.play(ShowCreation(field))


    def calc_field(self,point):
        #This calculates the field at a single point.
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        #efield = (point - self.point_charge_loc)/r**3
        #efield = np.array((-y,x,0))/math.sqrt(x**2+y**2)  #Try one of these two fields
        efield = np.array(( -2*(y%2)+1 , -2*(x%2)+1 , 0 ))/3  #Try one of these two fields
        return Vector(efield,color=YELLOW).shift(point)

class MovingCharges(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field = VGroup(*[self.calc_field(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])
        self.field=field
        source_charge = self.Positron().move_to(self.point_charge_loc)
        self.play(FadeIn(source_charge))
        self.play(ShowCreation(field))
        self.moving_charge()

    def calc_field(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return Vector(efield).shift(point)

    def moving_charge(self):
        numb_charges=4
        possible_points = [v.get_start() for v in self.field]
        points = random.sample(possible_points, numb_charges)
        particles = VGroup(*[
            self.Positron().move_to(point)
            for point in points
        ])
        for particle in particles:
            particle.velocity = np.array((0,0,0))

        self.play(FadeIn(particles))
        self.moving_particles = particles
        self.add_foreground_mobjects(self.moving_particles )
        self.always_continually_update = True
        self.wait(10)

    def field_at_point(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return efield

    def continual_update(self, *args, **kwargs):
        if hasattr(self, "moving_particles"):
            dt = self.frame_duration
            for p in self.moving_particles:
                accel = self.field_at_point(p.get_center())
                p.velocity = p.velocity + accel*dt
                p.shift(p.velocity*dt)


    class Positron(Circle):
        CONFIG = {
        "radius" : 0.2,
        "stroke_width" : 3,
        "color" : RED,
        "fill_color" : RED,
        "fill_opacity" : 0.5,
        }
        def __init__(self, **kwargs):
            Circle.__init__(self, **kwargs)
            plus = TexMobject("+")
            plus.scale(0.7)
            plus.move_to(self)
            self.add(plus)

class FieldOfMovingCharge(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_start_loc" : 5.5*LEFT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field = VGroup(*[self.create_vect_field(self.point_charge_start_loc,x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])
        self.field=field
        self.source_charge = self.Positron().move_to(self.point_charge_start_loc)
        self.source_charge.velocity = np.array((1,0,0))
        self.play(FadeIn(self.source_charge))
        self.play(ShowCreation(field))
        self.moving_charge()

    def create_vect_field(self,source_charge,observation_point):
        return Vector(self.calc_field(source_charge,observation_point)).shift(observation_point)

    def calc_field(self,source_point,observation_point):
        x,y,z = observation_point
        Rx,Ry,Rz = source_point
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2 + (z-Rz)**2)
        if r<0.0000001:   #Prevent divide by zero  ##Note:  This won't work - fix this
            efield = np.array((0,0,0))  
        else:
            efield = (observation_point - source_point)/r**3
        return efield



    def moving_charge(self):
        numb_charges=3
        possible_points = [v.get_start() for v in self.field]
        points = random.sample(possible_points, numb_charges)
        particles = VGroup(self.source_charge, *[
            self.Positron().move_to(point)
            for point in points
        ])
        for particle in particles[1:]:
            particle.velocity = np.array((0,0,0))
        self.play(FadeIn(particles[1:]))
        self.moving_particles = particles
        self.add_foreground_mobjects(self.moving_particles )
        self.always_continually_update = True
        self.wait(10)


    def continual_update(self, *args, **kwargs):
        Scene.continual_update(self, *args, **kwargs)
        if hasattr(self, "moving_particles"):
            dt = self.frame_duration

            for v in self.field:
                field_vect=np.zeros(3)
                for p in self.moving_particles:
                    field_vect = field_vect + self.calc_field(p.get_center(), v.get_start())
                v.put_start_and_end_on(v.get_start(), field_vect+v.get_start())

            for p in self.moving_particles:
                accel = np.zeros(3)
                p.velocity = p.velocity + accel*dt
                p.shift(p.velocity*dt)


    class Positron(Circle):
        CONFIG = {
        "radius" : 0.2,
        "stroke_width" : 3,
        "color" : RED,
        "fill_color" : RED,
        "fill_opacity" : 0.5,
        }
        def __init__(self, **kwargs):
            Circle.__init__(self, **kwargs)
            plus = TexMobject("+")
            plus.scale(0.7)
            plus.move_to(self)
            self.add(plus)


class ExampleThreeD(ThreeDScene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field2D = VGroup(*[self.calc_field2D(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])

        self.set_camera_orientation(phi=PI/3,gamma=PI/5)
        self.play(ShowCreation(field2D))
        self.wait()
        #self.move_camera(gamma=0,run_time=1)  #currently broken in manim
        self.move_camera(phi=3/4*PI, theta=-PI/2)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(6)

    def calc_field2D(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return Vector(efield).shift(point)

###################################################

#################### 3D-Scenes ####################

class CameraPosition4(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=80 * DEGREES,theta=20*DEGREES,gamma=30*DEGREES,distance=6)
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.wait()

class MoveCamera1(ThreeDScene):
    
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)

    def construct(self):
        
        axes = ThreeDAxes()
        circle=Circle()
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.move_camera(phi=0*DEGREES,theta=0*DEGREES,gamma=0*DEGREES,run_time=3)
        self.wait()

class MoveCamera2(ThreeDScene):
    
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)

    def construct(self):
        
        axes = ThreeDAxes()
        circle=Circle()
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.move_camera(phi=0*DEGREES,theta=0*DEGREES,gamma=90*DEGREES,run_time=1)
        self.wait()

class MoveCamera3(ThreeDScene):
    
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)

    def construct(self):
        
        axes = ThreeDAxes()
        circle=Circle()
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.move_camera(phi=80*DEGREES,theta=20*DEGREES,gamma=20*DEGREES,run_time=1)
        self.wait()

class MoveCamera4(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=80 * DEGREES)           
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.begin_ambient_camera_rotation(rate=0.1)            #Start move camera
        self.wait(5)
        self.stop_ambient_camera_rotation()                     #Stop move camera
        self.move_camera(phi=80*DEGREES,theta=-PI/2)            #Return the position of the camera
        self.wait()

class ParametricCurve1(ThreeDScene):
    def construct(self):
        curve1=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u/2
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        curve2=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        axes = ThreeDAxes()

        self.add(axes)

        self.set_camera_orientation(phi=80 * DEGREES,theta=-60*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1) 
        self.play(ShowCreation(curve1))
        self.wait()
        self.play(Transform(curve1,curve2),rate_func=there_and_back,run_time=3)
        self.wait()

# Add this in the object: .set_shade_in_3d(True)

class ParametricCurve2(ThreeDScene):
    def construct(self):
        curve1=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u/2
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        curve2=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )

        curve1.set_shade_in_3d(True)
        curve2.set_shade_in_3d(True)

        axes = ThreeDAxes()

        self.add(axes)

        self.set_camera_orientation(phi=80 * DEGREES,theta=-60*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1) 
        self.play(ShowCreation(curve1))
        self.wait()
        self.play(Transform(curve1,curve2),rate_func=there_and_back,run_time=3)
        self.wait()

    #----- Surfaces
class SurfacesAnimation(ThreeDScene):  # 圆面
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)
    def construct(self):
        axes = ThreeDAxes()
        
        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)


        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(sphere))
        self.wait(5)
        
class SurfacesAnimation2(ThreeDScene):  # 圆柱面
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)
    def construct(self):
        axes = ThreeDAxes()
        
        cylinder = ParametricSurface(
			lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (1 - u)
            ]),
            resolution=(6, 32)).fade(0.5) #Resolution of the surfaces


        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(cylinder))
        self.wait(5)

class SurfacesAnimation3(ThreeDScene):  # 抛物面
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)
    def construct(self):
        axes = ThreeDAxes()
        
        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v)*u,
                np.sin(v)*u,
                u**2
            ]),v_max=TAU,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(10, 32)).scale(2)

        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(paraboloid))
        self.wait(5)

class SurfacesAnimation4(ThreeDScene):  # 马鞍面
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)
    def construct(self):
        axes = ThreeDAxes()
        
        para_hyp = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v**2
            ]),v_min=-2,v_max=2,u_min=-2,u_max=2,checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)).scale(1)

        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(para_hyp))
        self.wait(5)

class SurfacesAnimation5(ThreeDScene):  # 圆锥面
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)
    def construct(self):
        axes = ThreeDAxes()
        
        cone = ParametricSurface(
            lambda u, v: np.array([
                u*np.cos(v),
                u*np.sin(v),
                u
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[GREEN_D, GREEN_E],
            resolution=(15, 32)).scale(1)

        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(cone))
        self.wait(5)

class SurfacesAnimation6(ThreeDScene):   # 双曲面
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)
    def construct(self):
        axes = ThreeDAxes()
        
        hip_one_side = ParametricSurface(
            lambda u, v: np.array([
                np.cosh(u)*np.cos(v),
                np.cosh(u)*np.sin(v),
                np.sinh(u)
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[YELLOW_D, YELLOW_E],
            resolution=(15, 32))

        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(hip_one_side))
        self.wait(5)

class SurfacesAnimation7(ThreeDScene):  # 椭圆面
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)
    def construct(self):
        axes = ThreeDAxes()
        
        ellipsoid = ParametricSurface(
            lambda u, v: np.array([
                1*np.cos(u)*np.cos(v),
                2*np.cos(u)*np.sin(v),
                0.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[TEAL_D, TEAL_E],
            resolution=(15, 32)).scale(2)

        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(ellipsoid))
        self.wait(5)

class SurfacesAnimation8(ThreeDScene):
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)
    def construct(self):
        axes = ThreeDAxes()
        
        ellipsoid=ParametricSurface(
            lambda u, v: np.array([
                1*np.cos(u)*np.cos(v),
                2*np.cos(u)*np.sin(v),
                0.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[TEAL_D, TEAL_E],
            resolution=(15, 32)).scale(2)
        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(sphere))
        self.wait()
        self.play(ReplacementTransform(sphere,ellipsoid))
        self.wait(1)
        

###################################################

###################### Others #####################

class ForEachExample(Scene):
    def construct(self):
        text_list=[]
        text_group=VGroup()
        for i in range(1,13):
            t=str(i)
            text=TextMobject(t)
            text.move_to(UP*2.5)
            text.rotate(-PI/6*i,about_point=ORIGIN)
            self.play(Write(text),run_time=0.2)
            text_list.append(text)
            text_group=VGroup(text_group,text_list[i-1])
        self.wait()

class example(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange_submobjects(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()
        self.play(
            LaggedStart(FadeOutAndShiftUp,title),
            LaggedStart(FadeOutAndShiftDown, basel),
        )
        self.wait()


class DotMap(Scene):
    def construct(self):
        dots = dict()
        annos = dict()
        var_index = 0
        for x in range(-7, 8):
            for y in range(-4, 5):
                annos[f"{x}{y}"] = TexMobject(f"({x}, {y})")
                dots[f"{var_index}"] = Dot(np.array([x, y, 0]))
                var_index = var_index + 1
        for anno, dot in zip(annos.values(), dots.values()):
            self.add(anno)
            self.add(dot)
            self.wait(0.2)
            self.remove(anno)

class CoorPolygon(Scene):
    def construct(self):
        for x in range(-7, 8):
            for y in range(-4, 5):
                self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))
        polygon = Polygon(
            np.array([3, 2, 0]),
            np.array([1, -1, 0]),
            np.array([-5, -4, 0]),
            np.array([-4, 4, 0]))
        self.add(polygon)
        self.play(Uncreate(polygon))

class CoorAlias(Scene):
    def construct(self):
        for x in range(-7, 8):
            for y in range(-4, 5):
                self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))

        aliases = {
            "UP": UP,
            "np.array([0,1,0])": np.array([0, 1, 0]),
            "DOWN": DOWN,
            "np.array([0,-1,0])": np.array([0, -1, 0]),
            "LEFT": LEFT,
            "np.array([-1,0,0])": np.array([-1, 0, 0]),
            "RIGHT": RIGHT,
            "np.array([1,0,0])": np.array([1, 0, 0]),
            "UL": UL,
            "np.array([-1,1,0])": np.array([-1, 1, 0]),
            "DL": DL,
            "np.array([-1,-1,0])": np.array([-1, -1, 0]),
            "UR": UR,
            "np.array([1,1,0])": np.array([1, 1, 0]),
            "DR": DR,
            "np.array([1,-1,0])": np.array([1, -1, 0])}
        circle = Circle(color=RED, radius=0.5)
        self.add(circle)
        self.wait(0.5)

        for text, aliase in aliases.items():
            anno = TexMobject(f"\\texttt{{{text}}}")
            self.play(Write(anno, run_time=0.2))
            self.play(ApplyMethod(circle.shift, aliase))
            self.wait(0.2)
            self.play(FadeOut(anno, run_time=0.2))

class CoorArithmetic(Scene):
    def construct(self):
        for x in range(-7, 8):
            for y in range(-4, 5):
                self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))

        circle = Circle(color=RED, radius=0.5)
        self.add(circle)
        self.wait(0.5)

        aliases = {
            "LEFT * 3": LEFT * 3,
            "UP + RIGHT / 2": UP + RIGHT / 2,
            "DOWN + LEFT * 2": DOWN + LEFT * 2,
            "RIGHT * 3.75 * DOWN": RIGHT * 3.75 * DOWN,
            # certain arithmetic won't work as you expected
            # In [4]: RIGHT * 3.75 * DOWN
            # Out[4]: array([ 0., -0.,  0.])
            "RIGHT * 3.75 + DOWN": RIGHT * 3.75 + DOWN}

        for text, aliase in aliases.items():
            anno = TexMobject(f"\\texttt{{{text}}}")
            self.play(Write(anno, run_time=0.2))
            self.play(ApplyMethod(circle.shift, aliase))
            self.wait(0.2)
            self.play(FadeOut(anno, run_time=0.2))

class R(Scene):
    def construct(self):
        text=TextMobject("start")
        text.to_corner(RIGHT + UP)
        squares = VGroup()
        for i in range(9):
            squares.add(Square())
        squares.arrange_in_grid(n_rows=3, n_cols=3)
        self.add(squares)
        anims=[]
        for i in range(18):
            anims.append(FadeToColor(squares[i%9],RED,rate_func=there_and_back))
        self.play(Write(text))
        self.play(AnimationGroup(
            *anims,
            lag_ratio=0.1,
            group=Group(*[anim.mobject for anim in anims])))
        self.play(Transform(text,TextMobject("end").to_corner(RIGHT + UP)))
        self.wait()

class AnimationFadeOut(Scene):
    def construct(self):
        square = Square()

        anno = TextMobject("Fade Out") # 淡出效果
        anno.shift(2 * DOWN)
        self.add(anno)
        self.add(square)
        self.play(FadeOut(square))

class AnimationFadeIn(Scene):
    def construct(self):
        square = Square()
        
        anno = TextMobject("Fade In") # 淡入效果
        anno.shift(2 * DOWN)
        self.add(anno)
        self.play(FadeIn(square))

class AnimationFadeInFrom(Scene):
    def construct(self):
        square = Square()
        for label, edge in zip(
            ["LEFT", "RIGHT", "UP", "DOWN"], [LEFT, RIGHT, UP, DOWN]
        ):
            anno = TextMobject(f"Fade In from {label}")
            anno.shift(2 * DOWN)
            self.add(anno)

            self.play(FadeInFrom(square, edge))
            self.remove(anno, square)
                  
# 从上下左右四个方向淡出
class AnimationFadeOutAndShift(Scene):
    def construct(self):
        square = Square()
        for label, edge in zip(
            ["LEFT", "RIGHT", "UP", "DOWN"], [LEFT, RIGHT, UP, DOWN]
        ):
            anno = TextMobject(f"Fade Out and shift {label}")
            anno.shift(2 * DOWN)
            self.add(anno)

            self.play(FadeOutAndShift(square, edge))
            self.remove(anno, square)

# 从点淡入
class AnimationFadeInFromPoint(Scene):
    def construct(self):
        square = Square()
        for i in range(-6, 7, 2):
            anno = TextMobject(f"Fade In from point {i}")
            anno.shift(2 * DOWN)
            self.add(anno)
            self.play(FadeInFromPoint(square, point=i))
            self.remove(anno, square)

# 从以一定的比例放大或缩小淡入
class AnimationFadeInFromLarge(Scene):
    def construct(self):
        square = Square()

        for factor in [0.1, 0.5, 0.8, 1, 2, 5]:
            anno = TextMobject(f"Fade In from large scale\_factor={factor}")
            anno.shift(2 * DOWN)
            self.add(anno)

            self.play(FadeInFromLarge(square, scale_factor=factor))
            self.remove(anno, square)

class AnimationGrowFromEdge(Scene):
    def construct(self):

        for label, edge in zip(
            ["LEFT", "RIGHT", "UP", "DOWN"], [LEFT, RIGHT, UP, DOWN]
        ):
            anno = TextMobject(f"Grow from {label} edge")
            anno.shift(2 * DOWN)
            self.add(anno)
            square = Square()
            self.play(GrowFromEdge(square, edge))
            self.remove(anno, square)

class AnimationGrowFromCenter(Scene):
    def construct(self):
        square = Square()

        anno = TextMobject("Grow from center")
        anno.shift(2 * DOWN)
        self.add(anno)

        self.play(GrowFromCenter(square))

class AnimationFadeInFromDiagonal(Scene):
    def construct(self):
        square = Square()
        for diag in [UP + LEFT, UP + RIGHT, DOWN + LEFT, DOWN + RIGHT]:
            self.play(FadeInFrom(square, diag))
                           
class AnimationGrowFromPoint(Scene):
    def construct(self):
        square = Square()
        for i in range(-6, 7, 2):
            anno = TextMobject(f"Grow In from point {i}")
            anno.shift(2 * DOWN)
            self.add(anno)
            self.play(GrowFromPoint(square, point=i))
            self.remove(anno, square)   

class AnimationIndicate(Scene):
    def construct(self):
        anno = TextMobject("Indicate")

        self.add(anno)
        self.play(Indicate(anno))

class AnimationFocusOn(Scene):
    def construct(self):
        anno = TextMobject("Focus On")

        self.add(anno)
        self.play(FocusOn(anno,opacity=0.7))

class AnimationFlash(Scene):
    def construct(self):
        anno = TextMobject("Flash")

        self.add(anno)
        self.play(Flash(anno))

class AnimationCircleIndicate(Scene):
    def construct(self):
        anno = TextMobject("CircleIndicate")

        self.add(anno)
        self.play(CircleIndicate(anno))

class AnimationShowPassingFlash(Scene):
    def construct(self):
        anno = TextMobject("ShowPassingFlash")

        self.add(anno)
        self.play(ShowPassingFlash(anno))

class AnimationShowCreationThenDestruction(Scene):
    def construct(self):
        anno = TextMobject("ShowCreationThenDestruction")

        self.add(anno)
        self.play(ShowCreationThenDestruction(anno))

class AnimationShowCreationThenFadeOut(Scene):
    def construct(self):
        anno = TextMobject("ShowCreationThenFadeOut")

        self.add(anno)
        self.play(ShowCreationThenFadeOut(anno))

class AnimationAnimationOnSurroundingRectangle(Scene):
    def construct(self):
        anno = TextMobject("AnimationOnSurroundingRectangle")

        self.add(anno)
        self.play(AnimationOnSurroundingRectangle(anno))

class AnimationShowPassingFlashAround(Scene):
    def construct(self):
        anno = TextMobject("ShowPassingFlashAround")

        self.add(anno)
        self.play(ShowPassingFlashAround(anno))

class AnimationShowCreationThenDestructionAround(Scene):
    def construct(self):
        anno = TextMobject("ShowCreationThenDestructionAround")

        self.add(anno)
        self.play(ShowCreationThenDestructionAround(anno))
        self.wait(2)

class AnimationShowCreationThenFadeAround(Scene):
    def construct(self):
        anno = TextMobject("ShowCreationThenFadeAround")

        self.add(anno)
        self.play(ShowCreationThenFadeAround(anno))
        self.wait(2)


class AnimationApplyWave(Scene):
    def construct(self):
        anno = TextMobject("ApplyWave")

        self.add(anno)
        self.play(ApplyWave(anno))
        self.wait(2)

class AnimationWiggleOutThenIn(Scene):
    def construct(self):
        anno = TextMobject("WiggleOutThenIn")

        self.add(anno)
        self.play(WiggleOutThenIn(anno))
        self.wait(2)

class AnimationTurnInsideOut(Scene):
    def construct(self):
        anno = TextMobject("TurnInsideOut")

        self.add(anno)
        self.play(TurnInsideOut(anno))
        self.wait(2)

class HomotopyExample(Scene):
    def construct(self):
        def plane_wave_homotopy(x, y, z, t):
            norm = get_norm([x, y])
            tau = interpolate(5, -5, t) + norm/FRAME_X_RADIUS
            alpha = sigmoid(tau)
            return [x, y + 0.5*np.sin(2*np.pi*alpha)-t*SMALL_BUFF/2, z]

        mobjects=VGroup(
            TextMobject("Text").scale(3),
            Square(),
        ).arrange_submobjects(RIGHT,buff=2)

        self.add(mobjects)
        self.play(
            *[Homotopy(
                plane_wave_homotopy,
                mob
            ) for mob in mobjects]
        )
        self.wait(0.3)

class PhaseFlowExample(Scene):
    def construct(self):
        def func(t):
            return t*0.5*RIGHT

        mobjects=VGroup(
            TextMobject("Text").scale(3),
            Square(),
        ).arrange_submobjects(RIGHT,buff=2)

        self.play(
            *[PhaseFlow(
                func, mob,
                run_time = 2,
            )for mob in mobjects]
        )

        self.wait()

class MoveAlongPathExample(Scene):
    def construct(self):
        line=Line(ORIGIN,RIGHT*FRAME_WIDTH,buff=1)
        line.move_to(ORIGIN)
        dot=Dot()
        dot.move_to(line.get_start())

        self.add(line,dot)
        self.play(
            MoveAlongPath(dot,line)
        )
        self.wait(0.3)

class RotatingExample(Scene):
    def construct(self):
        square=Square().scale(2)
        self.add(square)

        self.play(
            Rotating(
                square,
                radians=PI/4,
                run_time=2
            )
        )
        self.wait(0.3)
        self.play(
            Rotating(
                square,
                radians=PI,
                run_time=2,
                axis=RIGHT
            )
        )
        self.wait(0.3)

class RotateExample(Scene):
    def construct(self):
        square=Square().scale(2)
        self.add(square)

        self.play(
            Rotate(
                square,
                PI/4,
                run_time=2
            )
        )
        self.wait(0.3)
        self.play(
            Rotate(
                square,
                PI,
                run_time=2,
                axis=RIGHT
            )
        )
        self.wait(0.3)

class DrawBorderThenFillExample(Scene):
    def construct(self):
        vmobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        vmobjects.scale(1.5)
        vmobjects.arrange_submobjects(RIGHT,buff=2)

        self.play(
            *[DrawBorderThenFill(mob) for mob in vmobjects]
        )

        self.wait()

class SpinInFromNothingExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Square(),
                RegularPolygon(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.play(
            *[SpinInFromNothing(mob) for mob in mobjects]
        )

        self.wait()

class ShrinkToCenterExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Square(),
                RegularPolygon(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.play(
            *[ShrinkToCenter(mob) for mob in mobjects]
        )

        self.wait()

class TransformExample(Scene):
    def construct(self):
        mobject = RegularPolygon(3).scale(2)

        self.add(mobject)

        for n in range(4,9):
            self.play(
                Transform(
                    mobject,
                    RegularPolygon(n).scale(2)
                )
            )

        self.wait(0.3)

class ReplacementTransformExample(Scene):
    def construct(self):
        polygons = [*[RegularPolygon(n).scale(2) for n in range(3,9)]]

        self.add(polygons[0])

        for i in range(len(polygons)-1):
            self.play(
                ReplacementTransform(
                    polygons[i],
                    polygons[i+1]
                )
            )

        self.wait(0.3)


class TransformFromCopyExample(Scene):
    def construct(self):
        mobject = RegularPolygon(3).scale(2)

        self.add(mobject)

        for n in range(4,9):
            self.play(
                TransformFromCopy(
                    mobject,
                    RegularPolygon(n).scale(2)
                )
            )

        self.wait(0.3)

class ClockwiseTransformExample(Scene):
    def construct(self):
        polygons = VGroup(
              *[RegularPolygon(n).scale(0.7) for n in range(3,9)]
        ).arrange_submobjects(RIGHT,buff=1)

        self.add(polygons[0])

        for i in range(len(polygons)-1):
            self.play(
                ClockwiseTransform(
                    polygons[0],
                    polygons[i+1]
                )
            )

        self.wait(0.3)


class CounterclockwiseTransformExample(Scene):
    def construct(self):
        polygons = VGroup(
            *[RegularPolygon(n).scale(0.7) for n in range(3,9)]
        ).arrange_submobjects(RIGHT,buff=1)

        self.add(polygons[0])

        for i in range(len(polygons)-1):
            self.play(
                CounterclockwiseTransform(
                    polygons[0],
                    polygons[i+1]
                )
            )

        self.wait(0.3)

class MoveToTargetExample(Scene):
    def construct(self):
        mobject=Square()
        mobject.generate_target()
        VGroup(mobject,mobject.target)\
            .arrange_submobjects(RIGHT,buff=3)

        mobject.target.rotate(PI/4)\
                      .scale(2)\
                      .set_stroke(PURPLE,9)\
                      .set_fill(ORANGE,1)

        self.add(mobject)
        self.wait(0.3)

        self.play(MoveToTarget(mobject))
        self.wait(0.3)

class ApplyMethodExample(Scene):
    def construct(self):
        dot = Dot()
        text = TextMobject("Text")

        dot.next_to(text,LEFT)

        self.add(text,dot)

        self.play(ApplyMethod(text.scale,3,{"about_point":dot.get_center()}))
        #                                  --------------------------------
        #                                          Optional parameters

        self.wait(0.3)

class ApplyPointwiseFunctionExample(Scene):
    def construct(self):
        text = TextMobject("Text")

        self.add(text)

        def spread_out(p):
            p = p + 2*DOWN
            return (FRAME_X_RADIUS+FRAME_Y_RADIUS)*p/get_norm(p)
            #      -------------------------------
            #          See manimlib/constants.py

        self.play(
            ApplyPointwiseFunction(spread_out, text)
        )

class ApplyPointwiseFunctionToCenterExample(Scene):
    def construct(self):
        text = TextMobject("Text")

        self.add(text)

        def spread_out(p):
            p = p + 2*DOWN
            return (FRAME_X_RADIUS+FRAME_Y_RADIUS)*p/get_norm(p)
            #      -------------------------------
            #          See manimlib/constants.py

        self.play(
            ApplyPointwiseFunctionToCenter(spread_out, text)
        )

class FadeToColorExample(Scene):
    def construct(self):
        text = TextMobject("Text")\
               .set_width(FRAME_WIDTH)

        colors=[RED,PURPLE,GOLD,TEAL]

        self.add(text)

        for color in colors:
            self.play(FadeToColor(text,color))

        self.wait(0.3)

class ScaleInPlaceExample(Scene):
    def construct(self):
        text = TextMobject("Text")\
               .set_width(FRAME_WIDTH/2)

        scale_factors=[2,0.3,0.6,2]

        self.add(text)

        for scale_factor in scale_factors:
            self.play(ScaleInPlace(text,scale_factor))

        self.wait(0.3)

class RestoreExample(Scene):
    def construct(self):
        text = TextMobject("Original")\
               .set_width(FRAME_WIDTH/2)

        text.save_state()

        text_2 = TextMobject("Modified")\
               .set_width(FRAME_WIDTH/1.5)\
               .set_color(ORANGE)\
               .to_corner(DL)

        self.add(text)

        self.play(Transform(text,text_2))
        self.play(
            text.shift,RIGHT,
            text.rotate,PI/4
            )
        self.play(Restore(text))

        self.wait(0.7)

class ApplyFunctionExample(Scene):
    def construct(self):
        text = TextMobject("Text")\
               .to_corner(DL)

        self.add(text)

        def apply_function(mob):
            mob.scale(2)
            mob.to_corner(UR)
            mob.rotate(PI/4)
            mob.set_color(RED)
            return mob

        self.play(
            ApplyFunction(
                apply_function,
                text
            )
        )

        self.wait(0.3)

class HelloWorld(Scene):
    def construct(self):
        helloWorld = TextMobject("Hello world!")
        self.play(Write(helloWorld))
        self.wait()

class RiemannRectanglesAnimation(GraphScene):
    CONFIG = {
        "y_max": 8,
        "y_axis_height": 5,
        "init_dx":0.5,
    }
    def construct(self):
        self.setup_axes()
        def func(x):
            return 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5

        graph=self.get_graph(func,x_min=0.3,x_max=9.2)
        kwargs = {
            "x_min" : 2,
            "x_max" : 8,
            "fill_opacity" : 0.75,
            "stroke_width" : 0.25,
        }
        flat_rectangles = self.get_riemann_rectangles(
                                self.get_graph(lambda x : 0),
                                dx=self.init_dx,
                                start_color=invert_color(PURPLE),
                                end_color=invert_color(ORANGE),
                                **kwargs
        )
        riemann_rectangles_list = self.get_riemann_rectangles_list(
                                graph,
                                6,
                                max_dx=self.init_dx,
                                power_base=2,
                                start_color=PURPLE,
                                end_color=ORANGE,
                                 **kwargs
        )
        self.add(graph)
        # Show Riemann rectangles
        self.play(ReplacementTransform(flat_rectangles,riemann_rectangles_list[0]))
        self.wait()
        for r in range(1,len(riemann_rectangles_list)):
            self.transform_between_riemann_rects(
                    riemann_rectangles_list[r-1],
                    riemann_rectangles_list[r],
                    replace_mobject_with_target_in_scene = True,
                )
        self.wait()











###################################################

####################### MY #######################

class TrySuccession(Scene):
    def construct(self):
        circle = Circle()
        T=TexMobject(r"\text{This is an } \alpha.")

        self.play(Succession(T))
        self.wait(2)
        
class TryLaggedStart(Scene):
    def construct(self):
        circle = Circle()
        T=TexMobject(r"\text{This is an } \alpha.")

        self.play(Write(T))
        self.play(LaggedStart(FadeOutAndShiftDown,T))

class TrySpeedometer(Scene):
    def construct(self):
        l=Speedometer()
        
        self.play(ShowCreation(l))
        self.wait(0.7)

class TryLaptop(Scene):
    def construct(self):
        l=Laptop()
        
        self.play(ShowCreation(l))
        self.wait(0.7)

class TryClock(Scene):
    def construct(self):
        l=Clock()
        
        self.play(ShowCreation(l))
        self.wait(0.7)

class TryTikz(Scene):
    def construct(self):
        l=TikzMobject(r"""
    woshifsihfis 
    \tikz \draw (0,0)--(0,1);
        """
        )
        
        self.add(l)
        self.wait(0.7)

class TikzMobject(TextMobject):
    CONFIG = {
        "stroke_width": 1,
        "fill_opacity": 1,
        "stroke_opacity": 1,
    }

class ExampleTikz(Scene):
#     CONFIG={
#     "camera_config":{"background_color":RED}
# }
    def construct(self):
        # w=TextMobject(r"Hello, world!\\你好,世界!\\こんにちは世界！\\안녕하세요 세상!")
        # w.set_color(RED)
        circuit = TikzMobject(r"""
            \begin{circuitikz}[american voltages]
            \draw
              (0,0) to [short, *-] (6,0)
              to [V, l_=$\mathrm{j}{\omega}_m \underline{\psi}^s_R$] (6,2) 
              to [R, l_=$R_R$] (6,4) 
              to [short, i_=$\underline{i}^s_R$] (5,4) 
              (0,0) to [open,v^>=$\underline{u}^s_s$] (0,4) 
              to [short, *- ,i=$\underline{i}^s_s$] (1,4) 
              to [R, l=$R_s$] (3,4)
              to [L, l=$L_{\sigma}$] (5,4) 
              to [short, i_=$\underline{i}^s_M$] (5,3) 
              to [L, l_=$L_M$] (5,0); 
              \end{circuitikz}
            """)
        # circuit.set_color(RED)
        self.play(Write(circuit))
        # self.play(Write(w))
        self.wait()


class C(Scene):
    def construct(self):
        HelloWorld1 = Text('Hello, World!')
        t=TextMobject(r"\calligra{Rangers}")
        self.play(Write(t))
        self.wait()

class BraceText(Scene):
    def construct(self):
        text=TexMobject(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        brace_top = Brace(text[1], UP, buff = SMALL_BUFF)
        brace_bottom = Brace(text[3], DOWN, buff = SMALL_BUFF)
        text_top = brace_top.get_text("$g'f$")
        text_bottom = brace_bottom.get_text("$f'g$")
        self.play(
            GrowFromCenter(brace_top),
            GrowFromCenter(brace_bottom),
            FadeIn(text_top),
            FadeIn(text_bottom)
            )
        self.wait()


class MRText(Text):
    CONFIG = {
        'font': 'MR CANFIELDS',
        'size': 0.7
    }
class Rangers(Scene):
    def construct(self):
        eng = TextMobject('Animation Engine')
        man = MRText('Manim')
        man.next_to(eng, DOWN)
        manim=VGroup(eng,man)
        manim.move_to(LEFT*3.5)

        l=Line(np.array([0,1,0]),np.array([0,-1,0]))

        ma = TextMobject('Maker')
        me = MRText('Rangers')
        me.next_to(ma,DOWN)
        rangers=VGroup(ma,me)
        rangers.move_to(RIGHT*3.5)


        self.play(Write(manim))
        self.play(Write(rangers))
        self.play(ShowCreation(l))
        self.wait(2)

class Plot3(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "axes_color" : BLUE,
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()
        
    def setup_axes(self):
        GraphScene.setup_axes(self)
        # Custom parametters
        self.x_axis.add_numbers(*[0,2,5,4])
        # Y parametters
        init_label_y = 0
        end_label_y = 50
        step_y = 5
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        self.play(Write(self.x_axis),Write(self.y_axis))

class SvgTry(Scene):
    def construct(self):
        file_name='bianqian.svg'

class ZoomedSceneExample(ZoomedScene):
    CONFIG = {
        "zoom_factor": 0.3,
        "zoomed_display_height": 1,
        "zoomed_display_width": 6,
        "image_frame_stroke_width": 20,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 3,
        },
    }

    def construct(self):
        # Set objects
        dot = Dot().shift(UL*2)

        image=ImageMobject(np.uint8([[ 0, 100,30 , 200],
                                     [255,0,5 , 33]]))
        image.set_height(7)
        frame_text=TextMobject("Frame",color=PURPLE).scale(1.4)
        zoomed_camera_text=TextMobject("Zommed camera",color=RED).scale(1.4)

        self.add(image,dot)

        # Set camera
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(dot)
        frame.set_color(PURPLE)

        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)

        # brackground zoomed_display
        zd_rect = BackgroundRectangle(
            zoomed_display,
            fill_opacity=0,
            buff=MED_SMALL_BUFF,
        )

        self.add_foreground_mobject(zd_rect)

        # animation of unfold camera
        unfold_camera = UpdateFromFunc(
            zd_rect,
            lambda rect: rect.replace(zoomed_display)
        )

        frame_text.next_to(frame,DOWN)

        self.play(
            ShowCreation(frame),
            FadeInFromDown(frame_text)
        )

        # Activate zooming
        self.activate_zooming()

        self.play(
            # You have to add this line
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera
        )

        zoomed_camera_text.next_to(zoomed_display_frame,DOWN)
        self.play(FadeInFromDown(zoomed_camera_text))

        # Scale in     x   y  z
        scale_factor=[0.5,1.5,0]

        # Resize the frame and zoomed camera
        self.play(
            frame.scale,                scale_factor,
            zoomed_display.scale,       scale_factor,
            FadeOut(zoomed_camera_text),
            FadeOut(frame_text)
        )

        # Resize the frame
        self.play(
            frame.scale,3,
            frame.shift,2.5*DOWN
        )

        # Resize zoomed camera
        self.play(
            ScaleInPlace(zoomed_display,2)
        )


        self.wait()

        self.play(
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera,
            # -------> Inverse
            rate_func=lambda t: smooth(1-t),
        )
        self.play(
            Uncreate(zoomed_display_frame),
            FadeOut(frame),
        )
        self.wait()

class Title(Scene):
    def construct(self):
        text=TextMobject('Dragon Fractal')
        text.scale(3)

        self.play(Write(text))
        self.wait()
        self.play(FadeOut(text))

class AudioTest(Scene):
    def construct(self):
        group_dots=VGroup(*[Dot()for _ in range(3)])
        group_dots.arrange_submobjects(RIGHT)
        for dot in group_dots:
            self.add_sound("click",gain=-10)
            self.add(dot)
            self.wait()
        self.wait()
 
class SVGTest(Scene):
    def construct(self):
        svg = SVGMobject("finger")
        #svg = SVGMobject("camera")
        self.play(DrawBorderThenFill(svg,rate_func=linear))
        self.wait()
 
class ImageTest(Scene):
    def construct(self):
        image = ImageMobject("note")
        self.play(FadeIn(image))
        self.wait()