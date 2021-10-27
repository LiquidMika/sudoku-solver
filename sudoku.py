def ligne_complete(L, i):
    """
    Return True if the ith line of Matrix L is correct
    """
    rep = True
    for n in range(1, 10):
        if n in L[i]:
            continue
        else:
            rep = False
            break
    return rep


def complet(L):
    rep = True
    for n in range(9):
        if ligne_complete(L, n):
            continue
        else:
            rep = False
            break
    return rep


def ligne(L, i):
    return [x for x in L[i] if x != 0]


def carre(L, i, j):
    icoin = 3 * (i // 3)
    jcoin = 3 * (j // 3)
    return [
        L[x][y]
        for x in range(icoin, icoin + 3)
        for y in range(jcoin, jcoin + 3)
        if L[x][y] != 0
    ]


def colonne(L, i):
    return [x[i] for x in L if x[i] != 0]


def colonne_complete(L, i):
    rep = True
    col = [x[i] for x in L]
    for n in range(1, 10):
        if n in col:
            continue
        else:
            rep = False
            break
    return rep


def carre_complet(L, i):
    rep = True
    icoin = 3 * (i % 3)
    jcoin = 3 * (i // 3)
    carre = [L[x][y] for x in range(jcoin, jcoin + 3) for y in range(icoin, icoin + 3)]
    for n in range(1, 10):
        if n in carre:
            continue
        else:
            rep = False
            break
    return rep


def conflit(L, i, j):
    not_ok = set()
    for k in ligne(L, i):
        not_ok.add(k)
    for k in colonne(L, j):
        not_ok.add(k)
    for k in carre(L, i, j):
        not_ok.add(k)
    try:
        not_ok.remove(L[i][j])
    except KeyError:
        pass
    return list(not_ok)


def chiffres_ok(L, i, j):
    ok = []
    list_conflit = conflit(L, i, j)
    for k in range(1, 10):
        if k not in list_conflit:
            ok.append(k)
    return ok


def nb_possible(L, i, j):
    return len(chiffres_ok(L, i, j))


def un_tour(L):
    changement = False
    for i in range(9):
        for j in range(9):
            if L[i][j] == 0:
                if nb_possible(L, i, j) == 1:
                    L[i][j] = chiffres_ok(L, i, j)[0]
                    changement = True
    return changement


def complete(L):
    nb_tour = 0
    while un_tour(L):
        nb_tour += 1
    return nb_tour


def affiche(L):
    print("\n")
    for i in L:
        print(i)


M = [
    [2, 0, 0, 0, 9, 0, 3, 0, 0],
    [0, 1, 9, 0, 8, 0, 0, 7, 4],
    [0, 0, 8, 4, 0, 0, 6, 2, 0],
    [5, 9, 0, 6, 2, 1, 0, 0, 0],
    [0, 2, 7, 0, 0, 0, 1, 6, 0],
    [0, 0, 0, 5, 7, 4, 0, 9, 3],
    [0, 8, 5, 0, 0, 9, 7, 0, 0],
    [9, 3, 0, 0, 5, 0, 8, 4, 0],
    [0, 0, 2, 0, 6, 0, 0, 0, 1],
]

N = [
    [0, 1, 0, 0, 9, 0, 0, 3, 0],
    [0, 0, 0, 2, 0, 0, 0, 4, 0],
    [8, 2, 0, 7, 0, 3, 1, 0, 0],
    [0, 0, 5, 9, 0, 0, 0, 0, 0],
    [6, 0, 0, 0, 8, 5, 4, 2, 9],
    [2, 0, 8, 0, 0, 4, 0, 6, 1],
    [7, 0, 0, 0, 3, 0, 0, 8, 0],
    [0, 0, 0, 8, 0, 0, 0, 0, 3],
    [0, 0, 1, 0, 4, 0, 2, 0, 7],
]

affiche(N)
print("\n", complete(N), " tours")
affiche(N)
