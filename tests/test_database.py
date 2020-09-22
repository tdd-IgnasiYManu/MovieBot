import pytest
from src.database.bdinitializer import UserInfo
from src.database.queries import add_film, remove_film, search_films

USER_ID = -1
FILMS = [10, 212]

def test_adding_film():
    add_film(USER_ID, FILMS[0])
    add_film(USER_ID, FILMS[1])

    q = UserInfo.select()
    q.execute()

    user = q.first()

    assert user.user_id == USER_ID
    assert user.favourite_films == FILMS

    UserInfo.delete().where(UserInfo.user_id == USER_ID).execute()

def test_remove_film():
    add_film(USER_ID, FILMS[0])
    add_film(USER_ID, FILMS[1])

    q = UserInfo.select()
    q.execute()

    user = q.first()
    assert user.user_id == USER_ID
    assert user.favourite_films == FILMS

    remove_film(USER_ID, 212)

    q = UserInfo.select()
    q.execute()

    user = q.first()
    assert user.user_id == USER_ID
    assert user.favourite_films == [10]

    UserInfo.delete().where(UserInfo.user_id == USER_ID).execute()

def test_search_film():
    add_film(USER_ID, FILMS[0])
    add_film(USER_ID, FILMS[1])

    q = UserInfo.select()
    q.execute()

    user = q.first()
    assert user.user_id == USER_ID
    assert user.favourite_films == FILMS

    films = search_films(USER_ID)
    assert films != None

    UserInfo.delete().where(UserInfo.user_id == USER_ID).execute()
