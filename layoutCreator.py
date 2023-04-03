from len import *

def dictio(arbre):
    vertices = arbre[0]
    edges = arbre[1]
    dicoOccurences = {}
    for v in vertices:
        dicoOccurences[v] = 0
    for e in edges:
        dicoOccurences[e[0]] +=1
        dicoOccurences[e[1]] +=1
    return dicoOccurences

def LayoutAuto(arbre):
    n = len(arbre[0])
    if n == 1:
        return layout1(arbre)
    elif n == 2:
        return layout2(arbre)
    elif n == 3:
        return layout3(arbre)
    elif n == 4:
        return layout4(arbre)
    elif n == 5:
        return layout5(arbre)
    elif n == 6:
        return layout6(arbre)
    else:
        return None

def layout1(arbre):
    vertices = arbre[0]
    return [vertices]

def layout2(arbre):
    t = typeDarbre(arbre)
    edges = arbre[1]
    e1 = edges[0][0]
    e2 = edges[0][1]
    return [[e1],[e2]]
    

def layout3(arbre):
    edges = arbre[1]
    extremites = []
    pont = []
    centre = []
    dico = dictio(arbre)
    for item in dico.items():
        if item[1] == 1:
            extremites.append(item[0])
        elif item[1] == 2:
            centre.append(item[0])
    return [[extremites[0]],centre,[extremites[1]]]

def layout4(arbre):
    t = typeDarbre(arbre)
    edges = arbre[1]
    extremites = []
    pont = []
    centre = []
    dico = dictio(arbre)
    if t == 1: # lance pierre
        for item in dico.items():
            if item[1] == 1:
                extremites.append(item[0])
            if item[1] == 3:
                centre.append(item[0])
        return [extremites[:1],centre,extremites[1:]]
    elif t == 2: # planche
        for item in dico.items():
            if item[1] == 1:
                extremites.append(item[0])
            if item[1] == 2:
                pont.append(item[0])
        e1 = extremites[0]
        e2 = extremites[1]
        for p in pont:
            if (p,e1) in edges or (e1,p) in edges:
                p1 = p
            else:
                p2 = p
        return [[e1],[p1],[p2],[e2]]
    else:
        return None

def layout5(arbre):
    t = typeDarbre(arbre)
    edges = arbre[1]
    extremites = []
    pont = []
    centre = []
    dico = dictio(arbre)
    if t == 1: # trident -> 1 1 3
        for item in dico.items():
            if item[1] == 1:
                extremites.append(item[0])
            if item[1] == 4:
                centre.append(item[0])
        return [extremites[:1],centre,extremites[1:]]
    elif t == 2: # bequille -> 1 1 1 2
        for item in dico.items():
            if item[1] == 1:
                extremites.append(item[0])
            if item[1] == 2:
                pont.append(item[0])
            if item[1] == 3:
                centre.append(item[0])
        for e in extremites:
            if (e,pont[0]) in edges or (pont[0],e) in edges:
                ep = e
        extremites.remove(ep)
        return [[ep],pont,centre,extremites]
    elif t == 3: # droite -> 1 1 1 1 1
        for item in dico.items():
            if item[1] == 1:
                extremites.append(item[0])
            if item[1] == 2:
                pont.append(item[0])
        e1 = extremites[0]
        e2 = extremites[1]
        for p in pont:
            if (e1,p) in edges or (p,e1) in edges:
                p1 = p
            elif (e2,p) in edges or (p,e2) in edges:
                p3 = p
            else:
                p2 = p
        return [[e1],[p1],[p2],[p3],[e2]]

    else:
        return None

def layout6(arbre):
    t = typeDarbre(arbre)
    edges = arbre[1]
    extremites = []
    pont = []
    centre = []
    dico = dictio(arbre)
    if t == 1:#etoile -> 4 1 1
        for item in dico.items():
            if item[1] == 1:
                extremites.append(item[0])
            if item[1] == 5:
                centre.append(item[0])
        partition = [extremites[:1],centre,extremites[1:]]
    elif t == 2:# fourche -> 3 1 1 1
        for item in dico.items():
            if item[1] == 1:
                extremites.append(item[0])
            if item[1] == 2:
                pont.append(item[0])
            if item[1] == 4:
                centre.append(item[0])
        for e in extremites:
            if (e,centre[0]) not in edges and (centre[0],e) not in edges:
                e1 = e
                extremites.remove(e1)
        partition = [[e1],pont,centre,extremites]
    elif t == 3:# chromosome -> 2 1 1 2
        for item in dico.items():
            if item[1] == 1:
                extremites.append(item[0])
            if item[1] == 2:
                pont.append(item[0])
            if item[1] == 3:
                centre.append(item[0])
        extremites0 = []
        for e in extremites:
            if (e,centre[0]) in edges or (centre[0],e) in edges:
                extremites0.append(e)
        for e in extremites0:
            extremites.remove(e)
        partition = [extremites0,centre[:1],centre[1:],extremites]
    elif t == 4:# osselet -> 2 2 1 1
        for item in dico.items():
            if item[1] == 1:
                extremites.append(item[0])
            if item[1] == 2:
                pont.append(item[0])
            if item[1] == 3:
                centre.append(item[0])
        for e in extremites:
            if (e,centre[0]) in edges or (centre[0],e) in edges:
                e1 = e
        extremites.remove(e1)
        for e in extremites:
            if (e,pont[0]) in edges or (pont[0],e) in edges:
                pont = [pont[1],pont[0]]
            else:
                pont = [pont[0],pont[1]]
        partition = [[e1],centre,pont,extremites]
    elif t == 5:# cuillere -> 2 1 1 1 1
        for item in dico.items():
            if item[1] == 1:
                extremites.append(item[0])
            if item[1] == 2:
                pont.append(item[0])
            if item[1] == 3:
                centre.append(item[0])
        bout = []
        for e in extremites:
            if (e,centre[0]) in edges or (centre[0],e) in edges:
                bout.append(e)
        for p in pont:
            if (p,centre[0]) in edges or (centre[0],p) in edges:
                p1 = p
            else:
                p2 = p
        for e in extremites:
            if e not in bout:
                e0 = e
        partition = [[e0],[p2],[p1],centre,bout]

    elif t == 6:# tige -> 1 1 1 1 1 1
        for item in dico.items():
            if item[1] == 1:
                extremites.append(item[0])
            if item[1] == 2:
                pont.append(item[0])
        e1 = extremites[0]
        e2 = extremites[1]
        for edge in edges:
            if edge[0] == e1:
                p1 = edge[1]
            elif edge[1] == e1:
                p1 = edge[0]
        for edge in edges:
            if edge[0] == p1 and edge[1] != e1:
                p2 = edge[1]
            elif edge[1] == p1 and edge[0] != e1:
                p2 = edge[0]
        for edge in edges:
            if edge[0] == p2 and edge[1] != p1:
                p3 = edge[1]
            elif edge[1] == p2 and edge[0] != p1:
                p3 = edge[0]
        for edge in edges:
            if edge[0] == p3 and edge[1] != p2:
                p4 = edge[1]
            elif edge[1] == p3 and edge[0] != p2:
                p4 = edge[0]
        partition = [[e1],[p1],[p2],[p3],[p4],[e2]]
    else:
        partition = None
    return partition


