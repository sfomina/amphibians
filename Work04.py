import flask

my_app = flask.Flask(__name__)

@my_app.route('/')

def root():
    return "Are both frogs and toads amphibians?"
1


@my_app.route('/frog')

def frog():
    return "ribbit"



@my_app.route('/toad')

def toad():
    return "croak"



@my_app.route('/amphibians')

def amph():
    return "Yes, they are both amphibians"

if __name__ == "__main__":
    my_app.run()
    
