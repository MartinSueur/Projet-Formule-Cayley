from arbres import *

def occurences(arbre):
    vertices = arbre[0]
    edges = arbre[1]
    dicoOccurences = {}
    maxLienExt = 1
    for v in vertices:
        dicoOccurences[v] = 0
    for e in edges:
        dicoOccurences[e[0]] +=1
        dicoOccurences[e[1]] +=1
    for item in dicoOccurences.items():
        c=0
        if item[1] > 1:
            for e in edges:
                if e[0] == item[0]:
                    if dicoOccurences[e[1]] == 1:
                        c+=1
                elif e[1] == item[0]:
                    if dicoOccurences[e[0]] == 1:
                        c+=1
        if c > maxLienExt:
            maxLienExt = c
    return [maxLienExt]+list(dicoOccurences.values())

def memeTypes(type1,type2):
    if type1[0] != type2[0]:
        return False
    else:
        type1 = type1[1:]
        type2 = type2[1:]
    dico1 = {}
    dico2 = {}
    for o in type1:
        if o not in dico1:
            dico1[o] = 1
        else:
            dico1[o] += 1
    for o in type2:
        if o not in dico2:
            dico2[o] = 1
        else:
            dico2[o] += 1
    return dico1 == dico2
    


def typeDarbre(arbre):
    vals = occurences(arbre)
    n = len(arbre[0])
    type41 = [3, 3, 1, 1, 1]
    type42 = [1, 2, 2, 1, 1]
    type51 = [4, 4, 1, 1, 1, 1]
    type52 = [2, 3, 2, 1, 1, 1]
    type53 = [1, 2, 2, 2, 1, 1]
    type61 = [5, 5, 1, 1, 1, 1, 1]
    type62 = [3, 4, 2, 1, 1, 1, 1]
    type63 = [2, 3, 3, 1, 1, 1, 1]
    type64 = [1, 3, 2, 2, 1, 1, 1]
    type65 = [2, 3, 2, 1, 1, 2, 1]
    type66 = [1, 2, 2, 2, 2, 1, 1]
    if n == 4:
        if memeTypes(vals,type41):
            return 1
        if memeTypes(vals,type42):
            return 2
    elif n == 5:
        if memeTypes(vals,type51):
            return 1
        if memeTypes(vals,type52):
            return 2
        if memeTypes(vals,type53):
            return 3
    elif n == 6:
        if memeTypes(vals,type61):
            return 1
        if memeTypes(vals,type62):
            return 2
        if memeTypes(vals,type63):
            return 3
        if memeTypes(vals,type64):
            return 4
        if memeTypes(vals,type65):
            return 5
        if memeTypes(vals,type66):
            return 6


def TrouverTypes(listeArbres):
    listeTypes = []
    for a in listeArbres:
        vs = occurences(a)
        if listeTypes == []:
            listeTypes.append(vs)
        else:
            n=0
            for typ in listeTypes:
                if not memeTypes(typ,vs):
                    n+=1
            if n==len(listeTypes):
                listeTypes.append(vs)
    return listeTypes

arbres4 = [([1, 2, 3, 4], [(1, 2), (3, 1), (4, 1)]), ([1, 2, 3, 4], [(1, 2), (3, 1), (4, 2)]), ([1, 2, 3, 4], [(1, 2), (3, 1), (4, 3)]), ([1, 2, 3, 4], [(1, 2), (3, 2), (4, 1)]), ([1, 2, 3, 4], [(1, 2), (3, 2), (4, 2)]), ([1, 2, 3, 4], [(1, 2), (3, 2), (4, 3)]), ([1, 2, 3, 4], [(1, 2), (4, 1), (3, 4)]), ([1, 2, 3, 4], [(1, 2), (4, 2), (3, 4)]), ([1, 2, 3, 4], [(1, 3), (2, 3), (4, 1)]), ([1, 2, 3, 4], [(1, 3), (2, 3), (4, 2)]), ([1, 2, 3, 4], [(1, 3), (2, 3), (4, 3)]), ([1, 2, 3, 4], [(1, 3), (4, 1), (2, 4)]), ([1, 2, 3, 4], [(1, 3), (4, 3), (2, 4)]), ([1, 2, 3, 4], [(1, 4), (2, 3), (3, 4)]), ([1, 2, 3, 4], [(1, 4), (2, 4), (3, 2)]), ([1, 2, 3, 4], [(1, 4), (2, 4), (3, 4)])]

print(TrouverTypes(arbres5))