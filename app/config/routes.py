from system.core.router import routes

"""
    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""

routes['default_controller'] = 'Cats'


#--- cats
routes['GET']['/cats/getAllCats'] = 'Cats#getAllCats'
routes['GET']['/cats/selection/<id>'] = 'Cats#selection'

#--- users
routes['GET']['/users/register'] = 'Users#register'
routes['GET']['/users/isLogged'] = 'Users#isLogged'
routes['POST']['/users/add'] = 'Users#add'
routes['POST']['/users/login'] = 'Users#login'
routes['GET']['/users/logout'] = 'Users#logout'

routes['GET']['/users/getUserByEmail/<email>'] = 'Users#getUserByEmail'
routes['GET']['/users/getUserAddressByEmail/<email>'] = 'Users#getUserAddressByEmail'

#--- pricing
routes['GET']['/pricings/getPricing'] = 'Pricings#getPricing'
