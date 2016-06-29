from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
         # Note that we have to load the model before using it in the methods below
        self.load_model('User')

    # method to display registration page
    def index(self):
        #Loads home page
        print 'I am in travel controller home page'
        return self.load_view('new.html')


    def create(self):
        #register a new user - gather data posted to our create method and format it to pass it to the model
        user_info = {
            'f_name':request.form['f_name'],
            'l_name':request.form['l_name'],
            'email':request.form['email'],
            'passw':request.form['passw'],
            'conf_passw':request.form['conf_passw'],
        }
        # call create_user method from model and write some logic based on the returned value
        # notice how we passed the user_info to our model method
        create_status = self.models['User'].create_user(user_info)

        create_status = self.models['User'].create_user(user_info)
        if create_status['status'] == True:
            # the user should have been created in the model
            # we can set the newly-created users id and name to session
            session['id'] = create_status['user']['id'] 
            session['name'] = create_status['user']['name']
            # we can redirect to the users profile page here
            return redirect('/users')
        else:
            # set flashed error messages here from the error messages we returned from the Model
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            # redirect to the method that renders the form
            return redirect('/users/new')

        # print ('^' * 25)
        # print user
        # print ('^' * 25)
        # return redirect('/')

