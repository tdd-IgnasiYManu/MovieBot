#!/usr/bin/env python
from bdinitializer import UserInfo

def add_film(user_id: int, film_id: int):
    query = UserInfo.select().where(UserInfo.user_id == user_id)
    user = query.first()

    if user == None:
        UserInfo.create(user_id=user_id, film_id=[film_id])
    else:
        if film_id not in user.favourite_films:
            user.favourite_films.append(film_id)

            q = UserInfo.update({UserInfo.favourite_films: user.favourite_films}).where(UserInfo.user_id == user_id)
            updated_rows = q.execute()
        
    return updated_rows


def remove_film(user_id: int, film_id: int):
    query = UserInfo.select().where(UserInfo.user_id == user_id)
    user = query.first()

    if user is not None:
        if film_id in user.favourite_films:
            user.favourite_films.remove(film_id)

            if len(user.favourite_films) == 0:
                query = UserInfo.delete().where(UserInfo.user_id == user_id)
                updated_rows = query.execute()
            else:
                query = UserInfo.update({UserInfo.favourite_films: user.favourite_films}).where(UserInfo.user_id == user_id)
                updated_rows = query.execute()
    
    return updated_rows

def search_films(user_id: int):
    query = UserInfo.select().where(UserInfo.user_id == user_id)
    user = query.first()
    
    return user.favourite_films