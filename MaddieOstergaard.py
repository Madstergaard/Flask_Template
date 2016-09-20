from flask import Flask # Capital Flask is a subset of the module flask

fred = Flask(__name__)

@fred.route("/") # decorator, goes directly above funtion header, the 
                 # "/" (route) for webpage will run this function
def welcome():
    return "Welcome to the site"


@fred.route("/help")
def hola():
    return __name__ + "\thola!"


@fred.route("/forthewinners")
def winners():
    return "we are da champions"

if __name__ == '__main__':
    fred.run()

