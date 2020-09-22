#!/usr/bin/env python
import pytest
from src.database.bdinitializer import UserInfo
from src.database.queries import add_film

USER_ID = -1
INITIAL_FILMS = [10, 212]

def test_adding_film():
    add_film(USER_ID, INITIAL_FILMS)

    q = UserInfo.select()
    q.execute()

    user = q.first()

    assert user.user_id == USER_ID
    assert user.favourite_films == INITIAL_FILMS

    UserInfo.delete().where(UserInfo.user_id == USER_ID).execute()
