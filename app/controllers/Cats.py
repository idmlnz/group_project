from system.core.controller import *

class Cats(Controller):
  def __init__(self, action):
    super(Cats, self).__init__(action)
    self.load_model('Cat')
    self.db = self._app.db

  def index(self):
    return self.load_view('/intro.html')

  def getAllCats(self):
    cats = self.models['Cat'].getAllCats()
    return self.load_view('/index.html', data=cats)


