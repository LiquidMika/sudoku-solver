import pytest
from sudoku import *


def test_ligne_complete():
    assert ligne_complete(L1, 2) == False
    assert ligne_complete(L1, 3) == True


def test_complet():
    assert complet(L1) == False
    assert complet(L2) == True


def test_ligne():
    assert ligne(L1, 6) == [3, 7, 6, 4]


def test_carre():
    assert carre(L1, 7, 4) == [7, 1, 4, 6]
    assert carre(L2, 0, 0) == [1, 2, 3, 2, 3, 4, 3, 4, 5]
    assert carre(L1, 8, 8) == [6, 4, 2, 1, 7]


def test_colonne():
    assert colonne(L1, 0) == [4, 5, 6, 1, 3, 2]
    assert colonne(L1, 2) == [7, 6]
    assert colonne(L1, 8) == [5, 8, 1, 9, 3, 6, 4, 2, 7]


def test_colonne_complete():
    assert colonne_complete(L1, 0) == False
    assert colonne_complete(L1, 8) == True
    assert colonne_complete(L2, 4) == True


def test_carre_complet():
    assert carre_complet(L3, 0) == True
    assert carre_complet(L3, 1) == False
    assert carre_complet(L3, 2) == False
    assert carre_complet(L3, 7) == True
    assert carre_complet(L3, 8) == False


def test_conflit():
    assert conflit(L, 0, 0) == [1, 2, 3, 4, 5, 6, 7]
    assert conflit(L, 1, 0) == [1, 2, 3, 6, 7, 9]
    assert conflit(L, 0, 1) == [2, 4, 5, 7]
    assert conflit(L2, 8, 0) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert conflit(L4, 4, 4) == []


def test_chiffres_ok():
    assert chiffres_ok(L, 0, 0) == [8, 9]
    assert chiffres_ok(L, 1, 0) == [4, 5, 8]
    assert chiffres_ok(L, 0, 1) == [1, 3, 6, 8, 9]
    assert chiffres_ok(L2, 8, 0) == [9]
    assert chiffres_ok(L4, 4, 4) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert chiffres_ok(L, 4, 2) == [2, 5, 8, 9]


def test_nb_possible():
    assert nb_possible(L, 0, 0) == 2
    assert nb_possible(L, 1, 0) == 3
    assert nb_possible(L, 0, 1) == 5
    assert nb_possible(L2, 8, 0) == 1
    assert nb_possible(L4, 4, 4) == 9
    assert nb_possible(L, 4, 2) == 4

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


L = [
    [0, 6, 0, 0, 0, 0, 2, 0, 5],
    [4, 0, 0, 9, 2, 1, 0, 0, 0],
    [0, 7, 0, 0, 0, 8, 0, 0, 1],
    [0, 0, 0, 0, 0, 5, 0, 0, 9],
    [6, 4, 0, 0, 0, 0, 0, 7, 3],
    [1, 0, 0, 4, 0, 0, 0, 0, 0],
    [3, 0, 0, 7, 0, 0, 0, 6, 0],
    [0, 0, 0, 1, 4, 6, 0, 0, 2],
    [2, 0, 6, 0, 0, 0, 0, 1, 0],
]

L1 = [
    [0, 6, 0, 0, 0, 0, 2, 0, 5],
    [4, 0, 0, 9, 2, 1, 0, 0, 8],
    [0, 7, 0, 0, 0, 8, 0, 0, 1],
    [5, 8, 7, 6, 1, 3, 4, 2, 9],
    [6, 4, 0, 0, 0, 0, 0, 7, 3],
    [1, 0, 0, 4, 0, 0, 0, 0, 6],
    [3, 0, 0, 7, 0, 0, 0, 6, 4],
    [0, 0, 0, 1, 4, 6, 0, 0, 2],
    [2, 0, 6, 0, 0, 0, 0, 1, 7],
]

L2 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8],
]

L3 = [
    [1, 2, 3, 1, 2, 3, 7, 8, 9],
    [4, 5, 6, 4, 0, 6, 8, 9, 1],
    [7, 8, 9, 7, 8, 9, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 4, 5, 6, 5, 6, 7],
    [9, 1, 2, 7, 8, 9, 6, 7, 8],
]

L4 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
