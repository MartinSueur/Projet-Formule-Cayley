def combinaisons(k,n):
    resultat = []
    for i in range(2**(n)+1):
        comb = []
        for j in range(n+1):
            if (i>>j)&1==1:
                comb.append(j)
        if len(comb)==k:
            resultat.append(comb)
    return resultat

def isomorphe(arbre1,arbre2): # (1,2) = (2,1) et [(2,1),(2,3)] = [(2,3),(2,1)]
    edges1 = arbre1[1]
    edges2 = arbre2[1]
    vertices1 = arbre1[0]
    vertices2 = arbre2[0]
    for e in edges1:
        if e not in edges2 and (e[1],e[0]) not in edges2:
            return False
    if len(edges1) != len(edges2):
        return False
    for v in vertices1:
        if v not in vertices2:
            return False
    if len(vertices1) != len(vertices2):
        return False
    return True

def test_isomorphe(showtrees=False):
    arbre1 = ([1,2,3],[(2,1),(2,3)])
    arbre2 = ([1,2,3],[(3,2),(1,2)])
    arbre3 = ([1,2,3],[(2,1)])
    arbre4 = ([1,2,3,4],[(2,1),(3,2)])
    print("BEGINNING TESTS OF isomorphe() FUNCTION")
    if showtrees:
        print(f"\n arbre1 = {arbre1}\n arbre2 = {arbre2}\n arbre3 = {arbre3}\n arbre4 = {arbre4}")

    if isomorphe(arbre1,arbre2):
        print("TEST1 : OK")
    else:
        print("TEST1 ERREUR : arbre1 et arbre2 sont isomorphes...")
    if not isomorphe(arbre1,arbre3):
        print("TEST2 : OK")
    else:
        print("TEST2 ERREUR : arbre1 et arbre2 ne sont pas isomorphes")
    if not isomorphe(arbre1,arbre4):
        print("TEST3 : OK")
    else:
        print("TEST3 ERREUR : arbre1 et arbre4 ne sont pas isomorphes")
    

def listePriveDeElement(liste,elt):
    listeprime = liste[:]
    if elt in listeprime:
        listeprime.remove(elt)
    return listeprime



def coupure_simple(n):
    vertices = [i+1 for i in range(n)]
    ligne = [(i,i+1) for i in range(1,n)]
    resultat = [(vertices,ligne)]
    for i in range(1,n-2):
        liste = ligne[:]
        dest = liste[i][1]
        for j in range(i-1,-1,-1):
            liste[j] = (liste[j][0],dest)
        resultat.append((vertices,liste))
    return resultat

def fact(n):
    if n ==1:
        return 1
    else:
        return fact(n-1)*n

def parmi(k,n):
    assert n >= k
    return fact(n)//(fact(k)*fact(n-k))


def decale_indice(indices,c,n): #c etant la taille du cycle
    i=0
    while indices[-1-i] == (n-i-2):
        #print(i,indices)
        i+=1
    indices[-1-i]+=1
    return indices

def test_decale_indice():
    l1 = [0,1,2,3]
    l2 = [0,1,2,4]
    l3 = [1,2,4,5]
    l4 = [1,2,3]
    print(decale_indice(l1,4,6))
    print(decale_indice(l2,4,6))
    print(decale_indice(l3,4,6))
    print(decale_indice(l4,3,6))

#test_decale_indice()

