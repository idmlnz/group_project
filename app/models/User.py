from system.core.model import Model
import re

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


    def checkUser(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 1:
            errors.append('Password must be at least 8 characters long')

        if errors:
            return {"status": False, "errors": errors}
        else:
            get_user_query = "SELECT * FROM user WHERE email=\"{}\"".format(info['email'])
            user = self.db.query_db(get_user_query)[0]
            if (info['password'] == user['password']):
                return {"status": True, "user": user}
            else:
                errors.append('Your email does not match your password!!')
                return {"status": False, "errors": errors}


    def createUser(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # Some basic validation
        if not info['firstname']:
            errors.append('firstname cannot be blank')
        elif len(info['firstname']) < 2:
            errors.append('firstname must be at least 2 characters long')

        if not info['lastname']:
            errors.append('lastname cannot be blank')
        elif len(info['lastname']) < 2:
            errors.append('lastname must be at least 2 characters long')

        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid [myemail@yahoo.com] !')

        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 1:
            errors.append('Password must be at least 8 characters long')

        elif info['password'] != info['confirm_password']:
            errors.append('Password and confirmation must match!')

        if errors:
            return {"status": False, "errors": errors}

        else:
            # add user to DB
            # pw_hash = bcrypt.generate_password_hash(info['password'])
            pw_hash = info['password']

            # check if user already exists
            get_user_query = "SELECT * FROM user where email=\"{}\"".format(info['email'])
            print "query: {}".format(get_user_query)

            try:
                user = self.db.query_db(get_user_query)
                print "Register.createUser : {}".format(user)
                if user:
                    errors.append("{} already exists! Try login-in".format(info['email']))
                    return {"status": False, "errors": errors}
            except:
                print "err.args"

            insertQuery = "INSERT INTO user (firstname, lastname, email, password, created_at, updated_at) \
                VALUES (:firstname, :lastname, :email, :password, NOW(), NOW())"

            userData = {
                'firstname': info['firstname'],
                'lastname': info['lastname'],
                'email': info['email'],
                'password': pw_hash
            }
            print "userdata: {}".format(userData)
            self.db.query_db(insertQuery, userData)

            get_user_query = "SELECT * FROM user ORDER BY id DESC LIMIT 1"
            user = self.db.query_db(get_user_query)
            return {"status": True, "user": user[0]}
