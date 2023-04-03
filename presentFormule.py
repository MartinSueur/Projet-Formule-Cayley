from manim import *
from arbres import *
from len import *
from layoutCreator import *
#from manim_slides import Slide

class PresentationFormule(Scene):
    def construct(self):
        
        cayley = Title(r"Présentation de la formule de Cayley")
        text1 = Text(r"Le nombre d'arbres étiquetés à n noeuds est :").move_to(UP*2).scale(0.5)
        formule = MathTex(r"T_n = n^{n-2}").move_to(UP)
        text2 = Text(r"Il y a donc ")
        listeStrSommets = ["arbre à 1 sommet","arbre à 2 sommets","arbres à 3 sommets","arbres à 4 sommets","arbres à 5 sommets","arbres à 6 sommets"]
        listeTextSommets = []
        listeNumFormule = [r"1^{-1}",r"2^0",r"3^1",r"4^2",r"5^3",r"6^4"]
        listeNumCalcule = ["1","1","3","16","125","1296"]
        listeTexFormule = []
        listeTexCalcule = []
        for i in range(6):
            listeTextSommets.append(Text(listeStrSommets[i]).move_to(DOWN*i*0.7).scale(0.5))
            listeTexFormule.append(MathTex(listeNumFormule[i]).next_to(listeTextSommets[i],LEFT,buff=0.2))
            listeTexCalcule.append(MathTex(listeNumCalcule[i]).next_to(listeTextSommets[i],LEFT,buff=0.2))
        self.play(Write(cayley))
        self.play(Write(text1))
        self.play(Write(formule))
        self.wait()
        self.play(Write(text2.next_to(listeTexCalcule[0],LEFT,buff=0.3).scale(0.5)))
        for i in range(6):
            self.play(
                Write(listeTexFormule[i]),
                Write(listeTextSommets[i]),
            )
        for i in range(6):
            self.play(Transform(listeTexFormule[i],listeTexCalcule[i]))
        