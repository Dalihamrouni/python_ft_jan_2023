from flask_app import app
# ! Allways Remember To Import ALL ROUTES HERE (ALL CONTROLLERS)
from flask_app.controllers import authors

if __name__ == '__main__':
    app.run(debug=True, port=5003)