from user import User

users = [
    User(1, 'bob', 'pass')
]

username_mapping = {u.username: u for u in users}
userId_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)  # none returns of the username doesnt exist.
    if user and user.password == password:
        return user
# finds correct user object using username from JWT and then we compare its password
# to the one we receive through the /auth endpoint
# then the auth endpoint returns a JWT (JSON Web Token)


def identity(payload):
    user_id = payload['identity']
    return userId_mapping.get(user_id, None)
