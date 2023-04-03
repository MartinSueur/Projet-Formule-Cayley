from manim import *
from arbres import *
from len import *
from layoutCreator import *
from serieFinder import u

class Arbres5noeuds(Scene):
    def construct(self):
        listTypes = [
                     [(1,3),(2,3),(3,4),(5,3)],   #etoile
                     [(1,2),(2,3),(3,4),(5,3)],   #osselet
                     [(1,2),(2,3),(3,4),(4,5)]]   #tige

        cible = [[-4,-1,0],
                 [0,-1,0],
                 [4,-1,0]]

        types = [Graph([1,2,3,4,5],e,layout="partite",partitions=LayoutAuto(([1,2,3,4,5],e))).move_to(cible[i]).scale(0.7) for i,e in enumerate(listTypes)]

        compteurs = [Integer(number=0).next_to(c,DOWN) for c in cible]

        graphs = [Graph(vertices, edges, labels=True, layout="partite",partitions=LayoutAuto((vertices,edges))).scale(0.5).shift(LEFT*4+UP*2) for (vertices,edges) in arbres5]+[Graph([],[])]*3
        
        p=0
        factorielles = []
        texte = [r"\frac{5!}{4!}",r"\frac{5!}{2!}",r"\frac{5!}{2!}"]
        for c in compteurs:
            factorielles.append(MathTex(texte[p]).next_to(c,DOWN))
            p+=1
        delta = 90
        
        n=0

        self.play(AnimationGroup(*[Write(typ) for typ in types]+[Write(c) for c in compteurs]))
        bandeau = []
        for graph in graphs:
            if len(bandeau) < 3:
                self.play(AnimationGroup(
                FadeIn(graph,shift=RIGHT*3),
                AnimationGroup(*[arbre.animate.shift(RIGHT*3) for arbre in bandeau])),run_time=u[n]/2)
                n+=1
                bandeau.append(graph)
            elif len(bandeau) > 2 and len(bandeau) < 4:
                self.play(AnimationGroup(
                FadeIn(graph,shift=RIGHT*3),
                AnimationGroup(*[arbre.animate.shift(RIGHT*3) for arbre in bandeau])),run_time=u[n]/2)
                n+=1
                select = bandeau[0]
                typ = typeDarbre(([1,2,3,4,5],select.edges))-1
                c = compteurs[typ]
                self.play(AnimationGroup(Indicate(select),Indicate(types[typ]),c.animate.set_value(c.get_value()+1)),run_time=u[n]/2)
                n+=1
                bandeau.append(graph)
            else:
                self.play(AnimationGroup(
                FadeIn(graph,shift=RIGHT*3),
                AnimationGroup(*[arbre.animate.shift(RIGHT*3) for arbre in bandeau]),
                FadeOut(bandeau.pop(0),shift=RIGHT*3)),run_time=u[n]/2)
                n+=1
                select = bandeau[0]
                typ = typeDarbre(([1,2,3,4,5],select.edges))-1
                c = compteurs[typ]
                print(f"types={types} | compteurs={compteurs}| c={c} | typ={typ}")
                self.play(AnimationGroup(Indicate(select),Indicate(types[typ]),c.animate.set_value(c.get_value()+1)),run_time=u[n]/2)
                n+=1
                bandeau.append(graph)
        self.play(FadeOut(graphs[124],shift=RIGHT*3))
        self.play(AnimationGroup(
            *[Write(facto) for facto in factorielles]
        ))