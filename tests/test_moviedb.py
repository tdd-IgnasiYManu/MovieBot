import pytest
from src.moviedb.moviedbapi import busqueda, busca_relacionadas, buscar_id

def test_busqueda():
    res = busqueda('El señor de los anillos')
    assert res != None

def test_buscar_id():
    res = buscar_id(122)
    assert res != None

def test_busca_relacionadas():
    res = busca_relacionadas(122)
    assert res != None
