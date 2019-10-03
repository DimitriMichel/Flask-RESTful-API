import sqlite3

# moved into model folder because the api cannot receive data or send JSON from this class
# these methods below allow us to receive user help us store information about a user
# also these methods allow us to retrieve user objects from a database


class UserModel:
    TABLE_NAME = 'users'

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
# here we set methods to retrieve the username and password from a user in our database

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
# after this declaration all cursor methods are bound to the declared database of 'data.db'
        query = "SELECT * FROM {table} WHERE username=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (username,))  # must be a tuple in order to have a tuple we need the comma(x,)
        row = result.fetchone()
# our row = result.fetchone just means row will equal the first username found
        if row:
            user = cls(*row)    # (*args) recall * is all and args is arguments this code fills with database info
        else:                   # cls(*row) fills in with our CLASS arguments of (_id, username, password)
            user = None

        connection.close()      # this line tells us the cursor will be unusable from this point forward
        return user
# here we define a class function that will find our user's username from a SQL database

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
# here we define a class function that will find our user's id from a SQL database
# otherwise the same things are happening here
