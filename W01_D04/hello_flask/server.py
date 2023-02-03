from flask import Flask , render_template

app = Flask(__name__)

# localhost:5000
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'

@app.route('/hello')
def hello():
    return "Hello"

@app.route('/hello/<my_name>')
def hello_my_name(my_name):
    print(my_name)
    # return f"<h3> Hello {my_name}</h3> <script>alert('You are hacked')</script>"* 10
    return render_template("index.html", name = my_name)
      
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)    # Run the app in debug mode.