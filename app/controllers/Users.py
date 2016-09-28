from system.core.controller import *

class Users(Controller):
  def __init__(self, action):
    super(Users, self).__init__(action)
    self.load_model('User')
    self.db = self._app.db

  def index(self):
    pass

  def getUserByEmail(self, email):
    user = self.models['User'].getUserByEmail(email)
    return self.load_view('/index.html', data=user)


  def doAction(self, email):
    action = request.form['action']
    if (action == 'View Profile'):
      return self.displayUserView(email)

    if (action == 'Add as  Friend'):
      pass

    if (action == 'Remove as Friend'):
      pass

