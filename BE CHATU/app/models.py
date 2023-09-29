from ..database import DatabaseConnection

class User:
    _keys = ["user_id", "username", "password", "email", "profile image"]

    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.email = kwargs.get("email")
        self.profile_image = kwargs.get("profile_image")

    def serialize(self):
        return{
            "user_id": self.user_id,
            "username" : self.username,
            "password" : self.password,
            "email" : self.email,
            "profile_image" : self.profile_image,
        }    

@classmethod
def create(cls, user):
    query = """ INSERT INTO chatuniverse.users (username, password, email, profile_image)
                VALUES (%(username)s, %(password)s, %(email)s, %(profile_image)s)"""
    params = user._dict_
    DatabaseConnection.execute_query(query, params)

@classmethod
def delete(cls, user)
    query = "DELETE FROM chatuniverse.users Where user_id = %(user_id)s"
    params = user._dict_
    DatabaseConnection.execute_query(query, params)

@classmethod
def get(cls, user=Nome):
    if user is not None and user.user_id is not None:
        query = """SELECT user_id, username, password, email, profile_image
                    FROM chatuniverse.users WHERE user_id = %(user_id)s"""
        params = user._dict_
        result = DatabaseConnection.fetch one(query, params)
        if result:
            return cls(**dict(zip(cls._keys, result)))
        else: 
            return None
    else:
    query = "SELECT user_id, username, password, email, profile_image FROM chatuniverse.user"
    results = DatabaseConnection.fetch_all(query)
    users = []
    for row in results:
        users.append(cls(**dict(zip(cls._keys, result))))
    return users

    @classmethod
    def Login(cls, user):
        query = """SELECT user_id, username, email, profile_image
                FROM chatuniverse.users
                WHERE username = %(username)s AND password = %(password)s"""
        params = user._dict_
        result = DatabaseConnection.fetch_one (query, params)
        if result: 
            return cls(**dict(zip(cls.keys, results)))      
        else:
            return None