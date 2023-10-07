def userSchema(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"],
    }


def index(users) -> list:
    return [userSchema(user) for user in users]
