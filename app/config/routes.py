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

routes['default_controller'] = 'Welcome'


#--- cats
routes['GET']['/cats/getAllCats'] = 'Cats#getAllCats'

#--- users
routes['GET']['/users/getUserByEmail/<email>'] = 'Users#getUserByEmail'
routes['GET']['/users/getUserAddressByEmail/<email>'] = 'Users#getUserAddressByEmail'

#--- pricing
routes['GET']['/pricings/getPricing'] = 'Pricings#getPricing'
