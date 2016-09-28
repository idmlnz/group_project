from system.core.model import Model

class Pricing(Model):
    def __init__(self):
        super(Pricing, self).__init__()

    def getPricing(self):
        query = "SELECT * FROM pricing"
        return self.db.query_db(query)


