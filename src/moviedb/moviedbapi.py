#!/usr/bin/env python
import os
import requests as rq
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

TMDb_KEY = os.getenv('TMDb_KEY')
language = os.getenv('language')

def realiza_peticion(url: str):
    res = rq.get(url)
    res = res.json()['results'] if res.json()['results'] else None

    return res


def busqueda(query: str):
    return realiza_peticion(f'https://api.themoviedb.org/3/search/movie?api_key={TMDb_KEY}&query={query}&language={language}')


def busca_relacionadas(movie_id: int):
    return realiza_peticion(f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={TMDb_KEY}&language={language}')

