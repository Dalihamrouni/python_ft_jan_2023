from flask_app import  app
# ! REMEMBER TO IMPORT ALL ROUTES HERE
from flask_app.controllers import users, books
# from flask_app.controllers import books



if __name__ == '__main__':
    app.run(debug=True, port=5001)
