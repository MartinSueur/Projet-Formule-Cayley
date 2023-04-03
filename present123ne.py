from manim import *
from arbres import *
from len import *
from layoutCreator import *

class Arbres123noeuds(Scene):
    def construct(self):
        t1 = Title(r"Représentons ces arbres")
        lh = Line([-6.1,0,0],[6.1,0,0])
        lv = Line([0,0,0],[0,2.8,0])
        a1 = Graph([1],[],labels=True,layout='partite',partitions=LayoutAuto(([1],[]))).move_to([-3.05,1.4,0]).scale(0.7)
        a2 = Graph([1,2],[(1,2)],labels=True,layout='partite',partitions=LayoutAuto(([1,2],[(1,2)]))).move_to([3.05,1.4,0]).scale(0.7)
        arbres3 = [[(1,2),(2,3)],[(1,3),(3,2)],[(2,1),(1,3)]]
        a3 = VGroup(*[Graph([1,2,3],e,labels=True,layout='partite',partitions=LayoutAuto(([1,2,3],e))).scale(0.7) for e in arbres3]).arrange_in_grid(rows=1,cols=3,buff=0.5).shift(2*DOWN)
        self.play(Write(t1))
        self.play(Write(a1))
        self.play(Write(lv))
        self.play(Write(a2))
        self.play(Write(lh))
        self.play(Write(a3))