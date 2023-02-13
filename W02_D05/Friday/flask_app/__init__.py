from flask import Flask
app = Flask(__name__)
# ! Session Key is Required
app.secret_key = "Trust the Process"
DATABASE = "friday_db"