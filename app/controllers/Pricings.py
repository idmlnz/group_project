from system.core.controller import *

class Pricings(Controller):
  def __init__(self, action):
    super(Pricings, self).__init__(action)
    self.load_model('Pricing')
    self.db = self._app.db

  def index(self):
    pass

  def getPricing(self):
    pricing = self.models['Pricing'].getPricing()
    return self.load_view('/index.html', data=pricing)