def tous_les_arbres(n):
    noeuds = [i+1 for i in range(n)]
    res = []
    c = 1
    if n==4:
        for v in noeuds:
            edges = []
            ne = [v]
            noeuds2 = listePriveDeElement(noeuds,v)
            for v2 in noeuds2:
                ne.append(v2)
                noeuds3 = listePriveDeElement(noeuds2,v2)
                for v3 in noeuds3:
                    for n1 in ne:
                        ne2 = ne+[v3]
                        noeuds4 = listePriveDeElement(noeuds3,v3)
                        for v4 in noeuds4:
                            for n2 in ne2:
                                edges.append((v,v2))
                                edges.append((v3,n1))
                                edges.append((v4,n2))
                                res.append((noeuds,edges))
                                edges = []
                                print(f"arbre{c} est fait")
                                c+=1
    if n==5:
        for v in noeuds:
            edges = []
            ne = [v]
            noeuds2 = listePriveDeElement(noeuds,v)
            for v2 in noeuds2:
                ne.append(v2)
                noeuds3 = listePriveDeElement(noeuds2,v2)
                for v3 in noeuds3:
                    for n1 in ne:
                        ne2 = ne+[v3]
                        noeuds4 = listePriveDeElement(noeuds3,v3)
                        for v4 in noeuds4:
                            for n2 in ne2:
                                ne3 = ne2+[v4]
                                noeuds5 = listePriveDeElement(noeuds4,v4)
                                for v5 in noeuds5:
                                    for n3 in ne3:
                                        edges.append((v,v2))
                                        edges.append((v3,n1))
                                        edges.append((v4,n2))
                                        edges.append((v5,n3))
                                        res.append((noeuds,edges))
                                        edges = []
                                        print(f"arbre{c} est fait")
                                        c+=1
    if n==6:
        for v in noeuds:
                edges = []
                ne = [v]
                noeuds2 = listePriveDeElement(noeuds,v)
                for v2 in noeuds2:
                    ne.append(v2)
                    noeuds3 = listePriveDeElement(noeuds2,v2)
                    for v3 in noeuds3:
                        for n1 in ne:
                            ne2 = ne+[v3]
                            noeuds4 = listePriveDeElement(noeuds3,v3)
                            for v4 in noeuds4:
                                for n2 in ne2:
                                    ne3 = ne2+[v4]
                                    noeuds5 = listePriveDeElement(noeuds4,v4)
                                    for v5 in noeuds5:
                                        for n3 in ne3:
                                            ne4 = ne3+[v5]
                                            noeuds6 = listePriveDeElement(noeuds5,v5)
                                            for v6 in noeuds6:
                                                for n4 in ne4:
                                                    edges.append((v,v2))
                                                    edges.append((v3,n1))
                                                    edges.append((v4,n2))
                                                    edges.append((v5,n3))
                                                    edges.append((v6,n4))
                                                    res.append((noeuds,edges))
                                                    edges = []
                                                    print(f"arbre{c} est fait")
                                                    c+=1
    if n==7:
        for v in noeuds:
                edges = []
                ne = [v]
                noeuds2 = listePriveDeElement(noeuds,v)
                for v2 in noeuds2:
                    ne.append(v2)
                    noeuds3 = listePriveDeElement(noeuds2,v2)
                    for v3 in noeuds3:
                        for n1 in ne:
                            ne2 = ne+[v3]
                            noeuds4 = listePriveDeElement(noeuds3,v3)
                            for v4 in noeuds4:
                                for n2 in ne2:
                                    ne3 = ne2+[v4]
                                    noeuds5 = listePriveDeElement(noeuds4,v4)
                                    for v5 in noeuds5:
                                        for n3 in ne3:
                                            ne4 = ne3+[v5]
                                            noeuds6 = listePriveDeElement(noeuds5,v5)
                                            for v6 in noeuds6:
                                                for n4 in ne4:
                                                    ne5 = ne4+[v6]
                                                    noeuds7 = listePriveDeElement(noeuds6,v6)
                                                    for v7 in noeuds7:
                                                        for n5 in ne5:
                                                            edges.append((v,v2))
                                                            edges.append((v3,n1))
                                                            edges.append((v4,n2))
                                                            edges.append((v5,n3))
                                                            edges.append((v6,n4))
                                                            edges.append((v7,n5))
                                                            res.append((noeuds,edges))
                                                            edges = []
                                                            print(f"arbre{c} est fait")
                                                            c+=1
    return res

def enleve_cycles(liste_arbres):
    n = len(liste_arbres[0][0])
    arbres_bis = liste_arbres[:]
    for arbre in liste_arbres:
        edges = arbre[1]
        for i in range(n-2,2,-1):
            combs = combinaisons(i,n)
            for j in range(parmi(i,n-1)):
                combinaison = [edges[k] for k in combs[j]]
                liste_noeud = []
                for edge in combinaison:
                    if edge[0] not in liste_noeud:
                        liste_noeud.append(edge[0])
                    if edge[1] not in liste_noeud:
                        liste_noeud.append(edge[1])
                if len(liste_noeud)==i:
                    print("arbre-1")
                    arbres_bis.remove(arbre)
    return arbres_bis
                


def reduire_isomorphismes(liste_arbres):
    resultat = [liste_arbres[0]]
    a = 0
    for arbre1 in liste_arbres:
        a+=1
        print(a)
        i=0
        c=0
        while c == 0 and i < len(resultat):
            if isomorphe(arbre1,resultat[i]):
                c=1
            i+=1
        if c==0:
            resultat.append(arbre1)
            print("+1 arbre")
    return resultat

def enlever_erreurs(liste_arbres):
    c=0
    liste_bis = liste_arbres[:]
    for arbre in liste_arbres:
        c+=1
        edges = arbre[1]
        for e in edges:
            if e[0]==e[1]:
                liste_bis.remove(arbre)
                break
            else:
                pass
                #print(c,edges)
    return liste_bis
    

l = tous_les_arbres(7)
print(len(l))
print("tous_les_arbres : Done")
l = reduire_isomorphismes(l)
print(len(l))
print("reduire_isomorphismes : Done")
l=enlever_erreurs(l)
print(len(l))
print("enlever_erreurs : Done")
l=enleve_cycles(l)
print("enleve_cycle : Done")
print(l)
print(len(l))
