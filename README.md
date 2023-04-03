# Projet-Formule-Cayley
All the code I wrote and used during the progress of the projet about Cayley Formula
##Algorithms
TrouverArbre.py is the python implementation of the finds all trees algorithm. It only works up to 6 vertices because the amount of trees in the list exceeds what my memory can manage.

len.py is the python implementation of the finds all types algorithm. It works for any list of trees.

arbres.py is the result of the finds all trees algorithm for 4 vertices to 6 vertices, I stored these lists in this file because the execution of the finds all trees algorithm takes a lot of time.

layoutCreator.py contains the AutoLayout() function that allows me to render every tree of the same type with the same layout.

serieFinder.py initialises the two lists i use to manage the time of the present5ne animation and present6ne animation, with respectively the lists u and v.

##Animations

presentFormule is an animation presenting the Cayley tree Formula, and the first values of the numbers of trees with n vertices.

present123ne is an animation rendering the unique tree with 1 vertice, the unique tree with 2 vertices and the 3 trees with 3 vertices.

present4ne renders the 16 trees with 4 vertices and sort them by type.

present5ne renders the 125 trees with 5 vertices and sort them by type.

present6ne renders the 1296 trees with 6 vertices and sort them by type.
