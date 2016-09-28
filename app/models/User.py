from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def getUserByEmail(self, email):
        query = "SELECT * from user where email=\"{}\"".format(email)
        return self.db.query_db(query)

    def getUserAddressByEmail(self, email):
        query = "SELECT a. * FROM user AS u, address AS a WHERE u.email = \"{}\" AND u.id = a.user_id".format(email);
        print "BY EMAIL: {}.format(query)\n"
        return self.db.query_db(query)
