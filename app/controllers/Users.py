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

  def getUserAddressByEmail(self, email):
    user = self.models['User'].getUserAddressByEmail(email)
    return self.load_view('/index.html', data=user)

  def isLogged(self):
    # - check if user is login
    try:
      session['userid']
      print '\nuserid is SET'
      # -- display rent/adopt modal
      isLogged = {'value':1}
      return jsonify(isLogged=isLogged)

    except KeyError:
      print '\nuserid is NOT set'
      # -- display login modal
      isLogged = {'value':0}
      return jsonify(isLogged=isLogged)


  def add(self):
    userInfo = {}
    userInfo['firstname'] = request.form['firstname']
    userInfo['lastname'] = request.form['lastname']
    userInfo['email'] = request.form['email']
    userInfo['password'] = request.form['password']
    userInfo['confirm_password'] = request.form['confirm_password']

    createStatus = self.models['User'].createUser(userInfo)
    print "createstatus: {}".format(createStatus)
    if createStatus['status'] == True:
      session['userid'] = userInfo['email']
      print "ADD user successful for: {}".format(userInfo['email'])
    else:
      for message in createStatus['errors']:
        flash(message, 'regis_errors')
      return self.load_view('registration/register.html', error=createStatus['errors'])

    return redirect('/cats/catView')

  def login(self):
    userInfo = {}
    userInfo['email'] = request.form['login-email']

    userInfo['password'] = request.form['login-password']
    loginStatus = self.models['User'].checkUser(userInfo)

    if loginStatus['status'] == True:
      session['user'] = loginStatus['user']

    else:

      for message in loginStatus['errors']:
        flash(message, 'regis_errors')
      return self.load_view('users/users.html', error=loginStatus['errors'])

    print "LOGIN successful for: {}".format(userInfo['email'])
    session['userid'] = userInfo['email']
    return redirect('/cats/catView')


  def logout(self):
    session.clear()
    print "\nSESSION is cleared on LOGOUT\n"
    return redirect('/')  # redirect to / FOR NOW
