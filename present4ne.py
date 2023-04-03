from manim import *
from arbres import *
from len import *
from layoutCreator import *

class Arbres4noeuds(Scene):
    def construct(self):
        t = Title("Arbres à 4 noeuds")
        tri = []
        tig = []
        for arbre in arbres4:
            if typeDarbre(arbre) == 1:
                tri.append(arbre)
            else:
                tig.append(arbre)
        tiges = VGroup(*[Graph(arbre[0],arbre[1],labels=True,layout='partite',partitions=LayoutAuto(arbre)).scale(0.6) for arbre in tig]).arrange_in_grid(rows=3,cols=4,buff=(0.25,0.7))
        tridents = VGroup(*[Graph(arbre[0],arbre[1],labels=True,layout='partite',partitions=LayoutAuto(arbre)).scale(0.6) for arbre in tri]).arrange_in_grid(rows=1,cols=4,buff=(0.7))
        arbres = VGroup(tiges,tridents).arrange_in_grid(rows=2,cols=1,buff=0.5)
        tige = Graph([1,2,3,4],[(1,2),(2,3),(3,4)],labels=True,layout='partite',partitions=LayoutAuto(([1,2,3,4],[(1,2),(2,3),(3,4)])),edge_config={(1, 2): {"stroke_color": BLUE},(2, 3): {"stroke_color": BLUE},(3, 4): {"stroke_color": BLUE}}).move_to([0,1,0]).scale(0.6)
        trident = Graph([1,2,3,4],[(1,2),(3,2),(4,2)],labels=True,layout='partite',partitions=LayoutAuto(([1,2,3,4],[(1,2),(3,2),(4,2)])),edge_config={(1, 2): {"stroke_color": GREEN},(3, 2): {"stroke_color": GREEN},(4, 2): {"stroke_color": GREEN}}).move_to([0,-1.5,0]).scale(0.6)
        circlesG = [Circle(0.15,color=BLUE,fill_opacity=1).move_to([x,1,0]) for x in [-1.2,-0.4,0.4,1.2]]
        s=0.95
        circlesD = [Circle(0.15,color=GREEN,fill_opacity=1).move_to(c) for c in [[-s,-1.5,0],[0,-1.5,0],[s,-1.02,0],[s,-1.98,0]]]
        
        
        self.play(Write(t))
        self.play(Write(arbres))
        self.wait(5)
        self.play(Circumscribe(tiges,color=BLUE))
        self.play(AnimationGroup(
            AnimationGroup(*[tig.animate.move_to([0,1,0]) for tig in tiges]),
            AnimationGroup(FadeIn(tige),AnimationGroup(*[FadeIn(circle) for circle in circlesG])),
            Write(Integer(number=12).set_color(BLUE).next_to(tige,DOWN)),
            lag_ratio=0.3))
        self.play(Circumscribe(tridents,color=GREEN))
        self.play(AnimationGroup(
            AnimationGroup(*[tri.animate.move_to([0,-1.5,0]) for tri in tridents]),
            AnimationGroup(FadeIn(trident),AnimationGroup(*[FadeIn(circle) for circle in circlesD])),
            Write(Integer(number=4).set_color(GREEN).next_to(trident,DOWN)),
            lag_ratio=0.3))
        self.wait()