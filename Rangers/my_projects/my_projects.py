from manimlib.imports import *


############# MY Mobjects ############
# DashedRectangle
class DashedRectangle(VGroup):
    CONFIG={
        "num_dashes": 30,
        "positive_space_ratio": 0.5,
        "width":5,
        "height":4,
        "line_config":{},
        "color":TEAL,
    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.add(*self.get_dashed_rectangle(self.width,self.height))
        self.move_to(ORIGIN)

    def get_dashed_rectangle(self,width,height):
        h1=[ORIGIN,UP*height]
        w1=[UP*height,UP*height+RIGHT*width]
        h2=[UP*height+RIGHT*width,RIGHT*width]
        w2=[RIGHT*width,ORIGIN]
        alpha=width/height
        divs=self.num_dashes

        n_h=int(divs/(2*(alpha+1)))
        n_w=int(alpha*n_h)
        dashedrectangle=VGroup()
        for n,l in zip([n_w,n_h],[[w1,w2],[h1,h2]]):
            for side in l:
                line=VMobject()
                line.set_points_as_corners(side)
                dashedrectangle.add(
                    DashedVMobject(
                        line,
                        num_dashes=n,
                        positive_space_ratio=self.positive_space_ratio,
                        ).set_color(self.color).set_style(**self.line_config)
                    )
        return [dashedrectangle[0],dashedrectangle[3],dashedrectangle[1],dashedrectangle[2]]

#SurroundingDashedRectangle depends of DashedRectangle
class SurroundingDashedRectangle(DashedRectangle):
    CONFIG={
        "num_dashes": 100,
        "positive_space_ratio": 0.5,
    }
    def __init__(self, mob, margin=0.1, **kwargs):
        width = mob.get_width() + margin
        height = mob.get_height() + margin
        super().__init__(width=width,height=height,**kwargs)
        self.move_to(mob)

class FreehandDraw(VMobject):
    CONFIG = {
        "sign":1,
        "close":False,
        "dx_random":7,
        "length":0.06
    }
    def __init__(self,path,partitions=120,**kwargs):
        VMobject.__init__(self,**kwargs)
        coords = []
        for p in range(int(partitions)+1):
            coord_i = path.point_from_proportion((p*0.989/partitions)%1)
            coord_f = path.point_from_proportion((p*0.989/partitions+0.001)%1)
            reference_line = Line(coord_i, coord_f).rotate(self.sign*PI/2, about_point=coord_i)
            normal_unit_vector = reference_line.get_unit_vector()
            static_vector = normal_unit_vector*self.length
            random_dx = random.randint(0,self.dx_random)
            random_normal_vector = random_dx * normal_unit_vector / 100
            point_coord = coord_i + random_normal_vector + static_vector
            coords.append(point_coord)
        if self.close:
            coords.append(coords[0])
        self.set_points_smoothly(coords)

# FreehandRectangle depends of FreehandDraw
class FreehandRectangle(VMobject):
    CONFIG = {
        "margin":0.7,
        "partitions":120,
    }
    def __init__(self,texmob,**kwargs):
        VMobject.__init__(self,**kwargs)
        rect = Rectangle(
            width  = texmob.get_width() + self.margin,
            height = texmob.get_height() + self.margin
            )
        rect.move_to(texmob)
        w = rect.get_width()  
        h = rect.get_height()
        alpha = w / h
        hp = np.ceil(self.partitions / (2 * (alpha + 1)))
        wp = np.ceil(alpha * hp)
        sides = VGroup(*[
            Line(rect.get_corner(c1),rect.get_corner(c2))
            for c1,c2 in zip([UL,UR,DR,DL],[UR,DR,DL,UL])
            ])
        total_points = []
        for side,p in zip(sides,[wp,hp,wp,hp]):
            path = FreehandDraw(side,p).points
            for point in path:
                total_points.append(point)
        total_points.append(total_points[0])
        self.set_points_smoothly(total_points)

class ZigZag(VMobject):
    CONFIG = {
        "margin":0.4,
        "sign":1
    }
    def __init__(self,path,partitions=10,**kwargs):
        VMobject.__init__(self,**kwargs)
        rect = Rectangle(
            width  = path.get_width() + self.margin,
            height = path.get_height() + self.margin
            )
        rect.move_to(path)
        w = rect.get_width()  
        h = rect.get_height()
        alpha = w / h
        hp = int(np.ceil(partitions / (2 * (alpha + 1))))
        wp = int(np.ceil(alpha * hp))
        sides = VGroup(*[
            Line(rect.get_corner(c1),rect.get_corner(c2))
            for c1,c2 in zip([UL,UR,DR,DL],[UR,DR,DL,UL])
            ])
        total_points = []
        for side,points in zip(sides,[wp,hp,wp,hp]):
            for p in range(points):
                total_points.append(side.point_from_proportion(p/points))
        total_points.append(total_points[0])
        middle = int(np.floor(len(total_points)/2))
        draw_points = []
        for p in range(2,middle):
            draw_points.append(total_points[-p*self.sign])
            draw_points.append(total_points[p*self.sign])
        self.set_points_smoothly(draw_points)

class MeasureDistance(VGroup):
    CONFIG = {
        "color":RED_B,
        "buff":0.3,
        "lateral":0.3,
        "invert":False,
        "dashed_segment_length":0.09,
        "dashed":True,
        "ang_arrows":30*DEGREES,
        "size_arrows":0.2,
        "stroke":2.4,
    }
    def __init__(self,mob,**kwargs):
        VGroup.__init__(self,**kwargs)
        if self.dashed==True:
            medicion=DashedLine(ORIGIN,mob.get_length()*RIGHT,dashed_segment_length=self.dashed_segment_length).set_color(self.color)
        else:
            medicion=Line(ORIGIN,mob.get_length()*RIGHT)
 
        medicion.set_stroke(None,self.stroke)
 
        pre_medicion=Line(ORIGIN,self.lateral*RIGHT).rotate(PI/2).set_stroke(None,self.stroke)
        pos_medicion=pre_medicion.copy()
 
        pre_medicion.move_to(medicion.get_start())
        pos_medicion.move_to(medicion.get_end())
 
        angulo=mob.get_angle()
        matriz_rotacion=rotation_matrix(PI/2,OUT)
        vector_unitario=mob.get_unit_vector()
        direccion=np.matmul(matriz_rotacion,vector_unitario)
        self.direccion=direccion
 
        self.add(medicion,pre_medicion,pos_medicion)
        self.rotate(angulo)
        self.move_to(mob)
 
        if self.invert==True:
            self.shift(-direccion*self.buff)
        else:
            self.shift(direccion*self.buff)
        self.set_color(self.color)
        self.tip_point_index = -np.argmin(self.get_all_points()[-1, :])
       
 
    def add_tips(self):
        linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
        vector_unitario=linea_referencia.get_unit_vector()
 
        punto_final1=self[0][-1].get_end()
        punto_inicial1=punto_final1-vector_unitario*self.size_arrows
 
        punto_inicial2=self[0][0].get_start()
        punto_final2=punto_inicial2+vector_unitario*self.size_arrows
 
        lin1_1=Line(punto_inicial1,punto_final1).set_color(self[0].get_color()).set_stroke(None,self.stroke)
        lin1_2=lin1_1.copy()
        lin2_1=Line(punto_inicial2,punto_final2).set_color(self[0].get_color()).set_stroke(None,self.stroke)
        lin2_2=lin2_1.copy()
 
        lin1_1.rotate(self.ang_arrows,about_point=punto_final1,about_edge=punto_final1)
        lin1_2.rotate(-self.ang_arrows,about_point=punto_final1,about_edge=punto_final1)
 
        lin2_1.rotate(self.ang_arrows,about_point=punto_inicial2,about_edge=punto_inicial2)
        lin2_2.rotate(-self.ang_arrows,about_point=punto_inicial2,about_edge=punto_inicial2)
 
 
        return self.add(lin1_1,lin1_2,lin2_1,lin2_2)
 
    def add_tex(self,text,scale=1,buff=-1,**moreargs):
        linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
        texto=TexMobject(text,**moreargs)
        ancho=texto.get_height()/2
        texto.rotate(linea_referencia.get_angle()).scale(scale).move_to(self)
        texto.shift(self.direccion*(buff+1)*ancho)
        return self.add(texto)
 
    def add_text(self,text,scale=1,buff=0.1,**moreargs):
        linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
        texto=TextMobject(text,**moreargs)
        ancho=texto.get_height()/2
        texto.rotate(linea_referencia.get_angle()).scale(scale).move_to(self)
        texto.shift(self.direccion*(buff+1)*ancho)
        return self.add(texto)
 
    def add_size(self,text,scale=1,buff=0.1,**moreargs):
        linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
        texto=TextMobject(text,**moreargs)
        ancho=texto.get_height()/2
        texto.rotate(linea_referencia.get_angle())
        texto.shift(self.direccion*(buff+1)*ancho)
        return self.add(texto)
 
    def add_letter(self,text,scale=1,buff=0.1,**moreargs):
        linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
        texto=TexMobject(text,**moreargs).scale(scale).move_to(self)
        ancho=texto.get_height()/2
        texto.shift(self.direccion*(buff+1)*ancho)
        return self.add(texto)
 
    def get_text(self, text,scale=1,buff=0.1,invert_dir=False,invert_texto=False,remove_rot=False,**moreargs):
        linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
        texto=TextMobject(text,**moreargs)
        ancho=texto.get_height()/2
        if invert_texto:
            inv=PI
        else:
            inv=0
        if remove_rot:
            texto.scale(scale).move_to(self)
        else:
            texto.rotate(linea_referencia.get_angle()).scale(scale).move_to(self)
            texto.rotate(inv)
        if invert_dir:
            inv=-1
        else:
            inv=1
        texto.shift(self.direccion*(buff+1)*ancho*inv)
        return texto
 
    def get_tex(self, tex,scale=1,buff=1,invert_dir=False,invert_texto=False,remove_rot=True,**moreargs):
        linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
        texto=TexMobject(tex,**moreargs)
        ancho=texto.get_height()/2
        if invert_texto:
            inv=PI
        else:
            inv=0
        if remove_rot:
            texto.scale(scale).move_to(self)
        else:
            texto.rotate(linea_referencia.get_angle()).scale(scale).move_to(self)
            texto.rotate(inv)
        if invert_dir:
            inv=-1
        else:
            inv=1
        texto.shift(self.direccion*(buff+1)*ancho)
        return texto
 
class RectanglePattern(VGroup):
    CONFIG={
        "space":0.2,
        "color":RED,
        "add_rectangle":False,
        "rectangle_color":WHITE,
        "rectangle_width":4
    }
    def __init__(self,width,height=None,stroke_width=2,**kwargs):
        super().__init__(**kwargs)
        if height==None:
            height=width
        W=width
        H=height
        b=self.space
        n=1
        if H>=W:
            while -H/2+n*b<H/2+W:
                if -H/2+n*b<-H/2+W:
                    x_i=W/2-n*b
                    x_f=W/2
                if -H/2+W<=(-H)/2+n*b and (-H)/2+n*b<=H/2:
                    x_i=-W/2
                    x_f=W/2
                if H/2<=(-H)/2+n*b and (-H)/2+n*b<H/2+W:
                    x_i=-W/2
                    x_f=H+W/2-n*b
                pat=FunctionGraph(lambda x : x-W/2-H/2+n*b, 
                                    color = self.color,
                                    stroke_width = stroke_width,
                                    x_min = x_i,
                                    x_max = x_f
                                    )
                self.add(pat)
                n+=1
        else:
            while n*b-H/2<W+H/2:
                if n*b-H/2<H/2:
                    x_i=W/2-n*b
                    x_f=W/2
                if H/2<=n*b-H/2 and n*b-H/2<W-H/2:
                    x_i=W/2-n*b
                    x_f=H+W/2-n*b
                if W-H/2<=n*b-H/2 and n*b-H/2<W+H/2:
                    x_i=-W/2
                    x_f=H+W/2-n*b
                pat=FunctionGraph(lambda x : x-W/2+n*b-H/2, 
                                    color = self.color,
                                    stroke_width = stroke_width,
                                    x_min = x_i,
                                    x_max = x_f
                                    )
                self.add(pat)
                n+=1
        if self.add_rectangle:
            self.add(
                Rectangle(
                    width=width,
                    height=height,
                    color=self.rectangle_color,
                    stroke_width=self.rectangle_width
                )
            )


############# MY ANIMATIONS ############
class PassRectangleAbstract(UpdateFromAlphaFunc):
    CONFIG = {
        "run_time": 1.3,
        "remover": True,
        "margin":0.1,
        "max_opacity":0.6,
        "init_opacity":0.2,
        "color":YELLOW,
        "rectangle_kwargs":{
            "fill_opacity":1,
            "stroke_width":0,
        },
    }

    def __init__(self, mobject,midle_color=None,**kwargs):
        digest_config(self, kwargs)
        self.mobject = mobject
        self.rectangle_kwargs["color"] = self.color
        if midle_color == None:
            midle_color = self.rectangle_kwargs["color"]
        rectangle = Rectangle(
            height=mobject.get_height()+self.margin,
            width=mobject.get_width()+self.margin,
            **self.rectangle_kwargs
            )
        rectangle.move_to(mobject)
        reference_line_left = Line(rectangle.get_corner(UL),rectangle.get_corner(DL))
        reference_line_right = Line(rectangle.get_corner(UR),rectangle.get_corner(DR))
        rectangle.init_state = rectangle.copy()
        rectangle_width = rectangle.get_width()
        rest_opacity = 1 - self.init_opacity
        def return_updater(mob,alpha):
            dx = interpolate(-PI/2,PI/2,alpha)
            mob.become(mob.init_state)
            mob.set_width(rectangle_width*np.cos(dx),stretch=True)
            # dx should not be zero
            sign = -abs(dx)/(dx+0.00000000001)
            direction = LEFT*sign
            reference_line = Line(
                rectangle.init_state.get_corner(UP+direction),
                rectangle.init_state.get_corner(DOWN+direction)
            )
            mob.next_to(reference_line,-direction,buff=0)
            opacity = self.init_opacity + (self.max_opacity-self.init_opacity)*np.cos(dx)
            mob.set_style(fill_opacity=opacity)
            mob.set_color(interpolate_color(self.rectangle_kwargs["color"],midle_color,np.cos(dx)))

        super().__init__(
            rectangle,return_updater
        )

class PassRectangle(AnimationGroup):
    def __init__(self, mobject, **kwargs):
        digest_config(self, kwargs)
        super().__init__(
            PassRectangleAbstract(mobject,**kwargs),
            #The reason for this, is that mobject always be foreground
            Animation(mobject)
        )

# UnderlineIndication
class UnderlineIndication(AnimationGroup):
    CONFIG = {
        "line_config":{},
        "line_type":Line,
        "reverse":True,
        "run_time":1.5
    }
    def __init__(self, mobject,margin=0.1,buff=0.2,**kwargs):
        digest_config(self, kwargs)
        line = self.line_type(
            mobject.get_corner(DL)+margin*LEFT,
            mobject.get_corner(DR)+margin*RIGHT,
            **self.line_config
        )
        line.shift(buff*DOWN)
        if self.reverse:
            kwargs["rate_func"] = there_and_back
            kwargs["run_time"] = self.run_time*2
        if self.line_type == DashedLine:
            kwargs["run_time"] = self.run_time/2
            kwargs["rate_func"] = smooth
            kwargs["lag_ratio"] = 0.005
        super().__init__(self.return_animation(line,**kwargs))
    
    def return_animation(self,line,**kwargs):
        if self.line_type == Line:
            return ShowCreationThenDestruction(line,**kwargs)
        elif self.line_type == DashedLine:
            return LaggedStartMap(ShowCreationThenDestruction,line,**kwargs)

class RemarkDashedRectangle(LaggedStart):
    CONFIG = {
        "line_config":{},
        "line_kwargs":{},
        "run_time":1,
        "lag_ratio":0.02,
        "color":YELLOW,
        "margin":0.1
    }
    def __init__(self,mob,**kwargs):
        digest_config(self, kwargs)
        self.line_kwargs["margin"] = self.margin
        # SurroundingDashedRectangle: See my_objects.py line 44
        dr = SurroundingDashedRectangle(
            mob,
            color=self.color,
            line_config=self.line_config,
            **self.line_kwargs
        )
        super().__init__(
            *[ShowCreationThenDestruction(line) for d in dr for line in d],
            **kwargs)

class FadeInFromEdges(LaggedStart):
    def __init__(self, text , **kwargs):
        digest_config(self, kwargs)
        super().__init__(
            *[FadeInFromPoint(obj,point=self.get_vector_from(obj,dist=1.4))for obj in text],
            **kwargs
        )

    def get_vector_from(self,obj,point=ORIGIN,dist=2):
            vect=obj.get_center()-point
            return vect*dist


class FadeInFromDirections(LaggedStart):
    CONFIG = {
        "directions":[DL,DOWN,DR,RIGHT,UR,UP,UL,LEFT],
        "magnitude":1
    }
    def __init__(self, text , **kwargs):
        digest_config(self, kwargs)
        self.reverse_directions=it.cycle(list(reversed(self.directions)))
        super().__init__(
            *[FadeInFromPoint(obj,point=obj.get_center()+d*self.magnitude)
                for obj,d in zip(text,self.reverse_directions)],
            **kwargs
        )

class FadeInFromRandom(LaggedStart):
    CONFIG = {
        "directions":[DL,DOWN,DR,RIGHT,UR,UP,UL,LEFT],
        "magnitude":0.5,
        "lag_ratio":0
    }
    def __init__(self, text , **kwargs):
        digest_config(self, kwargs)
        super().__init__(
            *[FadeInFromPoint(obj,point=random.choice(self.directions)*self.magnitude)
                for obj in text],
            **kwargs
        )


# Abstract scenes (no render this scenes)
# The "setup" method is always executed before the construct method
class GenericExample(Scene):
    def setup(self):
        text1 = Text("Hello world",font="Times").set_stroke(width=0)
        text2 = TexMobject(r"""
                    \oint_C \vec{B}\cdot d
                    \vec{l}=\mu_0\int_S \vec{J}
                    \cdot d \vec{s}+\mu_0
                    \epsilon_0\dfrac{d}{dt}
                    \int_S \vec{E}\cdot d \vec{s}"""
                )
        text3 = TextMobject("This is a example animation")
        self.text_group = VGroup(text1,text2,text3).arrange_submobjects(DOWN,buff=1)
        self.text_group.scale(1.4)
        self.add(self.text_group)

class GenericPaths(Scene):
    def setup(self):
        path1 = Square()
        path2 = Ellipse().scale(1.5)
        path3 = VMobject()
        path3.set_points_as_corners([LEFT*3,ORIGIN,UP,UP+RIGHT*3])
        self.path_group = VGroup(path1,path2,path3).arrange_submobjects(DL,buff=1)
        self.add(self.path_group)

class FormulaExample(Scene):
    def setup(self):
        self.tex_example = TexMobject(r"""
                    \oint_C \vec{B}\cdot d
                    \vec{l}=\mu_0\int_S \vec{J}
                    \cdot d \vec{s}+\mu_0
                    \epsilon_0\dfrac{d}{dt}
                    \int_S \vec{E}\cdot d \vec{s}"""
                )

#Scenes

class PassRectangleExample(GenericExample):
    def construct(self):
        t1,t2,t3 = self.text_group
        # PassRectangle: See my_animations.py line 4 -> 63
        self.play(
            PassRectangle(t1),
            PassRectangle(t2,color=TEAL),
            PassRectangle(t3,midle_color=ORANGE,color=RED)
            )
        self.wait()
        self.play(
            PassRectangle(t1,init_opacity=0.5,margin=0.5),
            PassRectangle(t2,init_opacity=0.1,max_opacity=1,rate_func=there_and_back),
            PassRectangle(t3,midle_color=ORANGE,color=RED,init_opacity=0.1,max_opacity=1)
            )
        self.wait(2)

class UnderlineIndicationExample(GenericExample):
    def construct(self):
        t1,t2,t3 = self.text_group
        # UnderlineIndication: See my_animations.py line 66
        self.play(
            UnderlineIndication(t1),
            UnderlineIndication(t2,line_type=DashedLine),
            )
        self.wait(2)

class DashedRectangleExample(GenericExample):
    def construct(self):
        t1,t2,t3 = self.text_group
        # DashedRectangle: See my_objects.py line 6
        dr1 = DashedRectangle(line_config={"stroke_opacity":0.5})
        # SurroundingDashedRectangle: See my_objects.py line 45
        dr2 = SurroundingDashedRectangle(t1)
        self.add(dr1,dr2)
        # RemarkDashedRectangle: See my_animations.py line 97
        self.play(
            RemarkDashedRectangle(t2),
            RemarkDashedRectangle(t3,line_config={"stroke_width":3},color=PURPLE,margin=0.5)
        )
        self.wait(2)

class FreeHandExample(GenericExample):
    def construct(self):
        t1,t2,t3 = self.text_group
        # FreehandRectangle: my_objects.py - line 81
        t1_fh = FreehandRectangle(t1)
        t2_fh = FreehandRectangle(t2,margin=0.2,color=RED,stroke_width=2)
        t3_fh = FreehandRectangle(t3,margin=0.2,color=RED,fill_opacity=1,fill_color=PURPLE,partitions=20)
        self.bring_to_back(t3_fh)
        self.play(
            *list(map(ShowCreation,[t1_fh,t2_fh])), #<- This is a way to play multiple animations:
            # *list(map(Animation,mobs)), # mobs can be a list or a VGroup
            DrawBorderThenFill(t3_fh),
            *list(map(Write,[t1,t2,t3])),
        )
        self.wait(2)

class FreeHandExample2(GenericPaths):
    def construct(self):
        p1,p2,p3 = self.path_group
        # FreehandDraw: my_objects.py - line 56
        p1_fh = FreehandDraw(p1,close=True)
        p2_fh = FreehandDraw(p2,close=True,color=RED,partitions=30,dx_random=2)
        p3_fh = FreehandDraw(p3,partitions=20,dx_random=1)
        fh_group = VGroup(p1_fh,p2_fh,p3_fh)
        self.wait()
        self.play(
            *[ReplacementTransform(mob1,mob2) for mob1,mob2 in zip(self.path_group,fh_group)]
        )
        self.wait(2)

class Zig(Scene):
    def construct(self):
        path = TextMobject("This is wrong").scale(2)
        # ZigZag: my_objects.py - line 110
        draw = ZigZag(path,color=RED,stroke_width=10)
        self.add(path)
        self.wait(1.5)
        self.play(ShowCreation(draw,run_time=1,rate_func=linear))
        self.wait(2)

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

class StartAnimationInTheMiddleOfAnother(Scene):
    def construct(self):
        c = Circle().scale(2)
        s = Square().scale(2)
        l = Line(DOWN,UP).scale(2)
        time = DecimalNumber(self.time).add_updater(lambda m: m.set_value(self.time))
        time.to_corner(DL)
        self.add(time)
        self.play(
            # 6 partitions, that is (total_time = 4):
            # ShowCreation starts at t=(0/6)*total_time=0s and end t=(5/6)*total_time=3.333s
            ShowCreation(c,  rate_func=Custom(6,0,5)),
            # FadeIn starts at t=(2/6)*total_time=1.3333s and end t=(4/6)*total_time=2.6666s
            FadeIn(s,        rate_func=Custom(6,2,4,func=there_and_back)),
            # GrowFromCenter starts at t=(4/6)*total_time=2.6666s and end t=(6/6)*total_time=4s
            GrowFromCenter(l,rate_func=Custom(6,4,6)),
            run_time=4 # <- total_time
            )
        self.wait()

class MeasureObject1(Scene):
    def construct(self):
        square=Square()
        measure_line=Line(square.get_corner(DL),square.get_corner(UL))
        # MeasureDistance: my_objects.py - line 143
        measure=MeasureDistance(measure_line).add_tips()
        measure_tex=measure.get_tex("x")
        self.add(square,measure,measure_tex)
        self.wait(2)

class MeasureObject2(Scene):
    def construct(self):
        triangle = RegularPolygon(n=3)
        #Vertices
        triangle.vertices_text = VMobject()
        triangle.vertices_text.add_updater(lambda mob: mob.become(self.get_triangle_vertices(triangle)))
        #Measure side
        triangle.measure1 = VMobject()
        triangle.measure1.add_updater(self.get_updater_side(triangle,0,1,"a"))
        triangle.measure2 = VMobject()
        triangle.measure2.add_updater(self.get_updater_side(triangle,1,2,"b",color=TEAL))
        #Sides
        self.add(triangle,triangle.vertices_text,triangle.measure1,triangle.measure2)
        self.wait()
        self.play(triangle.scale,[5,2,1])
        self.wait()
        self.play(triangle.scale,[0.7,2,1])
        self.wait(2)

    def get_triangle_vertices(self,mob,buff=0.3):
        vertices = mob.get_vertices()
        vertices_text = VGroup(*[
            Text(f"{v}",height=2,stroke_width=0,font="Times")\
            .move_to(mob.get_center()+(vert-mob.get_center())*(buff/get_norm(vert)+1))
            for v,vert in zip(range(len(vertices)),vertices)]
            )
        return vertices_text

    def get_measure_side(self,mob,vert1,vert2,tex,buff=2,**kwargs):
        vertices = mob.get_vertices()
        side = Line(vertices[vert2],vertices[vert1])
        return MeasureDistance(side,**kwargs).add_tips().add_letter(tex,buff=buff)

    def get_updater_side(self,*args,**kwargs):
        return lambda mob: mob.become(self.get_measure_side(*args,**kwargs))

class PatternExample(Scene):
    def construct(self):
        # RectanglePattern: my_objects.py - line 283
        pattern_1=RectanglePattern(4,2)
        pattern_2=RectanglePattern(3,add_rectangle=True)
        pattern_3=RectanglePattern(3,6,color=ORANGE)
        pg=VGroup(pattern_1,pattern_2,pattern_3).arrange(RIGHT)
        self.add(pg)
        self.wait()

class FadeInFromEdgesExample(FormulaExample):
    def construct(self):
        # if your TexMobject have one dimension, that is:
        # tex = TexMobject("SingleFormula")
        # Then you have to use FadeInFromEdges(tex[0])
        # If your TexMobject have multiple formulas, that is:
        # tex = TexMobject("Multiple","Formula")
        # Then you have to specify the number of array, that is:
        # FadeInFromEdges(tex[0]) or FadeInFromEdges(tex[1])
        # Same rules to FadeInFromDirections and FadeInFromRandom
        self.play(
            FadeInFromEdges(self.tex_example[0]),
            run_time=3
        )
        self.wait()

class FadeInFromDirectionsExample(FormulaExample):
    def construct(self):
        self.play(
            FadeInFromDirections(self.tex_example[0]),
            run_time=3
        )
        self.wait()

class FadeInFromRandomExample(FormulaExample):
    def construct(self):
        self.play(
            FadeInFromRandom(self.tex_example[0]),
            run_time=3
        )
        self.wait()
