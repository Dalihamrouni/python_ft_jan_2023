from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 
# ? Render Page -  Form
@app.route('/')
def form():
    return render_template("form.html")
# ? Action Route  - Form Submit
@app.route('/process', methods=['POST'])
def process_form():
    print(f"{request.form} ****************")

    session['name'] = request.form['username']
    session['age'] = request.form['user_age']
    session['fav_food'] = request.form['fav_food']

    # ! NERVER EVER RENDER ON POST REQUESGT
    #! return render_template("display.html")
    return redirect('/display')
# ? Render Page -  Display
@app.route('/display')
def display():
    print(f"{request.form} ++++++++++++++++")
    print(f"{session} ------------")
    # eyJhZ2UiOiIzNSIsImZhdl9mb29kIjoiXHVkODNjXHVkZjgyIiwibmFtZSI6IkFsZXgifQ.Y9zgYw.xuAOjx3jC7VqamIpNxuMR55XIjA
    return render_template("display.html")

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/display')
    
if __name__ == '__main__':
    app.run(debug = True, port=5001)