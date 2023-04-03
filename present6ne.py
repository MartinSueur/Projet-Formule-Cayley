from manim import *
from arbres import *
from len import *
from layoutCreator import *
from serieFinder import v

class Arbres6noeuds(Scene):
    def construct(self):
        listTypes = [[(1,2),(2,3),(2,4),(2,5),(2,6)],   #etoile
                     [(1,2),(2,3),(3,4),(3,5),(3,6)],   #fourche
                     [(1,3),(2,3),(3,4),(4,5),(4,6)],   #chormosome
                     [(1,2),(2,3),(2,4),(3,5),(4,6)],   #osselet
                     [(1,2),(2,3),(3,4),(4,5),(4,6)],   #cuillere
                     [(1,2),(2,3),(3,4),(4,5),(5,6)]]   #tige

        cible = [[4,0,0],
                 [0,0,0],
                 [-4,-2,0],
                 [0,-2,0],
                 [-4,0,0],
                 [4,-2,0]]

        types = [Graph([1,2,3,4,5,6],e,layout="partite",partitions=LayoutAuto(([1,2,3,4,5,6],e))).move_to(cible[i]).scale(0.5) for i,e in enumerate(listTypes)]

        compteurs = [Integer(number=0).next_to(c,DOWN) for c in cible]

        graphs = [Graph(vertices, edges, labels=True, layout="partite",partitions=LayoutAuto((vertices,edges))).scale(0.5).shift(LEFT*4+UP*2.5) for (vertices,edges) in arbres6]+[Graph([],[])]*3

        p=0
        factorielles = []
        texte = [r"\frac{6!}{5!}",r"\frac{6!}{3!}",r"\frac{6!}{(2!)^3}",r"\frac{6!}{2!}",r"\frac{6!}{2!}",r"\frac{6!}{2!}",]
        

        n=0

        self.play(AnimationGroup(*[Write(typ) for typ in types]+[Write(c) for c in compteurs]))
        bandeau = []
        for graph in graphs:
            if len(bandeau) < 3:
                self.play(AnimationGroup(
                FadeIn(graph,shift=RIGHT*3),
                AnimationGroup(*[arbre.animate.shift(RIGHT*3) for arbre in bandeau])),run_time=v[n]/2)
                n+=1
                bandeau.append(graph)
            elif len(bandeau) > 2 and len(bandeau) < 4:
                self.play(AnimationGroup(
                FadeIn(graph,shift=RIGHT*3),
                AnimationGroup(*[arbre.animate.shift(RIGHT*3) for arbre in bandeau])),run_time=v[n]/2)
                n+=1
                select = bandeau[0]
                typ = typeDarbre(([1,2,3,4,5,6],select.edges))-1
                c = compteurs[typ]
                self.play(AnimationGroup(Indicate(select),Indicate(types[typ]),c.animate.set_value(c.get_value()+1)),run_time=v[n]/2)
                n+=1
                bandeau.append(graph)
            else:
                self.play(AnimationGroup(
                FadeIn(graph,shift=RIGHT*3),
                AnimationGroup(*[arbre.animate.shift(RIGHT*3) for arbre in bandeau]),
                FadeOut(bandeau.pop(0),shift=RIGHT*3)),run_time=v[n]/2)
                n+=1
                select = bandeau[0]
                typ = typeDarbre(([1,2,3,4,5,6],select.edges))-1
                c = compteurs[typ]
                self.play(AnimationGroup(Indicate(select),Indicate(types[typ]),c.animate.set_value(c.get_value()+1)),run_time=v[n]/2)
                n+=1
                bandeau.append(graph)
        self.play(FadeOut(graphs[1295],shift=RIGHT*3))
        self.play(AnimationGroup(AnimationGroup(*[t.animate.shift(UP*2) for t in [types[4],types[0],types[1]]]+[t.animate.shift(UP) for t in [types[2],types[3],types[5]]]),
                  AnimationGroup(*[c.animate.shift(UP*2) for c in [compteurs[4],compteurs[0],compteurs[1]]]+[c.animate.shift(UP) for c in [compteurs[2],compteurs[3],compteurs[5]]])))
        
        for c in compteurs:
            factorielles.append(MathTex(texte[p]).next_to(c,DOWN))
            p+=1
        
        self.play(AnimationGroup(
            *[Write(facto) for facto in factorielles]
        ))