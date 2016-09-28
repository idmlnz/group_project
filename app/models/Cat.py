from system.core.model import Model

class Cat(Model):
    def __init__(self):
        super(Cat, self).__init__()

    def getAllCats(self):
        query = "SELECT * FROM cat"
        return self.db.query_db(query)


