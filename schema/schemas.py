from models.model import User, Movies


def userSchema(user: User) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user.name,
        "username": user.username,
        "email": user.email,
        "password": user.password,
    }


def movieSchema(movie: Movies) -> dict:
    return {
        "id": str(movie["_id"]),
        "title": movie.title,
        "slug": movie.slug,
        "descriptions": movie.descripton,
        "duration": movie.duration
    }


def janiNaKiUser(users) -> list:
    return [userSchema(user) for user in users]
